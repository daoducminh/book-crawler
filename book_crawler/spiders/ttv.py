# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.http.response import Response
from scrapy.loader import ItemLoader

from book_crawler.utilities.constants.common_constants import *
from book_crawler.utilities.constants.ttv_constants import *
from book_crawler.utilities.items.ttv_book_items import Chapter, BookInfo
from book_lists.book_list_ttv import book_list


class TtvSpider(Spider):
    name = 'ttv'
    custom_settings = {
        'ITEM_PIPELINES': {
            'book_crawler.pipelines.MongoPipeline': 1,
        },
        'LOG_ENABLED': False,
        'DEFAULT_REQUEST_HEADERS': {
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'content-type': 'text/html; charset=UTF-8',
            'connection': 'keep-alive',
            'upgrade-insecure-requests': 1,
            'accept-encoding': 'gzip, deflate, br'
        },
        'RETRY_TIMES': 50
    }

    def start_requests(self):
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
        loader.add_xpath(FULL_NAME, BOOK_FULL_NAME_PATH)
        loader.add_xpath(AUTHOR, BOOK_AUTHOR_PATH)
        loader.add_css(LAST_CHAPTER, BOOK_LAST_CHAPTER_PATH)

        # Extracting data
        page = loader.load_item()
        last_chapter = int(page.get(LAST_CHAPTER))

        yield {
            SHORT_NAME: short_name,
            FULL_NAME: page.get(FULL_NAME),
            AUTHOR: page.get(AUTHOR),
            LAST_CHAPTER: last_chapter
        }

        for i in range(1, last_chapter + 1):
            yield Request(
                url=CHAPTER_URL.format(short_name, i),
                callback=self.parse_chapter,
                cb_kwargs=dict(short_name=short_name, chapter_index=i)
            )

    def parse_chapter(self, response: Response, short_name, chapter_index):
        # Get chapter data using ItemLoader
        loader = ItemLoader(item=Chapter(), response=response)
        # Find elements
        loader.add_css(TITLE_CONTENT, TITLE_CONTENT_PATH)
        loader.add_xpath(CONTENT, CONTENT_PATH)

        # Extracting data
        page = loader.load_item()
        content = page.get(CONTENT)
        if content:
            yield {
                SHORT_NAME: short_name,
                TITLE_INDEX: chapter_index,
                TITLE_CONTENT: page.get(TITLE_CONTENT),
                CONTENT: content
            }
