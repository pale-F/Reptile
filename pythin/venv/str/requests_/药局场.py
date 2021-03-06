# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/7 13:13
# @Author : 成为F
# @File : 药局场.py
# @Software : PyCharm
import requests
import json
if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    data = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':'',
    }
    json_ids = requests.post(url=url,data=data,headers=headers).json()

    id_list = []

    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    # print(id_list)



    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    all_list_dtail = []
    for id in id_list:
        data = {
            'id':id
        }
        json_detail = requests.post(url=url, data=data, headers=headers).json()

        all_list_dtail.append(json_detail)
        #print(json_detail)

        #存储
    fp = open('./药监局data.json','w',encoding='utf-8')
    json.dump(all_list_dtail,fp=fp,ensure_ascii=False)
    print('over')


