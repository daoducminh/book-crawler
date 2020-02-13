# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from scrapy.http.response import Response
from scrapy.loader import ItemLoader

from book_list import book_list
from utilities.books.constants import *
from utilities.items.book_items import Chapter, BookInfo


class DemoSpider(scrapy.Spider):
    name = 'demo'

    custom_settings = {
        'ITEM_PIPELINES': {
            'book_crawler.pipelines.MongoPipeline': 1,
        }
    }

    def start_requests(self):
        yield Request(
            url=BOOK_LIST_URL,
            callback=self.parse_book_list
        )

    def parse_book_list(self, response: Response):
        book_list = json.loads(response.text)

        if book_list:
            for book in book_list:
                yield Request(
                    url=BASE_URL.format(book),
                    callback=self.parse_book_info,
                    cb_kwargs=dict(short_name=book)
                )

    def parse_book_info(self, response: Response, short_name):
        # Get book's full name and author
        loader = ItemLoader(item=BookInfo(), response=response)
        # Find elements
        loader.add_css(FULL_NAME, BOOK_FULL_NAME_PATH)
        loader.add_css(AUTHOR, BOOK_AUTHOR_PATH)
        loader.add_xpath(LAST_CHAPTER, BOOK_LAST_CHAPTER_PATH)

        # Extracting data
        page = loader.load_item()
        full_name = page.get(FULL_NAME)
        author = page.get(AUTHOR)
        last_chapter = int(page.get(LAST_CHAPTER))

        for i in range(last_chapter, -1, -1):
            if i == 0:
                yield {
                    SHORT_NAME: short_name,
                    FULL_NAME: full_name,
                    AUTHOR: author,
                    LAST_CHAPTER: last_chapter
                }
            else:
                yield Request(
                    url=CHAPTER_URL.format(short_name, i),
                    callback=self.parse_chapter,
                    cb_kwargs=dict(short_name=short_name)
                )

    def parse_chapter(self, response: Response, short_name):
        # Get chapter data using ItemLoader
        loader = ItemLoader(item=Chapter(), response=response)
        # Find elements
        loader.add_xpath(TITLE_INDEX, TITLE_INDEX_PATH)
        loader.add_css(TITLE_CONTENT, TITLE_CONTENT_PATH)
        loader.add_css(CONTENT, CONTENT_PATH)

        # Extracting data
        page = loader.load_item()

        yield {
            SHORT_NAME: short_name,
            TITLE_INDEX: int(page.get(TITLE_INDEX)),
            TITLE_CONTENT: page.get(TITLE_CONTENT),
            CONTENT: page.get(CONTENT)
        }
