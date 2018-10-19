'''
Created on 06-Jun-2018

@author: Pritika
'''
import paramiko
from sys import stdin, stdout, stderr

class CustomSSHClient:
    def __init__(self,host,port=22,user=None,pwd=None):
        self.host =host
        self.user = user
        self.port =port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, pwd)
    
    def check_output(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        return stdout.read().decode('ascii') #convert byte string to unicode
    
    def __del__(self):
        self.ssh.close()


if __name__ == '__main__':
    ssh = CustomSSHClient('****.info',user='training', pwd='training')
    op = ssh.check_output('lscpu')
    print(op)
        

    