# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/13 9:58
# @Author : 成为F
# @File : xpath作业.py
# @Software : PyCharm
import requests
from lxml import etree
if __name__ == '__main__':

    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    url = 'http://sc.chinaz.com/jianli/free.html'

    #response = requests.get(url=url, headers=headers)

    # response.encoding = 'gbk'
    # page_text = response.text
    page_text = requests.get(url=url, headers=headers).text.encode('ISO-8859-1')


    tree = etree.HTML(page_text)

    #box_list = tree.xpath('//div[@class="main_list jl_main masonry"]')
    box_list = tree.xpath('//*[@id="container"]/div')

    fp = open('./简历.txt', 'w', encoding='utf-8')
    for box in box_list:
        url_ie = 'http:'+box.xpath('./a/@href')[0]
        name = box.xpath('./a/img/@alt')[0]
        #print(ie)
        #print(name+':'+url_ie)

        pagedown_text = requests.get(url=url_ie, headers=headers).text
        #print(pagedown_text)

        #下载压缩包地址
        tree = etree.HTML(pagedown_text)
        down_list = tree.xpath('// *[ @ id = "down"] / div[2] / ul / li[1] / a/ @href')[0]
        #print('下载地址：'+down_list)



        #保存到txt
        fp.write(name+': '+url_ie+'\n'+'下载地址：'+down_list+ '\n'+'\n')
    fp.close()


















