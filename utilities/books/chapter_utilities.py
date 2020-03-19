import codecs
import re

from utilities.books.constants import BOOK_HEADER, FILE_NAME, ADS_PATTERN


def get_title_index(text: str):
    return text.split(' ')[-1]


def get_title_content(text: str):
    text = text.replace(':', '')
    text = re.sub('[Cc]hương *\\d*', '', text)
    return text.strip()


def print_book_header(file, book_name):
    file.write(BOOK_HEADER.format(book_name))


def write_file(short_name):
    return codecs.open(FILE_NAME.format(short_name), 'w', 'utf-8')


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
    # Remove credit and ads
    arr[0] = remove_text_from_paragraph('Người đăng:.+', arr[0])
    if arr[0] == '':
        del arr[0]
    return arr


def get_last_chapter(text):
    return re.split('[.\\-]', text)[-2]
