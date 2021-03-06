# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/7 12:28
# @Author : 成为F
# @File : requests5.py
# @Software : PyCharm

import requests
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    data = {
        'cname': '',
        'pid': '',
        'keyword': '上海',
        'pageIndex': '1',
        'pageSize': '100',
    }

    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    response = requests.post(url=url,data=data,headers=headers)
    page_text = response.text
    print(page_text)
    with open('./kfc.html','w',encoding='utf-8') as fp:
      fp.write(page_text)
    print('ok')






