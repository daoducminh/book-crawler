import re
from book_crawler.utilities.chapter_utilities.common_chapter_utilities import remove_text_from_paragraph


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


def get_title_index(text: str):
    text = text.split(':')[0]
    return text.split(' ')[1]


def get_last_chapter(text: str):
    return text.split(' ')[0]
