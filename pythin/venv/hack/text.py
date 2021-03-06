import socket
from io import BytesIO
import pickle

def Clent_PIC(ip,port,obj):
    try:
        msg = pickle.dumps(obj)
        send_message = BytesIO(msg)
        send_message_fragment = send_message.read(1024)


    except:
        send_message = obj
        send_message_fragment =send_message.read(1024)


    socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_obj.connect((ip,port))


    while send_message_fragment:
        socket_obj.send(send_message_fragment)
        send_message_fragment = send_message.read(1024)

    socket_obj.close()

if __name__ == '__main__':
    dict_data = {'key':'welcome to shanghai','key_2':[1,2,3,4,5]}
    Clent_PIC('192.168.0.106',6666,dict_data)


