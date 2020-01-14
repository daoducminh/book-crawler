# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import remove_tags

from utilities.books.chapter_utilities import get_title_content, get_title_index, reformat_chapter_content


class Chapter(Item):
    title_index = Field(
        input_processor=MapCompose(remove_tags, get_title_index),
        output_processor=Join()
    )
    title_content = Field(
        input_processor=MapCompose(remove_tags, get_title_content),
        output_processor=Join()
    )
    content = Field(
        input_processor=MapCompose(remove_tags, reformat_chapter_content),
        output_processor=Join('\n\n')
    )
    next_chapter = Field(
        output_processor=Join()
    )


class BookInfo(Item):
    full_name = Field(
        input_processor=MapCompose(str.strip),
        output_processor=Join()
    )
    author = Field(
        input_processor=MapCompose(str.strip),
        output_processor=Join()
    )
