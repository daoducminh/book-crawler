import codecs
import re

from utilities.books.constants import BOOK_HEADER, FILE_NAME


def get_title_index(text):
    return text.split(' ')[-1]


def get_title_content(text):
    return re.split('[:?]', text)[-1].strip()


def print_book_header(file, book_name):
    file.write(BOOK_HEADER.format(book_name))


def write_file(short_name, book_index):
    return codecs.open(FILE_NAME.format(short_name, book_index), 'w', 'utf-8')


def remove_text_from_paragraph(text, paragraph):
    return re.sub(text, '', paragraph)


def reformat_chapter_content(text):
    # Remove whitespace at start and end
    temp = text.strip()
    # Split paragraph into sentences
    arr = temp.split('\n')
    # Remove start and end whitespaces of each sentences
    map(str.strip, arr)
    # Remove redeclare title
    if re.search('Chương [0-9]+ *::', arr[0]):
        arr = arr[1:]
    # Remove credit
    arr[0] = remove_text_from_paragraph('Người đăng:.+', arr[0])
    if arr[0] == '':
        del arr[0]
    return arr

