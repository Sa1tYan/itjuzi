# -*- coding: utf-8 -*-

# Scrapy settings for itjuzi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'itjuzi'
REDIS_HOST = '10.5.11.190'
REDIS_PORT = 6379
REDIS_PARAMS = {'db': 8}
SPIDER_MODULES = ['itjuzi.spiders']
NEWSPIDER_MODULE = 'itjuzi.spiders'
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
RANDOMIZE_DOWNLOAD_DELAY = True
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'itjuzi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 4
CONCURRENT_REQUESTS_PER_IP = 4

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   # 'itjuzi.middlewares.ItjuziSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'itjuzi.downloadmiddleware.SeleniumMiddleware': 500,
   'itjuzi.middlewares.ProxyMiddleware': 300,
   'itjuzi.middlewares.UAMiddleware': 400,
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware':300
   #  'itjuzi.middlewares.ItjuziSpiderMiddleware': 543,
   #  'itjuzi.middlewares.ItjuziSpiderMiddleware': 543,

}
RETRY_ENABLED = True
RETRY_TIMES = 30
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 407]

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'itjuzi.pipelines.ItjuziPipeline': 300,
   'itjuzi.pipelines.MongodbPipeline': 400,
   # 'itjuzi.pipelines.ExcelPipeline': 300,
}

MONGO_HOST = "10.5.11.190"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "itjuzi"  # 库名
# MONGO_COLL = "invst_com_all_info"  # collection名
# MONGO_USER = "simple" #用户名
# MONGO_PSW = "test" #用户密码

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
]

COOKIE_LIST = [
{'session': '0e8e9c978f9f8a8390658410f626904c1e38ce50', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222054', 'gr_user_id': '1a769dc3-a7c6-4f0e-9879-42cba85003a2', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'ca2bb73b-d0c0-466e-a00c-a08e13811b56', '_ga': 'GA1.2.1093659720.1539222055', '_gid': 'GA1.2.80432645.1539222055', '_gat': '1', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_ca2bb73b-d0c0-466e-a00c-a08e13811b56': 'true', 'identity': '18676751579%40test.com', 'remember_code': '6ZLoyc45Bo', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222058', 'acw_tc': '781bad2915392220674565303e31f906789e31001742567fefe9052cc333bf', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_ca2bb73b-d0c0-466e-a00c-a08e13811b56': 'user_id%3A607459', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222069', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222069', 'MEIQIA_VISIT_ID': '1BPQ3UsBSCMkHSjyKT3ggNDi1ay', 'MEIQIA_EXTRA_TRACK_ID': '1BPQ3QiArGZ6nxEJK47xJSt2oYf'},
{'session': 'd670275ab7254a1cd88f90132d90a7ee9373489d', 'gr_user_id': '12f628ed-83e1-415b-869f-815a565a09db', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'fcaaac8f-6c65-4feb-a714-9baebe63308e', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222129', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_fcaaac8f-6c65-4feb-a714-9baebe63308e': 'true', '_ga': 'GA1.2.479819166.1539222129', '_gid': 'GA1.2.1051527831.1539222129', '_gat': '1', 'identity': '18676751579%40test.com', 'remember_code': 'AL2ZdvHW5E', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222132', 'acw_tc': '781bad2515392221331378344e29a68716e3d198ed5d44c6e1df69eef24282', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_fcaaac8f-6c65-4feb-a714-9baebe63308e': 'user_id%3A607459', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222135', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222135', 'MEIQIA_VISIT_ID': '1BPQCiiw7aadmS0jkS1mYfVYZu6', 'MEIQIA_EXTRA_TRACK_ID': '1BPQCqOY0sJroFiylbOIiT8iHxW'},
{'session': 'f74335126ba9309b15449771a8f504736f54a08a', 'gr_user_id': '74d18f06-a8ae-4abd-b2b0-3188533e19ec', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'bfc6f53d-8eea-4c80-9372-397fe2ae83ab', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222196', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_bfc6f53d-8eea-4c80-9372-397fe2ae83ab': 'true', '_ga': 'GA1.2.24820304.1539222196', '_gid': 'GA1.2.667213017.1539222196', '_gat': '1', 'identity': '18676751579%40test.com', 'remember_code': '8b3lmWewVA', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222201', 'acw_tc': '76b20f6515392222008521123e79bb20db5019dff427ff489e484a45b90d03', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_bfc6f53d-8eea-4c80-9372-397fe2ae83ab': 'user_id%3A607459', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222202', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222202', 'MEIQIA_VISIT_ID': '1BPQL86P9fT98LYwP3LV2bbgBHG', 'MEIQIA_EXTRA_TRACK_ID': '1BPQL4rGEoq3zqyAQUnQGkYcfar'},
{'session': '9488b06fc2f6f0f755f2477b9a3525beb47c15a1', 'gr_user_id': '42dad3ea-b02b-4bdf-830b-a01951b7f665', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': '051713e2-b733-4da2-95ac-500d84c43cd8', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222250', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_051713e2-b733-4da2-95ac-500d84c43cd8': 'true', '_ga': 'GA1.2.733308299.1539222250', '_gid': 'GA1.2.962628592.1539222250', '_gat': '1', 'identity': '18676751579%40test.com', 'remember_code': '2ss6CURwzR', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222252', 'acw_tc': '781bad2815392222601292104e64013dad1b1542920b5c947bbc45ea68133f', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_051713e2-b733-4da2-95ac-500d84c43cd8': 'user_id%3A607459', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222262', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222262', 'MEIQIA_VISIT_ID': '1BPQRudsYi4fy7KB7WBvTT0CxfL', 'MEIQIA_EXTRA_TRACK_ID': '1BPQRoPWWDmiMMkw2oMiAehOBDg'},
{'session': 'a7d3b3a3755f6acf1eadec3c1352143299534c02', 'gr_user_id': 'c85b0de8-3096-42e0-bd01-e29f6bc451f4', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'b302cc13-bb1b-4d64-be23-05804322f6c0', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222256', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_b302cc13-bb1b-4d64-be23-05804322f6c0': 'true', '_ga': 'GA1.2.498288014.1539222256', '_gid': 'GA1.2.1888859350.1539222256', 'identity': '18676751579%40test.com', 'remember_code': 'io6PWxCael', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222258', 'acw_tc': '781bad2815392223028855524e640aa4317ee82a0bfb7a46450f582ebad60d', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_b302cc13-bb1b-4d64-be23-05804322f6c0': 'user_id%3A607459', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222304', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222304', 'MEIQIA_VISIT_ID': '1BPQSdSj537AAvMDRkcj3Qdsyv7', 'MEIQIA_EXTRA_TRACK_ID': '1BPQScJ0tw6x16cb3pGzQ2z6g2W'},
{'session': '4a43068a451dfad1a73d997e27b690badee927f3', 'gr_user_id': '0393ce42-8aea-4885-a544-bc454813b8df', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': '4f48a1c1-ba2b-4148-953c-816ba1d251e2', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222258', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_4f48a1c1-ba2b-4148-953c-816ba1d251e2': 'true', '_ga': 'GA1.2.808592694.1539222259', '_gid': 'GA1.2.136886795.1539222259', 'identity': '18676751579%40test.com', 'remember_code': 'B51pEqY.Cr', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222261', 'acw_tc': '781bad0715392224584313454e3519f4e2d1934393a0d04a439a386077314e', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_4f48a1c1-ba2b-4148-953c-816ba1d251e2': 'user_id%3A607459', '_gat': '1', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222460', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222460', 'MEIQIA_VISIT_ID': '1BPQSvT02esJJIAkFPmwpVzKoPm', 'MEIQIA_EXTRA_TRACK_ID': '1BPQSs2eq6NC8yEgB2SptdNnfd2'},
{'session': 'c5d1e7c81f38ebe12e553e8afb4dd979cb8be690', 'gr_user_id': '39fe2cc9-abbe-4d39-829f-bb5f6a517401', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'd00c99a1-e320-4587-aa35-0910a8f4f7e9', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222261', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_d00c99a1-e320-4587-aa35-0910a8f4f7e9': 'true', '_ga': 'GA1.2.374224968.1539222262', '_gid': 'GA1.2.953861319.1539222262', 'identity': '18676751579%40test.com', 'remember_code': 'gQvHqqp3ID', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222264', 'acw_tc': '781bad2415392225032291697e03b266b729b4926c461f46c6f93d365b0ad9', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_d00c99a1-e320-4587-aa35-0910a8f4f7e9': 'user_id%3A607459', '_gat': '1', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222505', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222505', 'MEIQIA_VISIT_ID': '1BPQTQhna925XpLucB80rgkqa0o', 'MEIQIA_EXTRA_TRACK_ID': '1BPQTNHKtlp37nLqVY5Hv6foIGE'},
{'session': '816916507f9f4573b8f0a5d10a27462fe3bb4c34', 'gr_user_id': '4b6cd23f-e8f5-4809-bbc6-a575384c89ec', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'f324c985-31aa-49fb-a339-09d815d943ae', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222264', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_f324c985-31aa-49fb-a339-09d815d943ae': 'true', '_ga': 'GA1.2.1855685637.1539222264', '_gid': 'GA1.2.735619281.1539222264', 'identity': '18676751579%40test.com', 'remember_code': 'xZHccj7V7j', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222267', 'acw_tc': '781bad0715392225740935272e35192399c845f8d6d289b7ac2c5f903765e3', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_f324c985-31aa-49fb-a339-09d815d943ae': 'user_id%3A607459', '_gat': '1', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222576', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222576', 'MEIQIA_VISIT_ID': '1BPQTfVCLrDR5M15MCT8lcq4RFK', 'MEIQIA_EXTRA_TRACK_ID': '1BPQTa1NvDp9bwx4t0e1HxvxOuw'},
{'session': 'eb74a225a5f3fbb57de1c9ca0492d7a7db3bfca3', 'gr_user_id': '0d66bfec-0460-4895-827e-f33b91b41809', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'b7b8c4f7-66de-42a1-83ed-35c216302111', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222559', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_b7b8c4f7-66de-42a1-83ed-35c216302111': 'true', '_ga': 'GA1.2.2109141883.1539222559', '_gid': 'GA1.2.2084999067.1539222559', 'identity': '18676751579%40test.com', 'remember_code': 'KQJ.iS1usI', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222561', 'acw_tc': '781bad3615392226157935408e2c6a01514af64d13c6509383a341262d0d1b', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_b7b8c4f7-66de-42a1-83ed-35c216302111': 'user_id%3A607459', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222617', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222617', 'MEIQIA_VISIT_ID': '1BPR4hOIJhcVhtm7JDpwPDWZnpq', 'MEIQIA_EXTRA_TRACK_ID': '1BPR4kMCdeZnkgoZuBfxLmUsBbp'},
{'session': '6d4e9c79f5fb382945a478e05f7b1627a0fcd9c8', 'gr_user_id': 'fdb16f85-c7fe-4fee-beba-4eb4c3aaf0fe', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': '5f0825e0-042c-4fd1-a608-4bc800b19f27', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1539222566', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_5f0825e0-042c-4fd1-a608-4bc800b19f27': 'true', '_ga': 'GA1.2.863205086.1539222566', '_gid': 'GA1.2.1012284469.1539222566', 'identity': '18676751579%40test.com', 'remember_code': 'TPGMdThM.i', 'unique_token': '607459', 'paidtype': 'vip', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1539222569', 'acw_tc': '781bad2415392226622818369e03b8b3082bbeec1f1fa0978d4c701cfde9b2', 'user-radar.itjuzi.com': '%7B%22n%22%3A%22Salt%22%2C%22v%22%3A3%7D', 'gr_cs1_5f0825e0-042c-4fd1-a608-4bc800b19f27': 'user_id%3A607459', '_gat': '1', 'Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222664', 'Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b': '1539222664', 'MEIQIA_VISIT_ID': '1BPR5W7DfRF7ve1DioHNAiDxHLo', 'MEIQIA_EXTRA_TRACK_ID': '1BPR5ZcwtdnhXtv9jVlwGmmYQBC'}




]

COOKIE_LIST_DETAIL = [
{'acw_tc': '781bad0815380259240434360e58d455a85b58973974aac062b32b0a7c77e5', 'session': 'd8c50f88323fa8e66dc66bf38019e3bde792d3c4', 'gr_user_id': '88ca1e4c-4246-48cd-851b-b682c0dbf901', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'f4038b98-d5af-4f46-a6c1-9f433af8bd86', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1538025928', '_ga': 'GA1.2.1706430768.1538025928', '_gid': 'GA1.2.1630726249.1538025928', '_gat': '1', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_f4038b98-d5af-4f46-a6c1-9f433af8bd86': 'true', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1538025946'},
{'acw_tc': '76b20f6915380260209078372e4026fdc383f82375a0e887d4f8968fa99f15', 'session': '0acd7706100fb6644bda0a5e2462701d17e1d25b', 'gr_user_id': '19925b7e-55f9-4495-ae15-4e22307d1bc5', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': '41eb8dc9-3adf-421f-b3bb-b38b87126df9', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1538026025', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_41eb8dc9-3adf-421f-b3bb-b38b87126df9': 'true', '_ga': 'GA1.2.1905017945.1538026025', '_gid': 'GA1.2.422734576.1538026025', '_gat': '1', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1538026028'},
{'acw_tc': '781bad3615380260653543456e2c5cfb74bd7a69f5a3922bcd04335deda030', 'session': '8026f6e99a41f1a13e614eeb24baf834bb4f5f0a', 'gr_user_id': '91bdaf9a-27f8-4b3f-b696-162157953a11', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': '4610d6e9-d46f-4d39-9737-56a504113145', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1538026069', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_4610d6e9-d46f-4d39-9737-56a504113145': 'true', '_ga': 'GA1.2.420523479.1538026070', '_gid': 'GA1.2.1989485939.1538026070', '_gat': '1', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1538026092'},
{'acw_tc': '76b20f6015380261278681414e1e9834cd69420b19fa48dc4a603b10fe9372', 'session': '53f21e300989c5202b970e755231e27875491d24', 'gr_user_id': '8e566b3b-5277-497b-b688-13ba466cc417', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'f8a3df6d-6ef6-418a-9cf7-f8d57fc52739', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_f8a3df6d-6ef6-418a-9cf7-f8d57fc52739': 'true', '_ga': 'GA1.2.14216541.1538026132', '_gid': 'GA1.2.1027173107.1538026132', '_gat': '1', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1538026132', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1538026134'},
{'acw_tc': '76b20f4815380261794336182e50fe89765758664a5bef7c446954469a3314', 'session': '93a11cf529b8952df89c72414d81516d4a086ba0', 'gr_user_id': '42a1ed2b-4fae-40f5-bec7-4612952bddbe', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': 'a97385ca-3a61-4ffc-985e-0c47954cdf29', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1538026183', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_a97385ca-3a61-4ffc-985e-0c47954cdf29': 'true', '_ga': 'GA1.2.31987305.1538026183', '_gid': 'GA1.2.238705619.1538026183', '_gat': '1', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1538026187'},
{'acw_tc': '76b20f6515380262295572421e79bef5ef3f0a30961ca2e7f597b593de9066', 'session': '035cef5b5e8dcf102be7b944640a047871e93365', 'gr_user_id': '9c7bc4fc-9702-460f-9900-a4ae0bdeaff1', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': '3146e6f9-9c1a-407c-a2d0-872b2815bcd1', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1538026233', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1538026233', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_3146e6f9-9c1a-407c-a2d0-872b2815bcd1': 'true', '_ga': 'GA1.2.2085584916.1538026234', '_gid': 'GA1.2.1361086913.1538026234', '_gat': '1'},
{'acw_tc': '781bad3615380262731997159e2c686a05453c7e5b4ef90703f58b94266633', 'session': 'b47f91a0d0168ecec2f03254694dc99cf1ffc5a6', 'gr_user_id': '2692e298-33ec-40f7-a598-75c90e46f4b4', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78': '3d6cfb3d-c1c9-441d-9ad5-5ef6f17bf4c1', 'Hm_lvt_1c587ad486cdb6b962e94fc2002edf89': '1538026277', 'Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89': '1538026277', 'gr_session_id_eee5a46c52000d401f969f4535bdaa78_3d6cfb3d-c1c9-441d-9ad5-5ef6f17bf4c1': 'true', '_ga': 'GA1.2.1906945368.1538026277', '_gid': 'GA1.2.279187255.1538026277', '_gat': '1'}


]
