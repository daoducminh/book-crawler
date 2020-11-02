# -*- coding: utf-8 -*-

import re


def get_title_content(text: str):
    text = text.replace(':', '')
    text = re.sub('[Cc]hương *\\d*', '', text)
    return text.strip()


def remove_text_from_paragraph(text, paragraph):
    return re.sub(text, '', paragraph)


def convert_line_break(text: str):
    return re.sub(r'(<br\/?>|<\/?p>)', '\n', text)
