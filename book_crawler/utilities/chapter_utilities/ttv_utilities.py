# -*- coding: utf-8 -*-

import re

from book_crawler.utilities.chapter_utilities.common_chapter_utilities import remove_text_from_paragraph


def reformat_chapter_content(text):
    # Remove whitespace at start and end
    temp = re.sub('(\r|\t)', '', text)
    # Split paragraph into sentences
    arr = re.split(r'\n+ *', temp)
    # Remove start and end whitespaces of each sentences
    map(str.strip, arr)
    arr = list(filter(None, arr))
    # Remove redeclare title
    if re.search('Chương [0-9]+ *::', arr[0]):
        arr = arr[1:]
    # Remove credit and ads
    arr[0] = remove_text_from_paragraph('Người đăng:.+', arr[0])
    if arr[0] == '':
        del arr[0]
    return arr


def get_last_chapter(text):
    return re.findall(r'\d+', text)[0]
