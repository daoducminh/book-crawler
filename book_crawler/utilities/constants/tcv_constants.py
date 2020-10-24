# -*- coding: utf-8 -*-

# URLs
BASE_URL = 'https://truyencv.com/{}'
CHAPTER_URL = 'https://truyencv.com/{}/chuong-{}'

# Book's info
BOOK_FULL_NAME_PATH = "h1.title > a::text"
BOOK_AUTHOR_PATH = "a.author::text"
BOOK_LAST_CHAPTER_PATH = '//div[@class="list-overview"]//a[1]/@href'

# Chapter's content
TITLE_CONTENT_PATH = '//div[@id="js-truyencv-read-content"]//h2[@class="title"]/text()'
CONTENT_PATH = "#js-truyencv-content::text"
