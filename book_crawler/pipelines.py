# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from utilities.books.constants import *


class MongoPipeline(object):
    def __init__(self):
        self.collection_name = None
        self.mongo_uri = 'mongodb://localhost:27017/'
        self.mongo_db = 'scrapy'
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
        temp = dict((k, item[k]) for k in item if k != SHORT_NAME)
        self.db[item[SHORT_NAME]].insert_one(temp)
        return item
