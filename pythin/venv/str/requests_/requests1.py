# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/3 16:19
# @Author : 成为F
# @File : resquests.py
# @Software : PyCharm
import requests
if __name__ == '__main__':
   url = 'https://www.sogou.com/'
   response = requests.get(url = url)
   page_text = response.text
   print(page_text)
   with open('./sg.html','w',encoding='utf-8') as fp:
      fp.write(page_text)
   print('ok')


