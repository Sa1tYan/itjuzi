import os
import xlsxwriter
from pymongo import MongoClient

class PostData2Excel(object):
    def find_data(self):
        workbook = xlsxwriter.Workbook('D:\work_related\itjuzi\itjuzi\itjuzi.xlsx')
        worksheet = workbook.add_worksheet(name='itjuzi')
        conn = MongoClient( '127.0.0.1', 27017 )
        db = conn.itjuzi
        my_set = db.invst_person
        list1 = []
        j = 0
        for i in my_set.find():
            # print(i)
            # print(type(i))
            data = [i['company_id'], i['company_name'], i['company_name_abbr'],i['company_status'],i['company_slogen'], i['company_profile'], i['company_url'], i['company_tag'], i['company_info'], i['regtime'], i['company_scale'], i['cofunder_id'], i['cofunder_name'], i['cofunder_position'], i['cofunder_profile'], i['itjuzi_url'] ]
            worksheet.write_row(j,1, data)
            # list1.append(i)
            j += 1
        print(len(list1))
        workbook.close()


if __name__ == '__main__':
    p = PostData2Excel()
    p.find_data()
