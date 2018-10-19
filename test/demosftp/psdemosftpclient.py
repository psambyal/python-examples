'''
Created on 07-Jun-2018

@author: Pritika
'''
from test.objoriented.psoopsssh import CustomSSHClient
from test.objoriented.psdemofactoryds import make_archive, glob

class CustomSFTPClient(CustomSSHClient):
    def __init__(self,host,port,user,pwd):
        super().__init__(host, port, user, pwd)
        self.sftp = self.ssh.open_sftp()
        
    def copy_to_remote(self,src_file,target_file):
        self.sftp.put(src_file,target_file)
    
    def __del__(self):
        self.sftp.close()
        super().__del__()
        
        
if __name__ == '__main__':
    archive_name = 'ps_pys.zip'
    make_archive(archive_name,*glob('../*.py')).save()
    
    sftp = CustomSFTPClient('****.info', 22, 'training' ,'training')
    sftp.copy_to_remote(archive_name, archive_name)
    print(sftp.check_output('ls -l'))