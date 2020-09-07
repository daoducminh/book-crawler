from scrapy import Request, Spider
from scrapy.http.response import Response
from scrapy.loader import ItemLoader

from book_lists.book_list_tct import book_list
from book_crawler.utilities.constants.common_constants import *
from book_crawler.utilities.constants.tct_constants import *
from book_crawler.utilities.items.tct_book_items import Chapter, BookInfo


class TctSpider(Spider):
    name = 'tct'

    custom_settings = {
        'ITEM_PIPELINES': {
            'book_crawler.pipelines.MongoPipeline': 1,
        },
        'LOG_ENABLED': False,
        'DEFAULT_REQUEST_HEADERS': {
            'accept': '*/*'
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
        loader = ItemLoader(item=BookInfo(), response=response)

        loader.add_css(FULL_NAME, BOOK_FULL_NAME_PATH)
        loader.add_xpath(AUTHOR, BOOK_AUTHOR_PATH)
        loader.add_css(LAST_CHAPTER, BOOK_LAST_CHAPTER_PATH)

        page = loader.load_item()

        yield {
            SHORT_NAME: short_name,
            FULL_NAME: page.get(FULL_NAME),
            AUTHOR: page.get(AUTHOR),
            LAST_CHAPTER: int(page.get(LAST_CHAPTER))
        }

        last_page_url = response.css(BOOK_LAST_PAGE_PATH).get()
        last_page = int(last_page_url.split('=')[1])

        for i in range(1, last_page + 1):
            yield Request(
                url=PAGE_URL.format(short_name, i),
                callback=self.parse_list_chapters,
                cb_kwargs=dict(short_name=short_name)
            )

    def parse_list_chapters(self, response, short_name):
        chapter_urls = response.css(CHAPTER_URLS).extract()

        for chapter_url in chapter_urls:
            url = response.urljoin(chapter_url)
            yield Request(
                url=url,
                callback=self.parse_chapter,
                cb_kwargs=dict(short_name=short_name)
            )

    def parse_chapter(self, response, short_name):
        loader = ItemLoader(item=Chapter(), response=response)
        # Find elements
        loader.add_css(TITLE_INDEX, TITLE_INDEX_PATH)
        loader.add_css(TITLE_CONTENT, TITLE_CONTENT_PATH)
        loader.add_css(CONTENT, CONTENT_PATH)

        # Extracting data
        page = loader.load_item()
        content = page.get(CONTENT)
        if content:
            yield {
                SHORT_NAME: short_name,
                TITLE_INDEX: int(page.get(TITLE_INDEX)),
                TITLE_CONTENT: page.get(TITLE_CONTENT),
                CONTENT: content
            }
