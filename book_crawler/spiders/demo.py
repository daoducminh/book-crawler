# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request
from scrapy.http.response import Response
from scrapy.loader import ItemLoader

from book_crawler.items import Chapter, BookInfo
from utilities.books.chapter_utilities import append_file, clear_file
from utilities.books.constants import *


class DemoSpider(scrapy.Spider):
    name = 'demo'

    def start_requests(self):
        # Get book-list from gist
        yield Request(
            url=BOOK_LIST_GIST,
            callback=self.parse
        )

    def parse(self, response: Response):
        raw_url = response.xpath(RAW_GIST_PATH).get()

        # Get book_list.json from gist
        yield Request(
            url=response.urljoin(raw_url),
            callback=self.parse_book_list
        )

    def parse_book_list(self, response: scrapy.http.response.Response):
        book_list = json.loads(response.body, encoding='utf-8')

        if book_list:
            for book in book_list:
                yield Request(
                    url=BASE_URL.format(book[SHORT_NAME]),
                    callback=self.parse_book_info,
                    cb_kwargs=dict(short_name=book[SHORT_NAME])
                )

    def parse_book_info(self, response: Response, short_name):
        # Get book's full name and author
        loader = ItemLoader(item=BookInfo(), response=response)
        # Find elements
        loader.add_css(FULL_NAME, BOOK_FULL_NAME_PATH)
        loader.add_css(AUTHOR, BOOK_AUTHOR_PATH)

        # Extracting data
        page = loader.load_item()
        full_name = page.get(FULL_NAME)
        author = page.get(AUTHOR)

        # Initial file to write
        clear_file(short_name)
        file = append_file(short_name)
        # Write file header with book name and author
        file.write(BOOK_HEADER.format(full_name, author))
        # print(full_name, author)

        yield Request(
            url=FIRST_CHAPTER_URL.format(short_name),
            callback=self.parse_chapter,
            cb_kwargs=dict(file=file)
        )

    def parse_chapter(self, response: Response, file):
        # Get chapter data using ItemLoader
        loader = ItemLoader(item=Chapter(), response=response)
        # Find elements
        loader.add_xpath(TITLE_INDEX, TITLE_INDEX_PATH)
        loader.add_css(TITLE_CONTENT, TITLE_CONTENT_PATH)
        loader.add_css(CONTENT, CONTENT_PATH)
        loader.add_xpath(NEXT_CHAPTER, NEXT_CHAPTER_PATH)

        # Extracting data
        page = loader.load_item()
        next_chapter = page.get(NEXT_CHAPTER)

        # Write title and content for each chapter
        file.write(EPISODE_HEADER.format(page.get(TITLE_INDEX), page.get(TITLE_CONTENT)))
        file.write(page.get(CONTENT))

        # Crawling next chapter
        if next_chapter:
            next_chapter_url = response.urljoin(next_chapter)
            yield Request(
                url=next_chapter_url,
                callback=self.parse_chapter,
                cb_kwargs=dict(file=file)
            )
        else:
            file.close()
