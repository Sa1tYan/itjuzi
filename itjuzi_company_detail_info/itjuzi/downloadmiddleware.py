# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
import random
import requests
from scrapy.http import HtmlResponse
from selenium import webdriver
from retrying import retry
from scrapy.conf import settings

class SeleniumMiddleware(object):
    def __init__(self):
        # 构建有界面的Chrome
        # a = random.randint(1,2)
        # a = 1
        #
        # if a == 1:
            # chrome = webdriver.ChromeOptions()
            # chrome.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"')
        self.driver = None
        self.driver_detail = None
        # self.driver_option = webdriver.ChromeOptions()
        # self.driver_option.add_argument()
        # self.driver = webdriver.Chrome(chrome_options=self.driver_option)
        # else:
        #     fire = webdriver.FirefoxOptions()
        #     # fire.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"')
        #     self.driver = webdriver.Firefox()
        # 构建无界面的Chrome
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.count_num_page = 1
        self.count_num_detail = 1

    # def login(self,driver):
    #     self.driver.get( 'https://www.itjuzi.com/user/login' )
    #     if self.driver.find_element_by_xpath( '//*[@id="create_account_email"]' ):
    #         user = self.driver.find_element_by_xpath( '//*[@id="create_account_email"]' )
    #         user.send_keys( '18676751579' )
    #         pwd = self.driver.find_element_by_xpath( '//*[@id="create_account_password"]' )
    #         pwd.send_keys( 'yan677326' )
    #         login_button = self.driver.find_element_by_xpath( '//*[@id="login_btn"]' )
    #         login_button.click()

    def login(self,driver):
        driver.get( 'https://www.itjuzi.com/user/login' )
        if driver.find_element_by_xpath( '//*[@id="create_account_email"]' ):
            user = driver.find_element_by_xpath( '//*[@id="create_account_email"]' )
            user.send_keys( '自己的账号' )
            pwd = driver.find_element_by_xpath( '//*[@id="create_account_password"]' )
            pwd.send_keys( '密码' )
            login_button = driver.find_element_by_xpath( '//*[@id="login_btn"]' )
            login_button.click()

    # 第一个参数是尝试次数，第二个参数是尝试间隔时间，超时会抛出异常，这样做的好处是节约时间，不需再用time去直接等待固定时间
    # @retry(stop_max_attempt_number = 20, wait_fixed=500)
    # def retry_load_page(self, request, spider):
    #     try:
    #         # 如果这里出现异常则交给try捕获，那么retry则不会工作
    #         self.driver.find_element_by_xpath('//ul[@class="list-main-personset person-list-result"]')
    #     except Exception as e:
    #         spider.logger.info('Retry<{}> page ({}times)'.format(request.url, self.count))
    #         self.count+=1
    #         raise Exception('<{}>page load timeout'.format(request.url))
    #
    # @retry(stop_max_attempt_number = 20, wait_fixed=300)
    # def retry_load_detail_page(self, request, spider):
    #     try:
    #         # 如果这里出现异常则交给try捕获，那么retry则不会工作
    #         self.driver.find_element_by_xpath('//*[@class="seo-important-title"]')
    #     except Exception as e:
    #         spider.logger.info('Retry<{}> page ({}times)'.format(request.url, self.count))
    #         self.count+=1
    #         raise Exception('<{}>page load timeout'.format(request.url))
    def generate_driver(self, proxy):
        driver_option = webdriver.ChromeOptions()
        driver_option.add_argument( '--proxy-server=' +proxy )
        driver = webdriver.Chrome( chrome_options=driver_option )
        # self.login( driver )
        return driver

    def process_request(self, request, spider):
        if self.count_num_page == 1:
            self.driver = self.generate_driver(request.meta['proxy'])
            self.login(self.driver)
        if self.count_num_detail == 1:
            self.driver_detail = self.generate_driver(request.meta['proxy'])

        self.count_num_page += 1
        self.count_num_detail += 1
        if 'person' in request.url:
            try:
                self.driver.get(request.url)
                html = self.driver.page_source
                url = self.driver.current_url

            except Exception as e:
                self.driver.quit()
                self.count_num_page = 1
                spider.logger.error(e)
            else:
                # self.retry_load_page(request, spider)
                # coo = self.driver.get_cookies()
                # print(coo)

                time.sleep(3)
                if self.count_num_page == 30:
                    self.driver.quit()
                    self.count_num_page = 1
                return HtmlResponse( url=url, body=html.encode( 'utf-8' ),request=request)

        elif 'company' in request.url:
            try:
                self.driver_detail.get( request.url )
                html = self.driver_detail.page_source
                url = self.driver_detail.current_url
            except Exception as e:
                self.driver_detail.quit()
                self.count_num_detail = 1
                spider.logger.error(e)
            else:
                # self.retry_load_page(request, spider)
                # coo = self.driver.get_cookies()
                # print(coo)
                # html = self.driver_detail.page_source
                # url = self.driver_detail.current_url
                time.sleep( 1 )
                if self.count_num_detail == 40:
                    self.driver_detail.quit()
                    self.count_num_detail = 1
                return HtmlResponse( url=url, body=html.encode( 'utf-8' ), request=request )
            # except Exception as e:
            #     spider.logger.error( e )
        #     s = driver.get(request.url)
        #
        #     time.sleep(2)
        #     try:
        #         html = driver.page_source
        #         return HtmlResponse( url=driver.current_url, body=html.encode( 'utf-8' ), request=request )
        #     except Exception as e:
        #         spider.logger.error( e )

        # if self.count_num == 30:
        #     self.driver.quit()
        #     self.count_num = 1
        # elif 0 < request.meta['retry'] <= 3:
        #     self.count = 1
        #     r = self.driver.get(request.url)
        #     time.sleep(2)
        #     # self.driver.implicitly_wait(1.3)
        #     try:
        #         # self.retry_load_detail_page(request,spider)
        #         html = self.driver.page_source
        #         return HtmlResponse( url=self.driver.current_url, body=html.encode( 'utf-8' ),request=request)
        #     except Exception as e:
        #         spider.logger.error( e )

        # if 'company' in request.url:
        #     try:
        #         requests.get()
        #     spider.logger.error('url error')



    # def __del__(self):
    #     self.driver.quit()


