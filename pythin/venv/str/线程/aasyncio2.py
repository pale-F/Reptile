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

    task_list=[
        asyncio.create_task(func(),name='n1'),
        asyncio.create_task(func2(),name='n2'),

    ]

    print('mian结束')

    #等待任务完成,返回两个值，done表示完成的返回值，penging表示未完成的返回值，timeout指最多等待时间
    done,pending = await asyncio.wait(task_list,timeout=None)
    print(done)
    #print(pending)

asyncio.run(main())




