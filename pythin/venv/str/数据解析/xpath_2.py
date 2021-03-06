# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/10 16:28
# @Author : 成为F
# @File : xpath_2.py
# @Software : PyCharm
import requests
from lxml import etree
import os

if __name__ == '__main__':

    if not os.path.exists('./piclibs'):
            os.mkdir('./piclibs')

    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    for page in range(1, 10):
        url = 'http://pic.netbian.com/4kdongman/index_' + format(page) + '.html'

        #url = 'http://pic.netbian.com/4kdongman/'

        response = requests.get(url=url,headers=headers)

        # 处理中文乱码，解码
        response.encoding = 'gbk'
        page_text = response.text


        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]//li')
        #print(li_list)


        for li in li_list:
            img_src ='http://pic.netbian.com'+ li.xpath('./a/img/@src')[0]
            print(img_src)
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg'

            #print(img_name)
            #请求图片
            img_data = requests.get(url=img_src,headers=headers).content
            img_path = 'piclibs/'+img_name
            #保存
            with open(img_path,'wb')as fp:
                fp.write(img_data)
                print(img_name,'success')

    print('over')




