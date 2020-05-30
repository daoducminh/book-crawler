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
            'accept': '*/*',
            # 'cookie': '__cfduid=de95d4341c7c8c6c5257bfa579a5e5e271584092018; csrftoken=otEAQgiYz4p4nHqJQX3da35G9iGEUed9hJ7VEMBK0FBN7ShBTKwiGvgi0eqdVbZy; truyenyy_sessionid=4n4h9crk9r8mg5xu6gmg2mvgkx6ptmff',
        }
    }

    def parse(self, response):
        pass
