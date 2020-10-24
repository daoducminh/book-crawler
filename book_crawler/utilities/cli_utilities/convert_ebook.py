# -*- coding: utf-8 -*-

from os import system, listdir

CONVERT_CMD = 'tsp ./convert.sh {0} {1} {2}'
AZW3 = 'azw3'
EPUB = 'epub'
NO_INLINE_TOC = '--no-inline-toc'


def convert_ebook(book_list):
    for file in listdir('books/'):
        for book in book_list:
            if book in file:
                file_name = file[:-5]
                system(CONVERT_CMD.format(file_name, AZW3, NO_INLINE_TOC))
                system(CONVERT_CMD.format(file_name, EPUB, ''))
