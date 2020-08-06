from os import system
import sys
import re

HTML_AZW3 = 'tsp ./convert.sh {0}'


def convert_ebook(book_list):
    for book in book_list:
        # Convert HTML file to AZW3 file
        system(HTML_AZW3.format(book))
