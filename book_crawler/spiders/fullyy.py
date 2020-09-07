from os import getenv
from scrapy import Request
from scrapy.http.response import Response
from scrapy.loader import ItemLoader
from dotenv import load_dotenv

from book_crawler.utilities.constants.yy_constants import TOP_BOOK_URLS, TOP_FULL_BOOK_URL, BASE_URL
from book_crawler.spiders.yy import YYSpider

load_dotenv(dotenv_path='.env')
COOKIE = getenv('YY_COOKIE')
MAX_PAGE_NUMBER = 6


class FullYYSpider(YYSpider):
    name = 'fullyy'

    custom_settings = {
        'ITEM_PIPELINES': {
            'book_crawler.pipelines.BookListPipeline': 200,
            'book_crawler.pipelines.MongoPipeline': 100,
        },
        'LOG_ENABLED': False,
        'DEFAULT_REQUEST_HEADERS': {
            'accept': '*/*',
            # 'cookie': COOKIE,
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
    }

    def start_requests(self):
        for i in range(1, MAX_PAGE_NUMBER):
            yield Request(
                url=TOP_FULL_BOOK_URL.format(i),
                callback=self.parse_top_books
            )

    def parse_top_books(self, response):
        url_lists = response.xpath(TOP_BOOK_URLS)
        for url in url_lists:
            short_name = [x for x in url.get().split('/') if x][-1]
            yield Request(
                url=BASE_URL.format(short_name),
                callback=self.parse_book_info,
                cb_kwargs=dict(short_name=short_name)
            )
