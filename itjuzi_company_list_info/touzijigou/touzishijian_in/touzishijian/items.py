# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TouzijigouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    invst_id = scrapy.Field()
    invst_name = scrapy.Field()
    invst_des = scrapy.Field()
    invst_url = scrapy.Field()
    invst_total = scrapy.Field()
    com_category = scrapy.Field()
    com_url = scrapy.Field()
    com_people_num = scrapy.Field()
    com_history_invst = scrapy.Field()
    com_capital = scrapy.Field()
    com_single_capital = scrapy.Field()
    com_invst_field = scrapy.Field()
    com_invst_rounds = scrapy.Field()
    com_manage_fund = scrapy.Field()
    # com_quit_case = scrapy.Field()
    # com_quit_case_des = scrapy.Field()
    # com_member = scrapy.Field()
    # com_member_duty = scrapy.Field()
    # com_news_title = scrapy.Field()
    # com_news_date = scrapy.Field()


class QuitCaseItem(scrapy.Item):
    invst_name = scrapy.Field()
    invst_id = scrapy.Field()
    com_quit_case = scrapy.Field()
    com_quit_case_des = scrapy.Field()


class InvstMemberItem(scrapy.Item):
    invst_id = scrapy.Field()
    invst_name = scrapy.Field()
    com_member = scrapy.Field()
    com_member_duty = scrapy.Field()
    com_member_des = scrapy.Field()

class InvstNewsItem(scrapy.Item):
    invst_id = scrapy.Field()
    invst_name = scrapy.Field()
    com_news_title = scrapy.Field()
    com_news_date = scrapy.Field()
