'''
Created on 07-Jun-2018

@author: Pritika
'''
import socket

server_address = 'localhost', 8989

try:
    with socket.socket() as sock:
        sock.connect(server_address)
        payload = sock.recv(4096)
        print('payload',payload)
except Exception as ex:
    print(ex)