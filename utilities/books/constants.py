# Book list
FULL_NAME = 'full_name'
SHORT_NAME = 'short_name'
AUTHOR = 'author'

# Common variables
BASE_URL = 'https://truyenyy.com/truyen/{0}/chuong-1.html'
TITLE_INDEX = 'title_index'
TITLE_CONTENT = 'title_content'
CONTENT = 'content'
NEXT_CHAPTER = 'next_chapter'
BOOK_HEADER = '# **{0}**\n\nTác giả: **{1}**\n\n---'
FILE_NAME = '{}.md'
EBOOK_NAME = '{}.docx'
EPISODE_HEADER = '\n\n## Chương {0}: {1} {{#chuong-{0}}}\n\n'
AZW3 = 'azw3'

# Ebook convert commands
MD_DOCX = 'pandoc -o {0} -f markdown-yaml_metadata_block -t docx {1}'
DOCX_AZW3 = 'ebook-convert {0}.docx {0}.azw3'
DOCX_EPUB = 'ebook-convert {0}.docx {0}.epub'

# Ebook metadata edit commands
METADATA = 'ebook-meta {2}.{3} -t "{0}" -a "{1}"'

# XPath selector
TITLE_INDEX_PATH = "//li[@class='breadcrumb-item active']"
NEXT_CHAPTER_PATH = "//*[contains(text(),'Chương Tiếp Theo')]/@href"
RAW_GIST_PATH = "(//div[@class='file-actions']/a)[1]/@href"

# CSS selector
TITLE_CONTENT_PATH = '.chapter-title'
CONTENT_PATH = '.inner'

# Book list's url
BOOK_LIST_GIST = 'https://gist.githubusercontent.com/zeratul0097/4df725ee5e50843f6745ccbf8791d423'
