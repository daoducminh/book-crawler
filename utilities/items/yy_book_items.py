from scrapy import Item, Field
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import remove_tags

from utilities.chapter_utilities.common_chapter_utilities import get_title_content, get_title_index
from utilities.chapter_utilities.yy_utilities import *


class Chapter(Item):
    title_content = Field(
        input_processor=MapCompose(remove_tags, get_title_content),
        output_processor=Join()
    )
    content = Field(
        input_processor=MapCompose(remove_tags, reformat_chapter_content),
        output_processor=Join('\n\n')
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
    last_chapter = Field(
        input_processor=MapCompose(get_last_chapter),
        output_processor=Join()
    )
