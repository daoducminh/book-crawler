# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import remove_tags

from book_crawler.utilities.books.chapter_utilities import *


class Chapter(scrapy.Item):
    title_index = scrapy.Field(
        input_processor=MapCompose(remove_tags, get_title_index),
        output_processor=Join()
    )
    title_content = scrapy.Field(
        input_processor=MapCompose(remove_tags, get_title_content),
        output_processor=Join()
    )
    content = scrapy.Field(
        input_processor=MapCompose(remove_tags, reformat_chapter_content),
        output_processor=Join('\n\n')
    )
    next_chapter = scrapy.Field()
