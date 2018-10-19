'''
Created on 19-Jun-2018

@author: Pritika
'''
from _cffi_backend import string
'''class A:
     def __init__(self):
         self.__i = 1
         self.j = 5
 
     def display(self):
         print(self.__i, self.j)
class B(A):
     def __init__(self):
         super().__init__()
         self.__i = 2
         self.j = 7  
c = B()
c.display()'''

'''''For example for string "helloworld"
 Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
'''
'''my_string = "helloworld"
dict={}
for i,j in enumerate(my_string):
    dict[j] =i 
    
print (dict)'''

'''count =0

def add():
    global count
    print ('count',count)
    count = count+1
    yield count

add()'''
my_string = 'welcomehere'
dict ={}
for i in my_string:
    #dict[i] = string.count(i)
    print(i)
    
    

    
