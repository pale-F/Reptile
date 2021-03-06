# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/5 13:59
# @Author : 成为F
# @File : requests3.py
# @Software : PyCharm

import requests
import json
if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'

    word = input('enter a word:')
    data = {
        'kw':word
    }

    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    response = requests.post(url=post_url,data=data,headers=headers)

    #json返回obj（确认服务器响应数据是json）
    dic_obj = response.json()
    print(dic_obj)

    #存储
    filename = word+'.json'
    fp = open(filename,'w',encoding='utf-8')

    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    fp.close()
    print('over')
