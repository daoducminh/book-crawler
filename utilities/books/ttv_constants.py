# URLs
BASE_URL = 'https://truyen.tangthuvien.vn/doc-truyen/{}'
CHAPTER_URL = 'https://truyen.tangthuvien.vn/doc-truyen/{}/chuong-{}'

# XPath selector
BOOK_FULL_NAME_PATH = "//a[@data-eid='qd_G03']"
BOOK_AUTHOR_PATH = "//a[contains(@href,'tac-gia') and @target='_blank' and not(@data-eid)]"
CONTENT_PATH = "//div[contains(@class,'box-chap') and not(contains(@class,'hidden'))]"

# CSS selector
BOOK_LAST_CHAPTER_PATH = '#j-bookCatalogPage'
TITLE_CONTENT_PATH = 'h2'
