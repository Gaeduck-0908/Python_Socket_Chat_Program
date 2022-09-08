# -*- coding: utf-8 -*-
# ������ ����ϱ� ���� ���̺귯��
import socket
# �����带 ����ϱ� ���� ���̺귯��
from _thread import *

Client = []

def threaded(C_socket,addr):
    print('Connect : ',addr[0], ':', addr[1])

    # Ŭ���̾�Ʈ�� ������ �����Ҷ�����
    while True:
        try:
            # ������ �޾ƿ�
            data = C_socket.recv(2048)

            # �޾ƿ� ������ ���
            print('Recived : ' + addr[0], ':', addr[1], data.decode())
            
            # ������ Ŭ���̾�Ʈ�� �����ϰ� data�� send
            if(len(Client) >= 2) :
                for C in Client :
                    if C != C_socket :
                        C.send(data)
            else :
                print('Not Users')
                continue

        except ConnectionResetError as e:
            print('Disconnected : ' + addr[0], ':', addr[1])
            Client.pop()
            break
    C_socket.close()

# ������ ���� �ּ�,��Ʈ
# HOST = '127.0.0.1'
HOST = '10.104.147.2'
while True:
    try:
        PORT = int(input('Server PORT > '))

        # ���ϻ��� 
        # AF_INET = �ּ� ü�� 
        # SOCK_STREAM = TCP�� �޾ƿ�
        S_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind = ���� ����
        S_socket.bind((HOST,PORT))

  
        # Ŭ���̾�Ʈ ���� �㰡
        S_socket.listen()

        print('Open Server')
        break
    except:
        print('Duplicate port number Please use a different number.\n')


# ���ѷ���
while True:
    print('Wait...')

    # accept = Ŭ���̾�Ʈ �޾ƿ�
    C_socket, addr = S_socket.accept()
    # ������ Ŭ���̾�Ʈ�� ����
    Client.append(C_socket)
    start_new_thread(threaded, (C_socket,addr))