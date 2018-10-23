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
        a = random.randint(1,2)

        if a == 1:
            # chrome = webdriver.ChromeOptions()
            # chrome.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"')
            self.driver = webdriver.Chrome()
        else:
            fire = webdriver.FirefoxOptions()
            # fire.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"')
            self.driver = webdriver.Firefox()
        # 构建无界面的Chrome
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # self.driver = webdriver.Chrome(chrome_options=options)
        # self.driver.get( 'https://www.itjuzi.com/user/login' )
        # if self.driver.find_element_by_xpath( '//*[@id="create_account_email"]' ):
        #     user = self.driver.find_element_by_xpath( '//*[@id="create_account_email"]' )
        #     user.send_keys( '18676751579' )
        #     pwd = self.driver.find_element_by_xpath( '//*[@id="create_account_password"]' )
        #     pwd.send_keys( 'yan677326' )
        #     login_button = self.driver.find_element_by_xpath( '//*[@id="login_btn"]' )
        #     login_button.click()

    # 第一个参数是尝试次数，第二个参数是尝试间隔时间，超时会抛出异常，这样做的好处是节约时间，不需再用time去直接等待固定时间
    @retry(stop_max_attempt_number = 20, wait_fixed=500)
    def retry_load_page(self, request, spider):
        try:
            # 如果这里出现异常则交给try捕获，那么retry则不会工作
            self.driver.find_element_by_xpath('//ul[@class="list-main-personset person-list-result"]')
        except Exception as e:
            spider.logger.info('Retry<{}> page ({}times)'.format(request.url, self.count))
            self.count+=1
            raise Exception('<{}>page load timeout'.format(request.url))

    @retry(stop_max_attempt_number = 20, wait_fixed=400)
    def retry_load_detail_page(self, request, spider):
        try:
            # 如果这里出现异常则交给try捕获，那么retry则不会工作
            self.driver.find_element_by_xpath('//*[@id="team-info"]/div[2]/a/span[2]')
            self.driver.find_element_by_xpath('//*[@id="news-dynamic"]/div[2]/a/span[2]')
        except Exception as e:
            # spider.logger.info('Retry<{}> page ({}times)'.format(request.url, self.count))
            # self.count+=1
            # raise Exception('<{}>page load timeout'.format(request.url))
            pass

    def process_request(self, request, spider):
        if 'investfirm' in request.url:
            self.count=1


            r = self.driver.get(request.url)

            # time.sleep(3)
            # self.driver.implicitly_wait()
            try:
                member_unfolder = self.driver.find_element_by_xpath('//*[@id="team-info"]/div[2]/a/span[1]')
                member_unfolder.click()
                self.driver.implicitly_wait(3)
                time.sleep(5)
            except:
                pass
            try:
                news_unfolder = self.driver.find_element_by_xpath('//*[@id="news-dynamic"]/div[2]/a/span[1]')
                news_unfolder.click()
                self.driver.implicitly_wait(3)
                time.sleep(5)
            except:
                pass
            try:
                self.retry_load_detail_page(request, spider)
                html = self.driver.page_source
                return HtmlResponse( url=self.driver.current_url, body=html.encode( 'utf-8' ),request=request)
            except Exception as e:
                spider.logger.error(e)



    # def __del__(self):
    #     self.driver.quit()


