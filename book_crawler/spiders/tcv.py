# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.http.response import Response
from scrapy.loader import ItemLoader

from book_list import book_list
from utilities.books.constants import *
from utilities.books.tcv_constants import *
from utilities.items.book_items import TcvChapter, TcvBookInfo


class TcvSpider(Spider):
    name = 'tcv'

    custom_settings = {
        'ITEM_PIPELINES': {
            'book_crawler.pipelines.MongoPipeline': 1,
        },
        'LOG_ENABLED': False,
        'DEFAULT_REQUEST_HEADERS': {
            'accept': '*/*'
        }
    }

    def parse(self, response):
        pass
