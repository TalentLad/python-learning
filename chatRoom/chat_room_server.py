#!/usr/bin/python3
# 2023.05.13
import socket
import select
import struct

class Server:
    def __init__(self,ip,port):
        self.s_listen:socket.socket = None
        self.ip = ip
        self.port = port
        self.current_users = []
        self.epoll = select.epoll()
        self.server_init()
        self.epoll.register(self.s_listen.fileno(), select.EPOLLIN)

    def server_init(self):
        self.s_listen = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s_listen.bind((self.ip,self.port))
        self.s_listen.listen(128)

    def task(self):
        new_client,client_addr = self.s_listen.accept()
        print(client_addr)
        user_name = new_client.recv(100).decode('utf8')
        user = User(user_name,new_client)
        self.epoll.register(new_client.fileno(),select.EPOLLIN)
        self.current_users.append(user)


    def transpond(self):
        while True:
            events = self.epoll.poll()
            for fd,event in events:
                if fd == self.s_listen.fileno():
                    self.task()
                else:
                    remove_user = None
                    for user in self.current_users:
                        if fd == user.new_client.fileno():
                            data = user.new_client.recv(1000)
                            if data:
                                for other in self.current_users:
                                    if other is user:
                                        pass
                                    else:
                                        other.new_client.send(data)
                            else:
                                remove_user = user
                    if remove_user:
                        print("{}已经断开连接...".format(remove_user.name))
                        self.epoll.unregister(remove_user.new_client.fileno())
                        self.current_users.remove(remove_user)


class User:
    def __init__(self,name,new_client):
        self.name = name
        self.new_client:socket.socket = new_client

    # def send_train(self,data):
    #     train_head_bytes = struct.pack('I',len(self.name))
    #     self.new_client.send(train_head_bytes + data)

if __name__ == '__main__':
    server = Server('192.168.152.129',2000)
    server.transpond()