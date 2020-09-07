import re
from book_crawler.utilities.chapter_utilities.common_chapter_utilities import remove_text_from_paragraph


def reformat_chapter_content(text):
    # Remove whitespace at start and end
    temp = text.strip()
    # Split paragraph into sentences
    arr = temp.split('\n')
    # Remove start and end whitespaces of each sentences
    map(str.strip, arr)
    return arr


def get_last_chapter(text):
    return re.findall(r'\d+', text)[0]