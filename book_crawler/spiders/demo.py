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
        }
    }

    def start_requests(self):
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
        last_chapter = page.get(LAST_CHAPTER)

        # return
        # Initial file to write
        # file = write_file(short_name)
        # Write file header with book name and author
        # file.write(BOOK_HEADER.format(full_name, author))
        # print(full_name, author)
        for i in range(1, 200):
            yield Request(
                url=CHAPTER_URL.format(short_name, i),
                callback=self.parse_chapter,
                # cb_kwargs=dict(file=file)
                cb_kwargs=dict(short_name=short_name)
            )

    def parse_chapter(self, response: Response, short_name):
        # Get chapter data using ItemLoader
        loader = ItemLoader(item=Chapter(), response=response)
        # Find elements
        loader.add_xpath(TITLE_INDEX, TITLE_INDEX_PATH)
        loader.add_css(TITLE_CONTENT, TITLE_CONTENT_PATH)
        loader.add_css(CONTENT, CONTENT_PATH)
        loader.add_xpath(NEXT_CHAPTER, NEXT_CHAPTER_PATH)

        # Extracting data
        page = loader.load_item()
        next_chapter = page.get(NEXT_CHAPTER)

        yield {
            SHORT_NAME: short_name,
            TITLE_INDEX: int(page.get(TITLE_INDEX)),
            TITLE_CONTENT: page.get(TITLE_CONTENT),
            CONTENT: page.get(CONTENT)
        }
        # Write title and content for each chapter
        # file.write(EPISODE_HEADER.format(page.get(TITLE_INDEX), page.get(TITLE_CONTENT)))
        # file.write(page.get(CONTENT))
        # index += 1
        # # Crawling next chapter
        # if next_chapter and index < 10:
        #     next_chapter_url = response.urljoin(next_chapter)
        #     yield Request(
        #         url=next_chapter_url,
        #         callback=self.parse_chapter,
        #         # cb_kwargs=dict(file=file)
        #         cb_kwargs=dict(short_name=short_name, index=index)
        #     )
        # else:
        #     pass
        #     file.close()
