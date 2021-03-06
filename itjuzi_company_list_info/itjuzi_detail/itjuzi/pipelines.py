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

class ItjuziPipeline(object):

    def open_spider(self, spider):
        self.f = open('info.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        json_str = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.f.write(json_str)
        return item

    def close_spider(self, spider):
        self.f.close()


class MongodbPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = client[settings['MONGO_DB']]  # 获得数据库句柄
        self.coll = self.db[settings['MONGO_COLL']] # 获得collections的句柄

    def process_item(self, item, spider):
        if item == None:
            return item
        post_item = dict(item)
        # temp_list = post_item['cofunder_name']
        # temp_list2 = post_item['cofunder_position']
        # temp_list3 = post_item['cofunder_profile']
        # for i in range(len(post_item['cofunder_name'])):
        #     post_item['cofunder_id'] = (i+1)
        #     post_item['cofunder_name'] = temp_list[i]
        #     post_item['cofunder_position'] = temp_list2[i]
        #     post_item['cofunder_profile'] = temp_list3[i].replace('\n', '')
        self.coll.insert(post_item)
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