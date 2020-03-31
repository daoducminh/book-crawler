import re


def get_title_index(text: str):
    return text.split(' ')[-1]


def get_title_content(text: str):
    text = text.replace(':', '')
    text = re.sub('[Cc]hương *\\d*', '', text)
    return text.strip()


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


def reformat_ttv_chapter_content(text):
    # Remove whitespace at start and end
    temp = re.sub('(\r|\t)', '', text)
    # Split paragraph into sentences
    arr = re.split(r'\n+ *', temp)
    # Remove start and end whitespaces of each sentences
    map(str.strip, arr)
    arr = list(filter(None, arr))
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


def get_ttv_last_chapter(text):
    return re.findall(r'\d+', text)[0]
