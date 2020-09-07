from scrapy import Item, Field
from itemloaders.processors import Join, MapCompose
from w3lib.html import remove_tags

from book_crawler.utilities.chapter_utilities.common_chapter_utilities import get_title_content
from book_crawler.utilities.chapter_utilities.tct_utilities import reformat_chapter_content, get_title_index, get_last_chapter


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
