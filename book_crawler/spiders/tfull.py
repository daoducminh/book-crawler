# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.http.response import Response
from scrapy.loader import ItemLoader

from book_crawler.utilities.constants.common_constants import *
from book_crawler.utilities.constants.tfull_constants import *
from book_crawler.utilities.items.tfull_book_items import Chapter, BookInfo
from book_lists.book_list_tfull import book_list

MAX_TRY = 1


class TfullSpider(Spider):
    name = 'tfull'
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
                callback=self.parse_chapter_list,
                cb_kwargs=dict(book=book)
            )

    def parse_chapter_list(self, response: Response, book):
        total_page = response.xpath('//input[@id="total-page"]/@value').get()
        if total_page:
            yield Request(
                url=LAST_CHAPTER_PAGE.format(book, total_page),
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
        last_chapter = page.get(LAST_CHAPTER)
        try:
            last_chapter = int(last_chapter)
        except:
            last_chapter = int(last_chapter.split(' ')[-1])

        yield {
            SHORT_NAME: short_name,
            FULL_NAME: page.get(FULL_NAME),
            AUTHOR: page.get(AUTHOR),
            LAST_CHAPTER: last_chapter
        }

        for i in range(1, last_chapter + 1):
            chapter_url = CHAPTER_URL.format(short_name, i)
            yield Request(
                url=chapter_url,
                callback=self.parse_chapter,
                cb_kwargs=dict(
                    short_name=short_name,
                    chapter_index=i,
                    chapter_url=chapter_url,
                    count=0
                ),
                dont_filter=True
            )

    def parse_chapter(self, response: Response, short_name, chapter_index, chapter_url, count):
        if count <= MAX_TRY:
            count = count + 1
            if chapter_url != response.request.url:
                chapter_url = CHAPTER_URL.format(
                    short_name, f'{"0"*count}{chapter_index}'
                )
                yield Request(
                    url=chapter_url,
                    callback=self.parse_chapter,
                    cb_kwargs=dict(
                        short_name=short_name,
                        chapter_index=chapter_index,
                        chapter_url=chapter_url,
                        count=count
                    ),
                    dont_filter=True
                )
            else:
                # Get chapter data using ItemLoader
                loader = ItemLoader(item=Chapter(), response=response)
                # Find elements
                loader.add_css(TITLE_CONTENT, TITLE_CONTENT_PATH)
                loader.add_css(CONTENT, CONTENT_PATH)

                page = loader.load_item()
                content = page.get(CONTENT)
                if content:
                    yield {
                        SHORT_NAME: short_name,
                        TITLE_INDEX: chapter_index,
                        TITLE_CONTENT: page.get(TITLE_CONTENT),
                        CONTENT: content
                    }
