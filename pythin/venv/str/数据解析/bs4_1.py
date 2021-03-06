# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/9 15:24
# @Author : 成为F
# @File : bs4_1.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text

    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul > li')

    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        detail_page_text = requests.get(url=detail_url,headers=headers).text

        detail_soup = BeautifulSoup(detail_page_text,'lxml')

        div_tag = detail_soup.find('div',class_='chapter_content')
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title'ok')













