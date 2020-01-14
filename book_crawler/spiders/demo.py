# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from book_crawler.items import Chapter
from utilities.books.book_list import BOOK_LIST
from utilities.books.chapter_utilities import append_file, clear_file
from utilities.books.constants import *

file_list = {}


class DemoSpider(scrapy.Spider):
    name = 'demo'

    def start_requests(self):
        for book in BOOK_LIST:
            # Init file to write
            clear_file(book[SHORT_NAME])
            file = append_file(book[SHORT_NAME])
            # Add file writer to list
            file_list[book[SHORT_NAME]] = file
            # Write file header with book name and author
            file.write(BOOK_HEADER.format(book[FULL_NAME], book[AUTHOR]))

            yield scrapy.Request(
                url=BASE_URL.format(book[SHORT_NAME]),
                callback=self.parse,
                meta={SHORT_NAME: book[SHORT_NAME]}
            )

    def parse(self, response: scrapy.http.response.Response):
        # Get file write from list
        short_name = response.meta[SHORT_NAME]
        file = file_list[short_name]

        # Get chapter data using ItemLoader
        loader = ItemLoader(item=Chapter(), response=response)
        loader.add_xpath(TITLE_INDEX, TITLE_INDEX_PATH)
        loader.add_css(TITLE_CONTENT, TITLE_CONTENT_PATH)
        loader.add_css(CONTENT, CONTENT_PATH)
        loader.add_xpath(NEXT_CHAPTER, NEXT_CHAPTER_PATH)

        # Extracting data
        page = loader.load_item()
        next_chapter = page.get(NEXT_CHAPTER)[0]

        # Write title and content for each chapter
        file.write(EPISODE_HEADER.format(page.get(TITLE_INDEX), page.get(TITLE_CONTENT)))
        file.write(page.get(CONTENT))

        # Crawling next chapter
        if next_chapter:
            next_chapter_url = response.urljoin(next_chapter)
            yield scrapy.Request(
                url=next_chapter_url,
                callback=self.parse,
                meta={SHORT_NAME: short_name}
            )

    @staticmethod
    def close(spider, reason):
        for file in file_list.values():
            file.close()
        return super().close(spider, reason)
