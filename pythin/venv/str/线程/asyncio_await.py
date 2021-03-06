# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/11/19 18:30
# @Author : 成为F
# @File : asyncio.py
# @Software : PyCharm
import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '122'

async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)
    return '233'


async def main():
    print('main开始')

    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func2())
    print('mian结束')

    ret1 = await task1
    ret2 = await task2

    print(ret1)
    print(ret2)

asyncio.run(main())




