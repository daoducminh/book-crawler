from os import system
import sys
import re

CONVERT_CMD = 'tsp ./convert.sh {0} {1} {2}'
AZW3 = 'azw3'
EPUB = 'epub'
NO_INLINE_TOC = '--no-inline-toc'


def convert_ebook(book_list):
    for book in book_list:
        system(CONVERT_CMD.format(book, AZW3, NO_INLINE_TOC))
        system(CONVERT_CMD.format(book, EPUB, ''))
