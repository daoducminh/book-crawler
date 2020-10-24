# -*- coding: utf-8 -*-

from os import system

AZW3 = 'azw3'
EPUB = 'epub'
NO_INLINE_TOC = '--no-inline-toc'
CONVERT_CMD = 'tsp ebook-convert books/{0}.html books/{0}.{1} --level1-toc "//h:h1" {2}'


def convert_ebook(book_list):
    for book in book_list:
        system(CONVERT_CMD.format(book, AZW3, NO_INLINE_TOC))
        system(CONVERT_CMD.format(book, EPUB, ''))
