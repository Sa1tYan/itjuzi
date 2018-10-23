# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import logging
import time
import json
from scrapy.utils.response import response_status_message

from .ip_pool import IpPool
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.conf import settings
from scrapy.exceptions import NotConfigured
from scrapy.utils.python import global_object_name
from fake_useragent import UserAgent
from .settings import USER_AGENT_LIST
from .settings import COOKIE_LIST

logger = logging.getLogger(__name__)

class UAMiddleware(object):
    # def __init__(self):
    #     self.ua = UserAgent()

    def process_request(self, request, spider):
        if request.url != 'https://www.baidu.com/':
            # cookie = random.choice( COOKIE_LIST )
            # request.cookies = cookie
            user_agent = random.choice(USER_AGENT_LIST)
            request.headers['User-Agent'] = user_agent
            # request.headers['referer'] = 'https://www.itjuzi.com/person?page={}'.format(request.meta['item']['page_id'])
            request.headers['referer'] = 'http://radar.itjuzi.com/company'
            # request.headers['Host'] = 'radar.itjuzi.com'
            # # 'Accept': 'application/json, text/javascript, */*; q=0.01',
            # # 'Accept-Encoding': 'gzip, deflate',
            # # 'Accept-Language': 'zh-CN,zh;q=0.9',
            # # 'Connection': 'keep-alive'
            # request.headers['X-Requested-With'] = 'XMLHttpRequest'
            # request.headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
            # request.headers['Accept-Encoding'] = 'gzip, deflate'
            # request.headers['Connection'] = 'keep-alive'

class ProxyMiddleware(RetryMiddleware):

    def __init__(self, settings):
        if not settings.getbool('RETRY_ENABLED'):
            raise NotConfigured
        self.max_retry_times = settings.getint('RETRY_TIMES')
        self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
        self.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')
        self.ip = IpPool()
        # self.ip_dict = ip.run()
        self.ip_dict = self.ip.run()
        self.count = 1

    def process_request(self, request, spider):
        self.count += 1
        # if isinstance(request, RetryMiddleware):

        if self.count == 35 or len(self.ip_dict['proxy_list']) < 8:
            self.count = 1
            self.ip_dict = self.ip.run()
        request.meta['proxy'] = random.choice(self.ip_dict['proxy_list'])
        print(request.meta['proxy'], '------', self.count)

# class RetryProxyMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        # print(request.headers)
        # print(request.meta)
        # print(response.body)
        # print(request)
        if request.meta.get('dont_retry', False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            self.ip_dict['proxy_list'].remove(request.meta['proxy'])
            # request.meta['proxy'] = random.choice(self.ip_dict['proxy_list'])
            return self._retry(request, reason, spider) or response
        # dict_data = json.loads( response.text )
        # if dict_data['status'] != '1':
        #     reason = response_status_message( response.status )
        #     return self._retry( request, reason, spider ) or response
        return response

    def _retry(self, request, reason, spider):
        retries = request.meta.get('retry_times', 0) + 1

        retry_times = self.max_retry_times

        if 'max_retry_times' in request.meta:
            retry_times = request.meta['max_retry_times']

        stats = spider.crawler.stats
        if retries <= retry_times:
            logger.debug("Retrying %(request)s (failed %(retries)d times): %(reason)s",
                         {'request': request, 'retries': retries, 'reason': reason},
                         extra={'spider': spider})
            retryreq = request.copy()
            print(request.meta['proxy'])
            retryreq.meta['proxy'] = random.choice(self.ip_dict['proxy_list'])
            print(retryreq.meta['proxy'])
            retryreq.meta['retry_times'] = retries
            retryreq.dont_filter = True
            retryreq.priority = request.priority + self.priority_adjust

            if isinstance(reason, Exception):
                reason = global_object_name(reason.__class__)

            stats.inc_value('retry/count')
            stats.inc_value('retry/reason_count/%s' % reason)
            return retryreq
        else:
            stats.inc_value('retry/max_reached')
            logger.debug("Gave up retrying %(request)s (failed %(retries)d times): %(reason)s",
                         {'request': request, 'retries': retries, 'reason': reason},
                         extra={'spider': spider})
# class ProxyMiddleware(object):
#
#     def process_request(self, request, spider):
#

# class ItjuziRefererMiddleware(object):
#
#     def process_request(self, reques):