# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json

import os
import pymongo
from scrapy.conf import settings
from .items import TouzijigouItem, QuitCaseItem, InvstMemberItem, InvstNewsItem


class MongodbPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = client[settings['MONGO_DB']]  # 获得数据库句柄
        # self.coll = self.db[settings['MONGO_COLL']] # 获得collections的句柄
        self.coll_info = self.db.touzijigou_info
        self.coll_member = self.db.touzijigou_member
        self.coll_quit = self.db.touzijigou_quit
        self.coll_news = self.db.touzijigou_news

    def process_item(self, item, spider):
        if isinstance(item, TouzijigouItem):
            post_item = dict(item)
            self.coll_info.insert(post_item)
        elif isinstance(item, QuitCaseItem):
            post_item = dict(item)
            self.coll_quit.insert(post_item)
        elif isinstance(item, InvstMemberItem):
            post_item = dict(item)
            self.coll_member.insert(post_item)
        elif isinstance(item, InvstNewsItem):
            post_item = dict(item)
            self.coll_news.insert(post_item)
        else:
            spider.logger.error()
        # self.coll.insert(post_item)
        return item


class ExcelPipeline(object):

    def open_spider(self, spider):
        store_file = os.path.dirname(__file__) + '/spiders/itjuzi.csv'
        self.f = open(store_file, 'w', newline='')
        self.writer = csv.writer(self.f)
        self.writer.writerow(('company_name', 'company_name_abbr', 'company_status', 'company_slogen', 'company_profile', 'company_url', 'company_tag', 'company_info','regtime','company_scale', 'cofunder_id', 'cofunder_name', 'cofunder_position', 'cofunder_profile', 'itjuzi_url'))

    def process_item(self, item, spider):
        self.writer.writerow((
            item['company_name'], item['company_name_abbr'], item['company_status'], item['company_slogen'], item['company_profile'], item['company_url'], item['company_tag'], item['company_info'], item['regtime'],item['company_scale'],item['cofunder_id'],item['cofunder_name'],item['cofunder_position'],item['cofunder_profile'], item['itjuzi_url']))
        return item

    def close_spider(self, spider):
        self.f.close()