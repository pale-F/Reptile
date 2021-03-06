# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/7 19:52
# @Author : 成为F
# @File : 正则1.py
# @Software : PyCharm
import requests
import re
import os
if __name__ == '__main__':

    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    url = 'https://www.qiushibaike.com/imgrank/page/%d/'

    for pagenum in range(1,3):
        new_url = format(url%pagenum)

        page_text = requests.get(url=new_url,headers=headers).text

        #正则表达式寻找图片url内容
        ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)
        #print(img_src_list)


        #创建文件夹保存图片
        if not os.path.exists('./正则1图片'):
            os.mkdir('./正则1图片')

        for src in img_src_list:
            src = 'https:'+src
            img_data = requests.get(url=src,headers=headers).content
            #生成图片名称
            img_name = src.split('/')[-1]
            #图片地址
            img_path = './正则1图片/'+img_name
            with open(img_path,'wb')as fp:
                fp.write(img_data)
                print(img_name,'over')




