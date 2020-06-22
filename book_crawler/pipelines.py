# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import pymongo
from dotenv import load_dotenv
from utilities.books.constants import SHORT_NAME, TITLE_INDEX

load_dotenv(dotenv_path='.env')


class MongoPipeline(object):
    def __init__(self):
        self.collection_name = None
        self.mongo_uri = os.getenv('MONGODB_URI')
        self.mongo_db = os.getenv('MONGODB_DATABASE')
        self.client = None
        self.db = None

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
    #     )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        short_name = item[SHORT_NAME]
        del item[SHORT_NAME]
        if TITLE_INDEX in item:
            self.db[short_name].update_one({TITLE_INDEX: item[TITLE_INDEX]}, {
                                           '$set': item}, upsert=True)
        else:
            self.db[short_name].update_one(item, {'$set': item}, upsert=True)
        return item
