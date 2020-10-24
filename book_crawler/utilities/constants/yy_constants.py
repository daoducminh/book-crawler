# -*- coding: utf-8 -*-

# URLs
BASE_URL = 'https://truyenyy.vn/truyen/{}/danh-sach-chuong?nf=yes'
CHAPTER_URL = 'https://truyenyy.vn/truyen/{0}/chuong-{1}.html'
TOP_FULL_BOOK_URL = 'https://truyenyy.vn/kim-thanh-bang/top/truyen-full/?page={}'

# Book's info
BOOK_LAST_CHAPTER_PATH = "//table[contains(@class,'table table-dark')]/tbody/tr[1]/td[1]/a/@href"
BOOK_FULL_NAME_PATH = 'h1.name::text'
BOOK_AUTHOR_PATH = 'div.author > a::text'

# Chapter's content
TITLE_CONTENT_PATH = '.chapter-title'
CONTENT_PATH = '.inner'

# Top book urls
TOP_BOOK_URLS = '//*[contains(@class, "books-list")]/li/a/@href'
# Ads pattern
# ADS_PATTERN = r'(_| _| *Bạn đang đọc truyện được lấy tại T\.r\.u\.y\.e\.n\.y\.y chấm cơm\.| *Nguồn: http://truyenyy\.vn|T\.r\.u\.y\.ệtruyenyy\.vn| *Bạn đang đọc truyện tại TruyệnFULL\.vn - http://truyenyy\.vn| *Text được lấy tại http://truyenyy\.vn| *Nguồn truyện: Truyện FULL| *Bạn đang đọc truyện được copy tại Truyện FULL| *Bạn đang đọc truyện tại Truyện FULL - www\.Truyện FULL| *Đọc Truyện Online Tại Truyện FULL| *Đọc Truyện Kiếm Hiệp Hay Nhất: http://truyenyy\.vn| *Đọc Truyện Online Tại http://truyenyy\.vn| *Truyện Sắc Hiệp - http://truyenyy\.vn| *Đọc Truyện Kiếm Hiệp http://truyenyy\.vn|truyenyy\.vn|truyenyy| *Bạn đang đọc truyện được lấy tại TruyệnFULL\.vn chấm cơm\.| *Truyện Tiên Hiệp - Truyện FULL)'
