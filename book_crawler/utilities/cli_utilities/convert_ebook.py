# -*- coding: utf-8 -*-

from os import system, listdir

AZW3 = 'azw3'
EPUB = 'epub'
NO_INLINE_TOC = '--no-inline-toc'
CONVERT_CMD = 'tsp ebook-convert books/{0}/{1}.html books/{0}/{1}.{2} --level1-toc "//h:h1" {3}'
BOOK_DIR = 'books/{}'


def convert_ebook(book_list):
    for book in book_list:
        for file in listdir(BOOK_DIR.format(book)):
            if book in file:
                file_name = file[:-5]
                system(CONVERT_CMD.format(book, file_name, AZW3, NO_INLINE_TOC))
                system(CONVERT_CMD.format(book, file_name, EPUB, ''))
