# -*- coding: utf-8 -*-
# 소켓을 사용하기 위한 라이브러리
import socket
from _thread import *

# 접속할 서버 주소,포트
# HOST = '127.0.0.1'
HOST = '10.104.147.2'
while True:
    try :
        PORT = int(input('Connect to PORT > '))

        # 소켓생성 
        # AF_INET = 주소 체계 
        # SOCK_STREAM = TCP로 받아옴
        C_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 서버 접속
        C_socket.connect((HOST,PORT))
        print('Connect!!!')
        break
    except :
        print('The port number to connect to is different..\n')

# 데이터를 받아올 함수
def recv_data(C_socket) :
    while True :
        data = C_socket.recv(2048)

        print("Recived : ",repr(data.decode()))

# 쓰레드 시작
start_new_thread(recv_data, (C_socket,))

print('Enter exit or quit to exit the program')
# 데이터 입력
while True:
    # 데이터 전송
    text = input()

    if text == 'quit' or text == 'exit':
        print('Terminate the connection.')
        break

    C_socket.sendall(text.encode())

C_socket.close()
