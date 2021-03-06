# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/18 16:34
# @Author : 成为F
# @File : 梨视频线程池.py
# @Software : PyCharm
import requests
from lxml import etree
import re

if __name__ == '__main__':
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    url = 'https://www.pearvideo.com/category_1'

    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')

    for li in li_list:
        detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
        #print(detail_url)
        name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
        #print(name)

        #对详情页发请求
        detail_page_text = requests.get(url=detail_url,headers=headers).text
        ex = '"srcUrl":"(.*?)"}}'
        video_url = re.findall(ex,detail_page_text)[0]
        print(video_url)








