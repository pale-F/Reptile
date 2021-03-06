# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/10 17:15
# @Author : 成为F
# @File : test.py
# @Software : PyCharm
import random
import time
import requests
from lxml import etree
if __name__ == '__main__':
    #
    # url = 'https://www.zwwx.com/book/1/1570/900343.html'
    #
    # headers = {
    #      'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    # }
    #
    # page_text = requests.get(url=url, headers=headers).text#.encode('ISO-8859-1')
    # #print(page_text)
    # tree = etree.HTML(page_text)
    # fp = open('./asd.txt', 'w', encoding='utf-8')
    # book = tree.xpath('//*[@id="content"]//text()')
    #
    # for bo in book:
    #
    #     #print(bo)
    #     bo = '  '+bo+'\n'
    #     fp.write(bo)
    #
    # fp.close()
    for a in range(1,10):
        time.sleep(random.uniform(0,2))
        print(random.uniform(0,2))

"srcUrl":"https://video.pearvideo.com/mp4/adshort/20201117/1605689647308-15488636_adpkg-ad_hd.mp4"}}
ex = "srcUrl":"(.*?)"}}
https://video.pearvideo.com/mp4/adshort/20201117/1605689647308-15488636_adpkg-ad_hd.mp4



