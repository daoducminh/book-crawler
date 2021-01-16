# -*- coding: utf-8 -*-

from os import system, listdir

AZW3 = 'azw3'
EPUB = 'epub'
NO_INLINE_TOC = '--no-inline-toc'
CONVERT_CMD = 'tsp ./convert.sh {0} {1} {2} {3}'
BOOK_DIR = 'books/{}'


def convert_ebook(book_list):
    for book in book_list:
        files = set([
            file[:-5]
            for file in listdir(BOOK_DIR.format(book)) if book in file
        ])
        for file_name in sorted(files):
            system(CONVERT_CMD.format(book, file_name, AZW3, NO_INLINE_TOC))
            system(CONVERT_CMD.format(book, file_name, EPUB, ''))
