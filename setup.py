# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name='book_crawler',
    version='1.0',
    author='minhdao',
    description='Book Crawler Project',
    packages=find_packages(exclude=[
        'docs',
        'tests',
        'static',
        'templates',
        '.gitignore',
        'README.md',
        'data',
        'books',
        'book_lists'
    ]),
    entry_points={'scrapy': ['settings = book_crawler.settings']},
    install_requires=[
        'scrapy',
        'w3lib',
        'pymongo',
        'pylint',
        'autopep8',
        'rope',
        'python-dotenv',
        'dnspython',
        'scrapy_cloudflare_middleware'
    ]
)
