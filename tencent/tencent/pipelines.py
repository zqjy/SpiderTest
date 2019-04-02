# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from tencent.items import TencentItem

client = MongoClient('192.168.31.64', 27017)
collection = client["tencent"]["hr"]

class TencentPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "hr":
            if isinstance(item, TencentItem):
                collection.insert(dict(item))
            # list = [v for v in item.values()]
            # print(','.join(list))
        return item
