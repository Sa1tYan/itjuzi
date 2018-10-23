# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json
import random
from .ip_pool import IpPool

class ProxyMiddleware(object):
    def __init__(self):
        self.ip = IpPool()
        # self.ip_dict = ip.run()
        self.ip_dict = self.ip.run()
        self.count = 1

    def process_request(self, request, spider):
        self.count += 1
        if self.count == 100:
            self.count = 1
            self.ip_dict = self.ip.run()
        request.meta['proxy'] = random.choice(self.ip_dict['proxy_list'])
        print(request.meta['proxy'], '------', self.count)