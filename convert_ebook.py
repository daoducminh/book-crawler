from os import system
import sys
import re
from book_lists.source_picker import select_source

FILENAME = '{}.html'
# Ebook convert commands
HTML_AZW3 = 'tsp ebook-convert books/{0}.html books/{0}.azw3 --level1-toc "//h:h1" --no-inline-toc'


def convert(book_list):
    for book in book_list:
        # Convert HTML file to AZW3 file
        system(HTML_AZW3.format(book))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        book_source = sys.argv[1]
        book_list = select_source(book_source)
        if book_list:
            convert(book_list)
        else:
            print('Invalid book source.')
    else:
        print('Invalid arguments')
