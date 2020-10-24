# -*- coding: utf-8 -*-

# URLs
BASE_URL = 'https://truyen.tangthuvien.vn/doc-truyen/{}'
CHAPTER_URL = 'https://truyen.tangthuvien.vn/doc-truyen/{}/chuong-{}'

# Book's info
BOOK_FULL_NAME_PATH = "//a[@data-eid='qd_G03']"
BOOK_AUTHOR_PATH = "//a[contains(@href,'tac-gia') and @target='_blank' and not(@data-eid)]"
BOOK_LAST_CHAPTER_PATH = '#j-bookCatalogPage'

# Chapter's content
TITLE_CONTENT_PATH = 'h2'
CONTENT_PATH = "//div[contains(@class,'box-chap') and not(contains(@class,'hidden'))]"
