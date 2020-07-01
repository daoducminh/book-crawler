from book_lists import book_list_yy, book_list_ttv, book_list_tfull, book_list_tcv
from os import getenv
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
MONGODB_URI = getenv('MONGODB_URI')


def get_top_book_list(name):
    client = MongoClient(MONGODB_URI)
    db = client[name]
    return db.list_collection_names()


def select_source(x):
    return {
        'yy': book_list_yy.book_list,
        'ttv': book_list_ttv.book_list,
        'tcv': book_list_tcv.book_list,
        'tfull': book_list_tfull.book_list,
        'fullyy': get_top_book_list('fullyy')
    }[x]
