# -*- coding: utf-8 -*-
# ������ ����ϱ� ���� ���̺귯��
import socket
from _thread import *

# ������ ���� �ּ�,��Ʈ
# HOST = '127.0.0.1'
HOST = '10.104.147.2'
while True:
    try :
        PORT = int(input('Connect to PORT > '))

        # ���ϻ��� 
        # AF_INET = �ּ� ü�� 
        # SOCK_STREAM = TCP�� �޾ƿ�
        C_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # ���� ����
        C_socket.connect((HOST,PORT))
        print('Connect!!!')
        break
    except :
        print('The port number to connect to is different..\n')

# �����͸� �޾ƿ� �Լ�
def recv_data(C_socket) :
    while True :
        data = C_socket.recv(2048)

        print("Recived : ",repr(data.decode()))

# ������ ����
start_new_thread(recv_data, (C_socket,))

print('Enter exit or quit to exit the program')
# ������ �Է�
while True:
    # ������ ����
    text = input()

    if text == 'quit' or text == 'exit':
        print('Terminate the connection.')
        break

    C_socket.sendall(text.encode())

C_socket.close()