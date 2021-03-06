# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/13 20:15
# @Author : 成为F
# @File : 爬取小说.py
# @Software : PyCharm
#https://www.zwwx.com/  中网文学

import random
import time
import requests
from lxml import etree
import time
if __name__ == '__main__':
    a = random.uniform(0, 2)
    time.sleep(a)
    #url = 'https://www.zwwx.com/book/1/xxxx/'
    url ='https://www.zwwx.com/book/13/13404/'

    headers = {
         'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    page_list = requests.get(url=url,headers=headers).text


    tree = etree.HTML(page_list)
    #书名和作者
    book_Information = tree.xpath('//*[@id="list"]/dl/dt/text()')[0]
    #print(book_Information)
    #章节网址
    Chapter_list = tree.xpath('//*[@id="list"]/dl/dd')
    #print(Chapter_list)
    print(book_Information+'网页获取成功')
    #文件名
    txt_name ='./'+book_Information+'.txt'
    fp = open( txt_name , 'w', encoding='utf-8')

    for web in Chapter_list:
        #各章节地址
        url_chapter = 'https://www.zwwx.com' + web.xpath('./a/@href')[0]
        #章节名
        chapter_name = web.xpath('./a/text()')[0]
        #print(chapter_name)

        chapter_list = requests.get(url=url_chapter,headers=headers).text
        tree = etree.HTML(chapter_list)
        book = tree.xpath('//*[@id="content"]//text()')
        #章节名
        ch_name = chapter_name+'\n'
        #保存章节名
        fp.write(ch_name)
        #延时
        time.sleep(random.uniform(0, 1))

        for book_paragraph in book:
            #章节内容
            book_paragraph = '  '+book_paragraph+'\n'
            #一章后回车

            fp.write(book_paragraph)

        print(chapter_name + ' 获取成功')
        #每章节后面加回车
        book_paragraph = '\n' + '\n'
        fp.write(book_paragraph)
    fp.close()



