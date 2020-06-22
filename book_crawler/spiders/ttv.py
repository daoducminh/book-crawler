# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.http.response import Response
from scrapy.loader import ItemLoader

from book_list_2 import book_list
from utilities.books.constants import *
from utilities.books.ttv_constants import *
from utilities.items.book_items import TtvChapter, TtvBookInfo


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
        loader = ItemLoader(item=TtvBookInfo(), response=response)
        # Find elements
        loader.add_xpath(FULL_NAME, BOOK_FULL_NAME_PATH)
        loader.add_xpath(AUTHOR, BOOK_AUTHOR_PATH)
        loader.add_css(LAST_CHAPTER, BOOK_LAST_CHAPTER_PATH)

        # Extracting data
        page = loader.load_item()
        full_name = page.get(FULL_NAME)
        author = page.get(AUTHOR)
        last_chapter = int(page.get(LAST_CHAPTER))

        for i in range(last_chapter, -1, -1):
            if i != 0:
                yield Request(
                    url=CHAPTER_URL.format(short_name, i),
                    callback=self.parse_chapter,
                    cb_kwargs=dict(short_name=short_name, title_index=i)
                )
            else:
                yield {
                    SHORT_NAME: short_name,
                    FULL_NAME: full_name,
                    AUTHOR: author,
                    LAST_CHAPTER: last_chapter
                }

    def parse_chapter(self, response: Response, short_name, title_index):
        # Get chapter data using ItemLoader
        loader = ItemLoader(item=TtvChapter(), response=response)
        # Find elements
        loader.add_css(TITLE_CONTENT, TITLE_CONTENT_PATH)
        loader.add_xpath(CONTENT, CONTENT_PATH)

        # Extracting data
        page = loader.load_item()
        content = page.get(CONTENT)
        if content:
            yield {
                SHORT_NAME: short_name,
                TITLE_INDEX: title_index,
                TITLE_CONTENT: page.get(TITLE_CONTENT),
                CONTENT: content
            }
