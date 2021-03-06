# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/15 11:26
# @Author : 成为F
# @File : 古诗文网.py
# @Software : PyCharm
import requests
from lxml import etree
#图片识别
import base64
import json

#图片识别
def base64_api(img):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": 'xxxx', "password": 'xxxxx', "image": b64} #图鉴端口账号 密码
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

if __name__ == '__main__':
    url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
         'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    code_img_src = 'https://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data = requests.get(url=code_img_src,headers=headers).content
    #保存本地图片
    with open('./data.jpg','wb')as fp:
        fp.write(img_data)
    #请求识别
    img_path = "./data.jpg"
    result = base64_api(img=img_path)
    print(result)