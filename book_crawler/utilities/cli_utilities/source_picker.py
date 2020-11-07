# -*- coding: utf-8 -*-
# from book_lists import book_list_yy, book_list_ttv, book_list_tfull, book_list_tcv, book_list_tct

# def select_source(x):
#     return {
#         'yy': book_list_yy.book_list,
#         'ttv': book_list_ttv.book_list,
#         'tcv': book_list_tcv.book_list,
#         'tfull': book_list_tfull.book_list,
#         'tct': book_list_tct.book_list
#         # 'fullyy': get_top_book_list('fullyy')
#     }[x]


def select_source(x):
    if x == 'yy':
        from book_lists.book_list_yy import book_list
        return book_list
    elif x == 'ttv':
        from book_lists.book_list_ttv import book_list
        return book_list
    elif x == 'tcv':
        from book_lists.book_list_tcv import book_list
        return book_list
    elif x == 'tct':
        from book_lists.book_list_tct import book_list
        return book_list
    elif x == 'tfull':
        from book_lists.book_list_tfull import book_list
        return book_list
    elif x == 'mtc':
        from book_lists.book_list_mtc import book_list
        return book_list
    # elif x == '':
    #     from book_lists.book_list_ import book_list
    #     return book_list
    else:
        return None
