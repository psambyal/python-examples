'''
Created on 07-Jun-2018

@author: Pritika
'''
import socketserver
from time import ctime

class CustomReasonHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        """invoked for each client request"""
        print('recv req from :{}'.format(self.client_address))
        ts =ctime().encode('ascii') # unicode into byte string
        self.request.sendall(ts)

class DayTimeService:

    def __init__(self, server_address):
        self.server = socketserver.TCPServer(server_address, CustomReasonHandler)
        self.server.serve_forever()


if __name__ == '__main__':
    DayTimeService('localhost',8989)