'''
Created on 06-Jun-2018

@author: pritika sambyal
'''

class PackageManager:
    '''data encapsulation'''
    def __init__(self,name,version):
        self.__name =name # name is a private attribute 
        self.version = version
        
    def __get_information(self):
        self.arch ='x06' # it will do it but this is wrong way , always add variable to self in __init__ method
        print(self.release)
        print('name',self.__name)
        print('version',self.version)
    
    def wrapper(self):
        self.__get_information() 

pm=PackageManager('pip','2.2.18')
pm.release ='green parrot'
pm.wrapper() # we can access private method this way
print('---------------')
pm._PackageManager__get_information() #we can access private method this way
print('---------------')
print(dir(pm)) # get list of method or attributes of a class
#print(pm.__name) we will get attribute error as __name is private and can't be accessed outside class
print('--------------')
