from os import getenv
import sys
import pymongo
from book_crawler.utilities.constants.common_constants import *
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
DATABASE_URI = getenv('MONGODB_URI')
FILE_FORMAT = '<html>\n<head>\n{0}\n</head>\n<body>\n{1}</body>\n</html>'
BOOK_HEADER = '<title>{0}</title>\n<meta name="author" content="{1}">'
CHAPTER = '<h1 title="{0}">Chương {0}: {1}</h1>\n<div>{2}</div>\n'
HTML_FILE = 'books/{0}-{1}.html'
FIELD_EXSITED = {'$exists': True}
CHAPTERS_PER_PART = 500


def create_html_ebook(book_source, book_list):
    client = pymongo.MongoClient(DATABASE_URI)
    db = client[book_source]

    for book in book_list:
        collection = db[book]
        response = collection.create_index([(TITLE_INDEX, pymongo.ASCENDING)])
        print(response)

        header = collection.find_one({AUTHOR: FIELD_EXSITED})
        h = BOOK_HEADER.format(header[FULL_NAME], header[AUTHOR])
        body = ''
        last_chapter = header[LAST_CHAPTER]
        remainder = last_chapter % CHAPTERS_PER_PART
        max_parts = last_chapter // CHAPTERS_PER_PART
        if remainder != 0:
            max_parts = max_parts + 1

        for i in range(max_parts):
            chapters = collection.find({TITLE_INDEX: FIELD_EXSITED}).sort(
                TITLE_INDEX, pymongo.ASCENDING).limit(CHAPTERS_PER_PART).skip(i*CHAPTERS_PER_PART)

            for chapter in chapters:
                arr = chapter[CONTENT].split('\n\n')

                content = '<p>'+'</p><p>'.join(arr)+'</p>'
                body += CHAPTER.format(
                    chapter[TITLE_INDEX],
                    chapter[TITLE_CONTENT],
                    content)
            with open(HTML_FILE.format(book, i+1), 'w') as file:
                file.write(FILE_FORMAT.format(h, body))
    client.close()
