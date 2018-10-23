import requests
from selenium import webdriver


class GetCookie(object):
    def __init__(self):
        self.list_url = "http://www.baidu.com/"
        self.headers = {
                'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        }

    def get_cookie(self):
        # resp = requests.get(self.list_url, headers=self.headers)
        # cookie = resp.cookies
        # cookie_dict = requests.utils.dict_from_cookiejar(cookie)
        # print(cookie_dict)
        chrome = webdriver.Chrome()
        chrome.get(self.list_url)
        c = chrome.get_cookies()
        print(c)

if __name__ == '__main__':
    gt = GetCookie()
    gt.get_cookie()
