# Book Crawler Project

## Installation
1. Install Python 3.
2. Install Python virtualenv.
3. Create virtual environment for project: `virtualenv .virtualenvs`
4. Install required packages: `.virtualenvs/bin/python -m pip install .`
5. Install MongoDB.

## Usage

1. Start MongoDB. Create database `scrapy`
2. Create `.env` file with configurations. For example:
   ```
   MONGODB_URI=mongodb://localhost:27017/
   MONGODB_DATABASE=scrapy
   ```
3. Create book list to crawl. For example, create `book_list.py` with:
   ```python
   book_list = [
      'dau-pha-thuong-khung',
      'nhat-niem-vinh-hang-dich'
   ]
   ```
   Books in book list have been extracted from `truyenyy`'s url. For example:
   ```
   https://truyenyy.com/truyen/dau-pha-thuong-khung/
   https://truyenyy.com/truyen/nhat-niem-vinh-hang-dich/
   ```
4. Start crawling: `.virtualenvs/bin/python -m scrapy crawl demo`
5. After crawling, create HTML ebook: `.virtualenvs/bin/python create_html_ebook.py`
6. Convert HTML ebook to AZW3 ebook: `.virtualenvs/bin/python convert_ebook.py`
7. All HTML and AZW3 books will appear in `books` folder.
