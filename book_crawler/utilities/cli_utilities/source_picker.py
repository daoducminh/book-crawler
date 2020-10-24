# -*- coding: utf-8 -*-

from dotenv import load_dotenv

from book_lists import book_list_yy, book_list_ttv, book_list_tfull, book_list_tcv, book_list_tct

load_dotenv(dotenv_path='.env')


def select_source(x):
    return {
        'yy': book_list_yy.book_list,
        'ttv': book_list_ttv.book_list,
        'tcv': book_list_tcv.book_list,
        'tfull': book_list_tfull.book_list,
        'tct': book_list_tct.book_list
        # 'fullyy': get_top_book_list('fullyy')
    }[x]
