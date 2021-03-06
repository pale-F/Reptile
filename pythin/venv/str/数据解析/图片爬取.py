# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/7 19:45
# @Author : 成为F
# @File : 正则1.py
# @Software : PyCharm

import requests
if __name__ == '__main__':
    url = 'https://pic.qiushibaike.com/system/pictures/12376/123765298/medium/4DQSFOC62BJCZO24.jpg'

    img_data = requests.get(url=url).content

    with open('./tu.jpg','wb')as fp:
        fp.write(img_data)
    print('over')












