from os import system
import re
from book_list import book_list

FILENAME = '{}.html'
# Ebook convert commands
HTML_AZW3 = 'tsp ebook-convert books/{0}.html books/{0}.azw3 --level1-toc "//h:h2" --no-inline-toc'


def main():
    system('cd books/')
    for book in book_list:
        # Convert HTML file to AZW3 file
        system(HTML_AZW3.format(book))


if __name__ == '__main__':
    main()
