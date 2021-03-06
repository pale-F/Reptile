# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/10 14:59
# @Author : 成为F
# @File : xpath_0.py
# @Software : PyCharm

from lxml import etree
if __name__ == '__main__':
    #自己创建html解析器，增加parser参数
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('text.html',parser=parser)

    r = tree.xpath('//table//div[@class="f14 m20 pageBody"]/p//text()')

    #r = tree.xpath('/html/head/title')
    print(r)