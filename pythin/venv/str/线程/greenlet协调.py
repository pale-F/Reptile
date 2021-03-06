# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/18 21:53
# @Author : 成为F
# @File : greenlet.py
# @Software : PyCharm
#反复横跳
from greenlet import greenlet
if __name__ == '__main__':

    def fun1():
        print(1)
        gr2.switch()
        print(2)
        gr2.switch()

    def fun2():
        print(3)
        gr1.switch()
        print(4)
        gr1.switch()

    gr1 = greenlet(fun1)
    gr2 = greenlet(fun2)

    gr1.switch()
