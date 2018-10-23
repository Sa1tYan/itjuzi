import requests
import json

class IpPool(object):
    def __init__(self):
        self.url = 'https://dps.kdlapi.com/api/getdps/?orderid=983733891297048&num=50&pt=1&ut=1&format=json&sep=1'

    def get_data(self):
        resp = requests.get(self.url)
        # print(resp.content.decode())
        return resp.content.decode()

    def save_data(self, data_list):
        dict_data = json.loads(data_list)
        temp_data = dict_data['data']['proxy_list']
        temp_list = []
        for data in temp_data:
            data1 = "http://" + data
            temp_list.append(data1)
        temp_dict = {}
        temp_dict['proxy_list'] = temp_list
        return temp_dict

    def run(self):
        data_list = self.get_data()
        data = self.save_data(data_list)
        return data



# if __name__ == '__main__':
#     ip = IpPool('https://dps.kdlapi.com/api/getdps/?orderid=983733891297048&num=20&pt=1&format=json&sep=1')
#     ip.run()