'''
Created on 06-Jun-2018

@author: pritika sambyal
'''
class SystemInformation:
    def __init__(self):
        '''
        magic method of python to contruct obj
        '''
        print(self,'am in constructor')
        
    def __del__(self):
        '''
        magic method of python to destroy obj when an object is garbage collected 
        '''
        print(self,'am getting destroyed')
        
    def __custom__(self):
        print(self,"am I called???")

si = SystemInformation()
print('si==>',si)
