# -*- coding: utf-8 -*-

# URLs
BASE_URL = 'https://truyencuatui.net/truyen/{0}.html'
PAGE_URL = 'https://truyencuatui.net/truyen/{0}.html?page={1}'

# Book's info
BOOK_FULL_NAME_PATH = 'h1.title'
BOOK_AUTHOR_PATH = '//a[contains(@href, "tac-gia")]/span[2]'
BOOK_LAST_PAGE_PATH = '.pagination li:last-child a::attr(href)'
BOOK_LAST_CHAPTER_PATH = '.stt span:nth-child(3)'

CHAPTER_URLS = '.danh-sach-chuong a::attr(href)'

# Chapter's content
TITLE_INDEX_PATH = '#b3 span'
TITLE_CONTENT_PATH = '#b3 span'
CONTENT_PATH = '.content'
