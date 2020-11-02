# -*- coding: utf-8 -*-

import re


def reformat_chapter_content(text):
    # Remove whitespace at start and end
    temp = text.strip()
    # Split paragraph into sentences
    arr = temp.split('\n')
    # Remove start and end whitespaces of each sentences
    map(str.strip, arr)
    for i in range(len(arr)):
        arr[i] = arr[i].replace('\n', ' ')
        arr[i] = re.sub(r'\s{2,}', ' ', arr[i])
        arr[i] = arr[i].strip()
        if not arr[i]:
            del arr[i]
    return arr


def get_last_chapter(text):
    return re.findall(r'\d+', text)[0]
