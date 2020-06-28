import re


def get_title_index(text: str):
    return text.split(' ')[-1]


def get_title_content(text: str):
    text = text.replace(':', '')
    text = re.sub('[Cc]hương *\\d*', '', text)
    return text.strip()


def remove_text_from_paragraph(text, paragraph):
    return re.sub(text, '', paragraph)
