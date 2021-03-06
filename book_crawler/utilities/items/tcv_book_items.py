# -*- coding: utf-8 -*-

from itemloaders.processors import Join, MapCompose
from scrapy import Item, Field
from w3lib.html import remove_tags

from book_crawler.utilities.chapter_utilities.common_chapter_utilities import *
from book_crawler.utilities.chapter_utilities.tcv_utilities import *


class BookInfo(Item):
    full_name = Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join()
    )
    author = Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Join()
    )
    last_chapter = Field(
        input_processor=MapCompose(remove_tags, get_last_chapter),
        output_processor=Join()
    )


class Chapter(Item):
    title_content = Field(
        input_processor=MapCompose(remove_tags, get_title_content),
        output_processor=Join()
    )
    content = Field(
        input_processor=MapCompose(
            convert_line_break,
            remove_tags,
            reformat_chapter_content
        ),
        output_processor=Join('\n\n')
    )
