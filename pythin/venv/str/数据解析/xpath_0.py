# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/10 14:59
# @Author : 成为F
# @File : xpath_0.py
# @Software : PyCharm

import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    url = 'https://sh.58.com/ershoufang/'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    li_list = tree.xpath('/html/body/div[5]/div[5]/div[1]/ul/li')
    #print(li_list)
    fp = open('./58.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')
    fp.close()










