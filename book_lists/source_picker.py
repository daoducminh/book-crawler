from book_lists import book_list_yy, book_list_ttv, book_list_tfull, book_list_tcv


def select_source(x):
    return{
        'yy': book_list_yy.book_list,
        'ttv': book_list_ttv.book_list,
        'tcv': book_list_tcv.book_list,
        'tfull': book_list_tfull.book_list
    }[x]
