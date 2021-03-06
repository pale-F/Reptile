# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/5 14:19
# @Author : 成为F
# @File : requests4.py
# @Software : PyCharm
import requests
import json
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'

    param = {
        'type': '19',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20',
    }

    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    response = requests.get(url=url,params=param,headers=headers)
    list_data = response.json()
    print(list_data)

    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp,check_circular=False)
    fp.close()

    print('over')



