# -*- coding: utf-8 -*-
# 소켓을 사용하기 위한 라이브러리
import socket
# 스레드를 사용하기 위한 라이브러리
from _thread import *

Client = []

def threaded(C_socket,addr):
    print('Connect : ',addr[0], ':', addr[1])

    # 클라이언트가 접속을 종료할때까지
    while True:
        try:
            # 데이터 받아옴
            data = C_socket.recv(2048)

            # 받아온 데이터 출력
            print('Recived : ' + addr[0], ':', addr[1], data.decode())
            
            # 전송한 클라이언트를 제외하고 data를 send
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

# 접속할 서버 주소,포트
HOST = '127.0.0.1'
while True:
    try:
        PORT = int(input('Server PORT > '))

        # 소켓생성 
        # AF_INET = 주소 체계 
        # SOCK_STREAM = TCP로 받아옴
        S_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind = 소켓 연결
        S_socket.bind((HOST,PORT))

  
        # 클라이언트 접속 허가
        S_socket.listen()

        print('Open Server')
        break
    except:
        print('Duplicate port number Please use a different number.\n')


# 무한루프
while True:
    print('Wait...')

    # accept = 클라이언트 받아옴
    C_socket, addr = S_socket.accept()
    # 접속한 클라이언트의 갯수
    Client.append(C_socket)
    start_new_thread(threaded, (C_socket,addr))
