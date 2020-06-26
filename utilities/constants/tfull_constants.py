# URLs
BASE_URL = 'https://truyenfull.vn/{}'
LAST_CHAPTER_PAGE = 'https://truyenfull.vn/{}/trang-{}'
CHAPTER_URL = 'https://truyenfull.vn/{}/chuong-{}/'

# Book's info
BOOK_FULL_NAME_PATH = 'h3.title::text'
BOOK_AUTHOR_PATH = 'a[itemprop="author"]::text'
BOOK_LAST_CHAPTER_PATH = "//ul[@class='list-chapter']/li[last()]/a/@href"

# Chapter's content
TITLE_CONTENT_PATH = '.chapter-title'
CONTENT_PATH = '#chapter-c::text'

# Ads pattern
# ADS_PATTERN = r'(_| _| *Bạn đang đọc truyện được lấy tại T\.r\.u\.y\.e\.n\.y\.y chấm cơm\.| *Nguồn: http://truyenyy\.vn|T\.r\.u\.y\.ệtruyenyy\.vn| *Bạn đang đọc truyện tại TruyệnFULL\.vn - http://truyenyy\.vn| *Text được lấy tại http://truyenyy\.vn| *Nguồn truyện: Truyện FULL| *Bạn đang đọc truyện được copy tại Truyện FULL| *Bạn đang đọc truyện tại Truyện FULL - www\.Truyện FULL| *Đọc Truyện Online Tại Truyện FULL| *Đọc Truyện Kiếm Hiệp Hay Nhất: http://truyenyy\.vn| *Đọc Truyện Online Tại http://truyenyy\.vn| *Truyện Sắc Hiệp - http://truyenyy\.vn| *Đọc Truyện Kiếm Hiệp http://truyenyy\.vn|truyenyy\.vn|truyenyy| *Bạn đang đọc truyện được lấy tại TruyệnFULL\.vn chấm cơm\.| *Truyện Tiên Hiệp - Truyện FULL)'
