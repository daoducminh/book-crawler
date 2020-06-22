import os
import pymongo
from dotenv import load_dotenv
from book_list import book_list

load_dotenv(dotenv_path='.env')

DATABASE_NAME = os.getenv('MONGODB_DATABASE')
DATABASE_URI = os.getenv('MONGODB_URI')
TITLE_INDEX = 'title_index'
TITLE_CONTENT = 'title_content'
CONTENT = 'content'
FULL_NAME = 'full_name'
SHORT_NAME = 'short_name'
AUTHOR = 'author'
LAST_CHAPTER = 'last_chapter'
# BOOK_HEADER = '# **{0}**\n\nTác giả: **{1}**\n\n---'
FILE_FORMAT = '<html>\n<head>\n{0}\n</head>\n<body>\n{1}</body>\n</html>'
BOOK_HEADER = '<title>{0}</title>\n<meta name="author" content="{1}">'
# CHAPTER = '\n\n## Chương {0}: {1}\n\n{2}'
CHAPTER = '<h2 title="{0}">Chương {0}: {1}</h2>\n<div>{2}</div>\n'
HTML_FILE = 'books/{}.html'
FIELD_EXSITED = {'$exists': True}
CHAPTERS_PER_PART = 1000


def main():
    client = pymongo.MongoClient(DATABASE_URI)
    db = client[DATABASE_NAME]

    for book in book_list:
        collection = db[book]
        response = collection.create_index([(TITLE_INDEX, pymongo.ASCENDING)])
        print(response)

        header = collection.find_one({AUTHOR: FIELD_EXSITED})

        file = open(HTML_FILE.format(book), 'w')
        h = BOOK_HEADER.format(header[FULL_NAME], header[AUTHOR])
        body = ''
        last_chapter = header[LAST_CHAPTER]
        remainder = last_chapter % CHAPTERS_PER_PART
        max_parts = last_chapter//CHAPTERS_PER_PART
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

        file.write(FILE_FORMAT.format(h, body))
        file.close()

    client.close()


if __name__ == '__main__':
    main()
