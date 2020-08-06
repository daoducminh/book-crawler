from os import system, getenv
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
VPS = getenv('VPS')
PRIVATE_KEY = getenv('PRIVATE_KEY')
DOWNLOAD_BOOKS_COMMAND = 'scp -i {2} {1}:~/book-crawler/books/{0}.* ./books'
UPLOAD_BOOK_LIST_COMMAND = 'scp -i {2} ./book_lists/book_list_{0}.py {1}:~/book-crawler/book_lists'


def download_books(book_list):
    for book in book_list:
        system(DOWNLOAD_BOOKS_COMMAND.format(book, VPS, PRIVATE_KEY))


def upload_book_list(book_source):
    system(UPLOAD_BOOK_LIST_COMMAND.format(book_source, VPS, PRIVATE_KEY))
