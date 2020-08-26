from os import system
import sys
import re

CONVERT_CMD = 'tsp ./convert.sh {0} {1}'
AZW3 = 'azw3'
EPUB = 'epub'


def convert_ebook(book_list):
    for book in book_list:
        system(CONVERT_CMD.format(book, AZW3))
        system(CONVERT_CMD.format(book, EPUB))
