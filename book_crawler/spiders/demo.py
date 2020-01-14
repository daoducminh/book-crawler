# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.loader import ItemLoader

from book_crawler.items import Chapter
from utilities.books.chapter_utilities import append_file, clear_file
from utilities.books.constants import *


class DemoSpider(scrapy.Spider):
    name = 'demo'

    def start_requests(self):
        # Get book-list from gist
        yield scrapy.Request(
            url=BOOK_LIST_GIST,
            callback=self.parse
        )

    def parse(self, response):
        raw_url = response.xpath(RAW_GIST_PATH).get()

        # Get book_list.json from gist
        yield scrapy.Request(
            url=response.urljoin(raw_url),
            callback=self.parse_book_list
        )

    def parse_book_list(self, response):
        book_list = json.loads(response.body, encoding='utf-8')

        if book_list:
            for book in book_list:
                # Init file to write
                clear_file(book[SHORT_NAME])
                file = append_file(book[SHORT_NAME])
                # Write file header with book name and author
                file.write(BOOK_HEADER.format(book[FULL_NAME], book[AUTHOR]))

                yield scrapy.Request(
                    url=BASE_URL.format(book[SHORT_NAME]),
                    callback=self.parse_chapter,
                    cb_kwargs=dict(file=file)
                )

    def parse_chapter(self, response, file):
        # Get chapter data using ItemLoader
        loader = ItemLoader(item=Chapter(), response=response)
        loader.add_xpath(TITLE_INDEX, TITLE_INDEX_PATH)
        loader.add_css(TITLE_CONTENT, TITLE_CONTENT_PATH)
        loader.add_css(CONTENT, CONTENT_PATH)
        loader.add_xpath(NEXT_CHAPTER, NEXT_CHAPTER_PATH)

        # Extracting data
        page = loader.load_item()
        next_chapter = page.get(NEXT_CHAPTER)[0]

        # Write title and content for each chapter
        file.write(EPISODE_HEADER.format(page.get(TITLE_INDEX), page.get(TITLE_CONTENT)))
        file.write(page.get(CONTENT))

        # Crawling next chapter
        if next_chapter:
            next_chapter_url = response.urljoin(next_chapter)
            yield scrapy.Request(
                url=next_chapter_url,
                callback=self.parse_chapter,
                cb_kwargs=dict(file=file)
            )
        else:
            file.close()
