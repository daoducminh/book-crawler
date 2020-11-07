# -*- coding: utf-8 -*-

import re

from book_crawler.utilities.chapter_utilities.common_chapter_utilities import remove_text_from_paragraph


def reformat_chapter_content(text):
    # Remove whitespace at start and end
    temp = text.strip()
    # Split paragraph into sentences
    arr = temp.split('\n\n')
    # Remove start and end whitespaces of each sentences
    map(str.strip, arr)
    for i in range(len(arr)):
        arr[i] = arr[i].replace('\n', ' ')
        arr[i] = re.sub(r'\s{2,}', ' ', arr[i])
        arr[i] = arr[i].strip()
    return [l for l in arr if l]
