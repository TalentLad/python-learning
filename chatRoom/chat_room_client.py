#!/usr/bin/python3
# 2023.05.13
import socket
import select
import struct
import sys

class User:
    def __init__(self,name,client):
        self.name = name
        self.client:socket.socket = client

    def send_train(self,data):
        name_bytes = self.name.encode('utf8')
        train_name_bytes = struct.pack('I',len(name_bytes))
        self.client.send(train_name_bytes+name_bytes+data)

    def recv_train(self):
        train_head_bytes = self.client.recv(4)
        train_head = self.client.recv(train_head_bytes[0])
        name = train_head.decode('utf8')
        data = self.client.recv(1000).decode('utf8')
        return '['+name +']' + data

class Client:
    def __init__(self,ip,port):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.epoll = select.epoll()
        self.epoll.register(self.client.fileno(),select.EPOLLIN)
        self.epoll.register(sys.stdin.fileno(),select.EPOLLIN)
        self.client.connect((self.ip, self.port))
        self.client.send(sys.argv[1].encode('utf8'))
        self.user = User(sys.argv[1],self.client)

    def task(self):
        while True:
            events = self.epoll.poll()
            for fd,event in events:
                if fd == sys.stdin.fileno():
                    data = input()
                    self.user.send_train(data.encode('utf8'))
                elif fd == self.client.fileno():
                    print(self.user.recv_train())

if __name__ == '__main__':
    client = Client('192.168.152.129',2000)
    client.task()
