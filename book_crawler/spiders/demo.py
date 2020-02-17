# -*- coding: utf-8 -*-
import scrapy
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
        },
        'LOG_ENABLED': True,
        'COOKIES_ENABLED': True,
        'DEFAULT_REQUEST_HEADERS': {
            'accept': 'application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'cookie': '_ga=GA1.2.465337527.1578842728; csrftoke-n=DmTnac3Gk2mG1yhZJbrIfsEoDvIYWoLtdUUiiH8ljvSqMyqjV7RHzNVI0L6LzUHp; truyenyy_sessionid=mux1i30szj759myq7dsitbv8rz6rhxqi; __cfduid=dfb4f87012c9333bb95b45e507494e06d1581581805; _gid=GA1.2.1298720373.1581907889; _gat=1',
            ':authority': 'truyenyy.com',
            ':method': 'GET',
            ':path': '/',
            ':scheme': 'https'
        }
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
        loader.add_css(FULL_NAME, BOOK_FULL_NAME_PATH)
        loader.add_css(AUTHOR, BOOK_AUTHOR_PATH)
        loader.add_xpath(LAST_CHAPTER, BOOK_LAST_CHAPTER_PATH)

        # Extracting data
        page = loader.load_item()
        full_name = page.get(FULL_NAME)
        author = page.get(AUTHOR)
        last_chapter = int(page.get(LAST_CHAPTER))

        for i in range(4, -1, -1):
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
