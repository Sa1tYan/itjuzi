# -*- coding: utf-8 -*-
import scrapy
import random
import json

import time
from ..items import TouzijigouItem, QuitCaseItem, InvstMemberItem, InvstNewsItem
from ..settings import USER_AGENT_LIST
from scrapy_redis.spiders import RedisSpider
from fake_useragent import UserAgent



class OrangeSpider(RedisSpider):
    name = 'touzijigou'
    # allowed_domains = ['itjuzi.com']
    # base_url = 'http://radar.itjuzi.com/investevent/info?location=in&orderby=def&page={}'
    redis_key = 'touzijigou:start_url'
    base_url = 'http://radar.itjuzi.com/investment/info?scope=&state=&location=&character=&orderby=def&page={}'
    ua = UserAgent()
    # start_urls = ['http://radar.itjuzi.com/investment/info?scope=&state=&location=&character=&orderby=def&page={}'.format(x) for x in range(1, 2)]


    def parse(self, response):

        user_agent = self.ua.random
        headers = {
            'User-Agent': user_agent,
            'Referer': 'http://radar.itjuzi.com/investment',
            # 'Host':'radar.itjuzi.com',
            'X-Requested-With':'XMLHttpRequest',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive'
        }
        # cookies = {'gr_user_id': '6006ab05-8592-4026-a0ad-38cfbc1699bb', 'MEIQIA_EXTRA_TRACK_ID': '18BSm50jICh5bQfzDIHCzDvCwVd',
        #  '_ga': 'GA1.2.1605509681.1536216584',
        #  'acw_tc': '76b20f6215368887849566074e1c045fae99bbd17ecebe6269936652827e17',
        #  'identity': '18676751579%40test.com', 'unique_token': '607459', 'paidtype': 'vip',
        #  'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1537413934,1537430893,1537494284,'+str(int(time.time())),
        #  '_gid': 'GA1.2.1384730953.1537839394', 'remember_code': 'qTR7nIoh.h',
        #  'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1537254676,1537413947,1537494289,'+str(int(time.time())),
        #  'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': str(int(time.time())),
        #  'session': '2fc73db6e1b558764d6566db1808936dc3619566',
        #  'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D',
        #  'gr_cs1_704cf353-1e72-4306-87a0-cdefa3d8349a': 'user_id%3A607459',
        #  'MEIQIA_VISIT_ID': '1AgizypqPYTqAuAwUnzvZcJ97eZ',
        #  'gr_session_id_eee5a46c52000d401f969f4535bdaa78': '54095c50-b0ae-410a-a151-77de389e290a',
        #  'gr_cs1_54095c50-b0ae-410a-a151-77de389e290a': 'user_id%3A607459',
        #  'gr_session_id_eee5a46c52000d401f969f4535bdaa78_54095c50-b0ae-410a-a151-77de389e290a': 'true', '_gat': '1',
        #  'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': str(int(time.time()))}

        for i in range(6001, 7321):
            url = 'https://www.itjuzi.com/investfirm/{}'
            item = TouzijigouItem()
            item['invst_id'] = i
            time.sleep(2)
            yield scrapy.Request(url=url.format(i),headers=headers ,callback=self.parse_detail_page, meta={'temp':item})
        # if 'investment' in response.url:

    # def parse_page(self, response):
    #     html_text = response.body.decode()
    #     # print(html_text)
    #     dict_data_list = json.loads(html_text)
    #     # print(dict_data_list)
    #     data_list = dict_data_list['data']['rows']
    #     for data in data_list:
    #         item = TouzijigouItem()
    #         item['invst_id']  = data['invst_id']
    #         item['invst_name']  = data['invst_name']
    #         item['invst_total']  = data['invst_total']
    #         item['invst_des'] = '"' + data['invst_des'] + '"'
    #         item['invst_url'] = 'https://www.itjuzi.com/investfirm/{}'.format(item['invst_id'])
    #         yield scrapy.Request(url=item['invst_url'], callback=self.parse_detail_page, meta={'temp':item})
    # def parse_page(self, response):
    #     for i in range(1, 21):
    #         url = 'https://www.itjuzi.com/investfirm/{}'
    #         yield scrapy.Request(url=url.format(i), callback=self.parse_detail_page)
    #

    def parse_detail_page(self, response):
        item = response.meta['temp']
        try:
            item['invst_des'] = response.xpath('//*[@class="list-unstyled base-intro"]/li[1]/text()').extract_first().replace('\n', '').replace(' ', '')
        except:
            item['invst_des'] = ''
        # print(response.body.decode())
        item['invst_name'] = response.xpath('//title/text()').extract_first().replace(' - IT桔子', "")
        item['com_category'] = response.xpath('//*[@class="inner-box"]/div[@class="tag-list"]/span[last()]/text()').extract_first()
        item['com_url'] = response.xpath('//*[@class="website-box"]/@href').extract_first()
        item['com_people_num'] = response.xpath('//*[@class="block-numberpad"]/div[2]/p/b/text()').extract_first()
        item['com_history_invst'] = response.xpath('//*[@class="block-numberpad"]/div[1]/p/b/text()').extract_first()
        if response.xpath('//*[@class="list-unstyled base-intro"]/li[2]/div[1]/text()').extract_first() == '单个项目投资规模':
            item['com_capital'] = ""
            item['com_single_capital'] = response.xpath('//*[@class="list-unstyled base-intro"]/li[2]/div[2]/span[1]/text()').extract_first().replace(" ","").replace('\xa0\xa0', ';')
        elif response.xpath('//*[@class="list-unstyled base-intro"]/li[2]/div[1]/text()').extract_first() == '管理资本规模':
            try:
                item['com_capital'] = response.xpath('//*[@class="list-unstyled base-intro"]/li[2]/div[2]/span[1]/text()').extract_first() + "其中包含" + response.xpath('//*[@class="list-unstyled base-intro"]/li[2]/div[2]/span[2]/text()').extract_first().replace(" ", "").replace('\xa0\xa0', ';')
            except:
                item['com_capital'] = ""
            try:
                item['com_single_capital'] = response.xpath('//*[@class="list-unstyled base-intro"]/li[3]/div[2]/span[1]/text()').extract_first().replace(" ", "").replace('\xa0\xa0', ';')
            except:
                item['com_single_capital'] = ""

        else:
            item['com_capital'] = ""
            item['com_single_capital'] = ""
        try:
            temp_list = response.xpath('//*[@class="list-unstyled base-intro"]//li/div/a[@class="tag-scope"]/text()').extract()
            temp_str = ""
            for temp in temp_list:
                temp_str = temp_str + " " + temp
            item['com_invst_field'] = temp_str
        except:
            item['com_invst_field'] = ""
        try:
            temp_list2 = response.xpath('//*[@class="list-unstyled base-intro"]//li/div/a[@class="tag-round"]/text()').extract()
            temp_str2 = ""
            for temp2 in temp_list2:
                temp_str2 = temp_str2 + " " + temp2
            item['com_invst_rounds'] = temp_str2.replace('\xa0\xa0', ';')
        except:
            item['com_invst_rounds'] = ""
        try:
            temp_list3 = response.xpath(
                '//*[@class="list-unstyled base-intro"]//li[last()]/div[2]/a[not(contains(@class, "tag"))]/text()' ).extract()
            temp_str3 = ""
            for temp3 in temp_list3:
                temp_str3 = temp_str3 + " " + temp3
            item['com_manage_fund'] = temp_str3.replace('\xa0\xa0', ';')
        except:
            item['com_manage_fund'] = ""

        item_case = QuitCaseItem()

        try:
            node_list = response.xpath('//*[@class="logo-wall"]/a')
            for node in node_list:
                item_case['invst_name'] = item['invst_name']
                item_case['invst_id'] = item['invst_id']
                item_case['com_quit_case'] = node.xpath('./h1/text()').extract_first()
                item_case['com_quit_case_des'] = node.xpath('./p/text()').extract_first()
                yield item_case
        except:
            item_case['invst_name'] = item['invst_name']
            item_case['com_quit_case'] = ""
            item_case['com_quit_case_des'] = ""
            yield item_case

        item_member = InvstMemberItem()
        try:
            node_list2 = response.xpath('//ul[@class="list-prodcase width100"]/li/div/div[@class="right"]')
            for node2 in node_list2:
                item_member['invst_id'] = item['invst_id']
                item_member['invst_name'] = item['invst_name']
                item_member['com_member'] = node2.xpath('./p[1]/a/b/text()').extract_first()
                item_member['com_member_duty'] = node2.xpath('./p[1]/a/span/text()').extract_first()
                item_member['com_member_des'] = node2.xpath('./p[2]/text()').extract_first().replace('\n', '').replace(" ", "").replace("\r", "")
                yield item_member
        except:
            item_member['invst_name'] = item['invst_name']
            item_member['com_member'] = ""
            item_member['com_member_duty'] = ""
            item_member['com_member_des'] = ""
            yield item_member

        item_news = InvstNewsItem()
        try:
            node_list3 = response.xpath('//*[@class="list-news timelined"]/li/div')
            for node3 in node_list3:
                item_news['invst_id'] = item['invst_id']
                item_news['invst_name'] = item['invst_name']
                item_news['com_news_title'] = node3.xpath('./p[1]/a/text()').extract_first()
                item_news['com_news_date'] = node3.xpath('./p[2]/span/text()').extract_first()
                yield item_news
            # item_news['invst_name'] = item['invst_name']
            # temp_date_list = response.xpath('//*[@class="list-news timelined"]/li/div/p/span/text()').extract()
            # temp_date_str = ""
            # for date in temp_date_list:
            #     if temp_date_str=="":
            #         temp_date_str = date
            #     else:
            #         temp_date_str = temp_date_str + ";" + date
            # item_news['com_news_date'] = temp_date_str
        except:
            item_news['invst_name'] = item['invst_name']
            item_news['com_news_title'] = ""
            item_news['com_news_date'] = ""
            yield item_news
        yield item


