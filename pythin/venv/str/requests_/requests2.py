# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/3 16:19
# @Author : 成为F
# @File : resquests.py
# @Software : PyCharm
import requests
if __name__ == '__main__':
   headers = {
            'User-Agent' :'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
   }
   url = 'https://www.sogou.com/web'
   kw = input('enter a word:')
   param = {
       'query':kw
   }

   response = requests.get(url=url,params=param,headers=headers)

   page_text = response.text
   filename = kw+'.html'
   print(page_text)
   with open(filename,'w',encoding='utf-8') as fp:
      fp.write(page_text)
   print(filename,'ok')


