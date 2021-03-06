# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/8 19:35
# @Author : 成为F
# @File : bs4.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re
import os

if __name__ == '__main__':
    fp = open('./text.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    #print(soup.p)
    #print(soup.find('p'))
    #print(soup.find_all('p'))
    print(soup.find('p').string)
















