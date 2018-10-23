# -*- coding: utf-8 -*-
import scrapy
import random
import json
import re
import time
from scrapy.spiders import CrawlSpider
from ..items import ItjuziItem, BuchongItem, NewsItem
from ..settings import USER_AGENT_LIST, COOKIE_LIST,COOKIE_LIST_DETAIL
from scrapy_redis.spiders import RedisSpider
from pymongo import MongoClient
from fake_useragent import UserAgent



class OrangeSpider(RedisSpider):
    name = 'second'
    # allowed_domains = ['itjuzi.com']
    # base_url = 'http://radar.itjuzi.com/investevent/info?location=in&orderby=def&page={}'
    redis_key = 'itjuzi:start_url'
    temp_url_list = []

    @staticmethod
    def get_com_url_list():
        conn = MongoClient( '10.5.11.190', 27017 )
        db = conn['itjuzi']
        col = db.invst_com_all_info
        temp = []
        for i in col.find():
            # print(i)
            i.pop( '_id' )
            i.pop( 'com_cat_name' )
            i.pop( 'com_sub_cat_name' )
            i.pop( 'invse_date' )
            i.pop( 'invse_detail_money' )
            i.pop( 'invse_round_id' )
            i.pop( 'invse_total_money' )
            i.pop( 'guzhi' )
            i.pop( 'com_addr' )
            i.pop( 'com_born_date' )
            i.pop( 'com_status' )
            i.pop( 'com_scale' )
            i.pop( 'com_news_count' )
            i.pop( 'com_des' )
            i.pop( 'com_slogan' )
            i.pop( 'com_fund_needs_name' )
            i.pop( 'com_name' )
            temp.append( i )
        return temp
    # def get_com_url_list():
    #     conn = MongoClient( '10.5.11.190', 27017 )
    #     db = conn['itjuzi']
    #     col = db.invst_company_url_all
    #     temp = []
    #     for i in col.find().sort([('page_id',1)]):
    #         # print(i)
    #         i.pop('_id')
    #         temp.append(i)
    #     return temp

    def parse(self, response):
        self.temp_url_list = self.get_com_url_list()
        # ua = UserAgent()
        for temp_list in self.temp_url_list:
            item = ItjuziItem()
            # user_agent = ua.random
            # user_agent = random.choice(USER_AGENT_LIST)
            item['page_id'] = temp_list['page_num']
            url = temp_list['itjuzi_url']
            # item['company_name_abbr'] = temp_list['com_name']
            # headers = {
            #     'User-Agent':user_agent,
            #     # 'referer': 'http://radar.itjuzi.com/investevent'
            #     'referer': 'https://www.itjuzi.com/person?page={}'.format(temp_list['page_id'])
            # }
            time.sleep(1)
            yield scrapy.Request(url=url, callback=self.parse_detail_page, meta={'item':item})

    # 解析竞品数据

    # def parse(self, response):
    #     for i in range(1, 5745):
    #         # cookie = random.choice(COOKIE_LIST)
    #         yield scrapy.Request(url=self.base_urls.format(i),callback=self.parse_page)
    #
    # def parse_page(self, response):
    #     # print(response.text)
    #     # print(11111)
    #     dict_data = json.loads(response.text)
    #     for data in dict_data['data']['rows']:
    #         item = InvstComItem()
    #         item['page_num'] = dict_data['data']['page_num']
    #         item['com_name'] = data['com_name']
    #         item['com_cat_name'] = data['com_cat_name']
    #         item['com_sub_cat_name'] = data['com_sub_cat_name']
    #         item['invse_date'] = data['invse_date']
    #         item['invse_detail_money'] = data['invse_detail_money']
    #         item['invse_round_id'] = data['invse_round_id']
    #         item['invse_total_money'] = data['invse_total_money']
    #         item['guzhi'] = data['guzhi']
    #         item['com_addr'] = data['com_addr']
    #         item['com_born_date'] = data['com_born_date']
    #         item['com_status'] = data['com_status']
    #         item['com_scale'] = data['com_scale']
    #         item['com_news_count'] = data['com_news_count']
    #         item['com_des'] = '"' + data['com_des'].replace("\r","").replace("\n", "").replace("\xa0", "").replace(" ", "") + '"'
    #         item['com_slogan'] = data['com_slogan']
    #         item['com_fund_needs_name'] = data['com_fund_needs_name']
    #         item['itjuzi_url'] = 'https://www.itjuzi.com/company/' + data['com_id']
    #
    #         yield item


    def parse_detail_page(self, response):
        # print(response.body.decode())
        item = ItjuziItem()
        bc_item = BuchongItem()
        item['itjuzi_url'] = response.url
        item['company_name_abbr'] = response.xpath('//*[@class="seo-important-title"]/@data-name').extract_first()
        bc_item['company_name_abbr'] = item['company_name_abbr']
        bc_item['itjuzi_url'] = response.url
        try:
            bc_item['page_view'] = response.xpath('//div[@class="block-numberpad colum3"]/div[1]/p/b/text()').extract_first().replace(" ", '').replace('\n', '').replace('\t','')
        except:
            bc_item['page_view'] = ""

        try:
            temp_list = response.xpath( '//div[@class="tagset dbi c-gray-aset tag-list"]/a/text()' ).extract()
            temp_str = ''
            for tag in temp_list:
                tag = tag.replace( '\n', '' ).replace( '\t', '' )
                temp_str = temp_str + ' ' + str( tag )
            bc_item['company_tag'] = '"' + temp_str + '"'
            yield bc_item
        except:
            bc_item['company_tag'] = ''
            yield bc_item

        news_item = NewsItem()
        news_item['company_name_abbr'] = response.xpath('//*[@class="seo-important-title"]/@data-name').extract_first()
        news_item['itjuzi_url'] = response.url
        if response.xpath('//*[@class="list-unstyled news-list"]/li'):
            node_list = response.xpath( '//*[@class="list-unstyled news-list"]/li' )
            for node in node_list:
                news_item['news_date'] = node.xpath('./span[1]/text()').extract_first().replace('\n','').replace('\t','')
                news_item['news_category'] = node.xpath('./span[2]/text()').extract_first()
                news_item['news_title'] = '"' + node.xpath('./a/text()').extract_first() + '"'
                yield news_item
        else:
            # news_item = NewsItem()
            # news_item['company_name_abbr'] = item['company_name_abbr']
            # news_item['itjuzi_url'] = response.url
            print(222222222222222222222222222222222222222222222222222222222222222222222222222)
            news_item['news_date'] = "-"
            news_item['news_category'] = "-"
            news_item['news_title'] = "-"
            yield news_item
        try:
            title_list = response.xpath('//div[@class="sub-titlebar detail-compete-info"]/a').extract()
            for i in range(len(title_list)):
                p = i + 1
                #//div[@class="tab-content"]/div[2]/ul/li/i[2]/p/a/@title
                item['com_title'] = response.xpath('//div[@class="sub-titlebar detail-compete-info"]/a[' + str(p) +']/text()').extract_first()
                info_list = response.xpath('//div[@class="tab-content"]/div[' + str(p+1) + ']/ul[1]/li')
                for info in range(len(info_list)):
                    node = '//*[@class="tab-content"]/div[' + str(p+1) + "]/ul[1]/li" + "[" +str(info+1) + "]"
                    # print(node + '/i[2]/p/a/@title')
                    # print(response.body)
                    item['com_name'] = response.xpath(node + '//p[@class="title"]/a/@title').extract_first()
                    try:
                        item['com_location'] = response.xpath(node + '//span[@class="t-small marr10"]/text()').extract_first().replace('\n',"").replace('\t', "")
                        item['com_regtime'] = response.xpath(node + '//span[@class="t-small"]/text()').extract_first().replace('\n',"").replace('\t', "")
                    except:
                        item['com_location'] = ""
                        item['com_regtime'] = ""
                    item['com_category'] = response.xpath(node + '/div/@title').extract_first()
                    item['com_round'] = response.xpath(node + '/i[3]/span/text()').extract_first()
                    item['com_money'] = response.xpath(node + '/i[4]/span/text()').extract_first()
                    yield item
        except:
            item['com_title'] = ""
            item['com_name'] = ""
            item['com_location'] = ""
            item['com_regtime'] = ""
            item['com_category'] = ""
            item['com_round'] = ''
            item['com_money']  = ""
            yield item






