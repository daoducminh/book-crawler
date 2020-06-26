# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.http.response import Response
from scrapy.loader import ItemLoader

from book_lists.book_list_tcv import book_list
from utilities.constants.common_constants import *
from utilities.constants.tcv_constants import *
from utilities.items.tcv_book_items import Chapter, BookInfo


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
