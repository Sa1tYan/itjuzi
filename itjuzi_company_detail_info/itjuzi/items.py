# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BuchongItem(scrapy.Item):
    company_name_abbr = scrapy.Field()
    page_view = scrapy.Field()
    itjuzi_url = scrapy.Field()
    company_tag = scrapy.Field()


class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    itjuzi_url = scrapy.Field()
    company_name_abbr = scrapy.Field()
    page_id = scrapy.Field()
    # page_view = scrapy.Field()
    com_title = scrapy.Field()
    com_name = scrapy.Field()
    com_location = scrapy.Field()
    com_regtime = scrapy.Field()
    com_category = scrapy.Field()
    com_round = scrapy.Field()
    com_money = scrapy.Field()


class NewsItem(scrapy.Item):
    company_name_abbr = scrapy.Field()
    news_date = scrapy.Field()
    news_title = scrapy.Field()
    news_category = scrapy.Field()
    itjuzi_url = scrapy.Field()


# class InvstComItem(scrapy.Item):
#     page_num = scrapy.Field()
#     com_name = scrapy.Field()
#     com_cat_name = scrapy.Field()
#     com_sub_cat_name = scrapy.Field()
#     invse_date = scrapy.Field()
#     invse_detail_money = scrapy.Field()
#     invse_round_id = scrapy.Field()
#     invse_total_money = scrapy.Field()
#     guzhi = scrapy.Field()
#     com_addr = scrapy.Field()
#     com_born_date = scrapy.Field()
#     com_status = scrapy.Field()
#     com_scale = scrapy.Field()
#     com_news_count = scrapy.Field()
#     com_des = scrapy.Field()
#     itjuzi_url = scrapy.Field()
#     com_slogan = scrapy.Field()
#     com_fund_needs_name = scrapy.Field()

