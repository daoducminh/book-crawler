from os import system
import sys
import re

HTML_AZW3 = 'tsp ebook-convert books/{0}.html books/{0}.azw3 --level1-toc "//h:h1" --no-inline-toc'


def convert_ebook(book_list):
    for book in book_list:
        # Convert HTML file to AZW3 file
        system(HTML_AZW3.format(book))
