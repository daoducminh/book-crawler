import sys
from book_lists.source_picker import select_source
from utilities.cli_utilities.create_html_ebook import create_html_ebook
from utilities.cli_utilities.convert_ebook import convert_ebook
from utilities.cli_utilities.transfer_books import upload_book_list, download_books

OPTION_LIST = ['create', 'convert', 'download', 'upload']

if __name__ == "__main__":
    if len(sys.argv) == 3:
        option = sys.argv[1]
        book_source = sys.argv[2]
        book_list = select_source(book_source)
        if option in OPTION_LIST:
            if book_list:
                if option == 'create':
                    create_html_ebook(option, book_list)
                if option == 'convert':
                    convert_ebook(book_list)
                if option == 'download':
                    download_books(book_list)
                if option == 'upload':
                    upload_book_list(book_source)
            else:
                print('Invalid book source.')
        else:
            print('Invalid option')
    else:
        print('Invalid arguments')
