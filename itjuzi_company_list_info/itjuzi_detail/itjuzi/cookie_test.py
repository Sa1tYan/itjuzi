import requests

class GetCookie(object):
    def __init__(self):
        self.headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        }
        self.url = "https://www.itjuzi.com/user/login"
        self.params = {
            "identity":"18676751579",
            "password":"yan677326"
        }
    def login(self):
        ssion = requests.session()
        ssion.post(url=self.url, data=self.params, headers=self.headers)
        ssion.get("https://www.itjuzi.com/", headers=self.headers)
        cookiejar = ssion.cookies
        cookie_dict = requests.utils.dict_from_cookiejar(cookiejar)
        return cookie_dict


# if __name__ == '__main__':
#     gc = GetCookie()
#     a = gc.login()
#     print(a)