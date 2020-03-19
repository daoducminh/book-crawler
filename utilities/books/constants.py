# Book list
FULL_NAME = 'full_name'
SHORT_NAME = 'short_name'
AUTHOR = 'author'

# Common variables
BASE_URL = 'https://truyenyy.com/truyen/{}/danh-sach-chuong?nf=yes'
FIRST_CHAPTER_URL = 'https://truyenyy.com/truyen/{0}/chuong-1.html'
CHAPTER_URL = 'https://truyenyy.com/truyen/{0}/chuong-{1}.html'
TITLE_INDEX = 'title_index'
TITLE_CONTENT = 'title_content'
CONTENT = 'content'
NEXT_CHAPTER = 'next_chapter'
LAST_CHAPTER = 'last_chapter'
BOOK_HEADER = '# **{0}**\n\nTác giả: **{1}**\n\n---'
FILE_NAME = '{}.md'
EPISODE_HEADER = '\n\n## Chương {0}: {1}\n\n'
AZW3 = 'azw3'

# XPath selector
TITLE_INDEX_PATH = "//li[@class='breadcrumb-item active']"
NEXT_CHAPTER_PATH = "//*[contains(text(),'Chương Tiếp Theo')]/@href"
RAW_GIST_PATH = "(//div[@class='file-actions']/a)[1]/@href"
BOOK_LAST_CHAPTER_PATH = "//table[contains(@class,'table table-dark')]/tbody/tr[1]/td[1]/a/@href"

# CSS selector
TITLE_CONTENT_PATH = '.chapter-title'
CONTENT_PATH = '.inner'
BOOK_FULL_NAME_PATH = 'h1.name::text'
BOOK_AUTHOR_PATH = 'div.author > a::text'

# Book list's url
BOOK_LIST_URL = 'https://raw.githubusercontent.com/zeratul0097/configurations/master/book_list.json'

# Ads pattern
ADS_PATTERN = r'(Người đăng:.+|_| _| *Bạn đang đọc truyện được lấy tại T.r.u.y.e.n.y.y chấm cơm.| *Nguồn: http://truyenyy.vn|T.r.u.y.ệtruyenyy.vn| *Bạn đang đọc truyện tại TruyệnFULL.vn - http://truyenyy.vn| *Text được lấy tại http://truyenyy.vn| *Nguồn truyện: Truyện FULL| *Bạn đang đọc truyện được copy tại Truyện FULL| *Bạn đang đọc truyện tại Truyện FULL - www.Truyện FULL| *Đọc Truyện Online Tại Truyện FULL| *Đọc Truyện Kiếm Hiệp Hay Nhất: http://truyenyy.vn| *Đọc Truyện Online Tại http://truyenyy.vn| *Truyện Sắc Hiệp - http://truyenyy.vn| *Đọc Truyện Kiếm Hiệp http://truyenyy.vn|truyenyy.vn|truyenyy| *Bạn đang đọc truyện được lấy tại TruyệnFULL.vn chấm cơm.| *Truyện Tiên Hiệp - Truyện FULL)'
