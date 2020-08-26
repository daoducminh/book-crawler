from os import system
import sys
import re

AZW3 = 'azw3'
EPUB = 'epub'
CONVERT_CMD = 'tsp ebook-convert books/{0}.html books/{0}.{1} --level1-toc "//h:h1" --no-inline-toc'


def convert_ebook(book_list):
    for book in book_list:
        system(CONVERT_CMD.format(book, AZW3))
        system(CONVERT_CMD.format(book, EPUB))
