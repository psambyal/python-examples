'''
Created on 06-Jun-2018

@author: pritika sambyal
'''
from test.objoriented.persontest import Person

class Employee(Person):
    def __init__(self,eid,fn,ln):
        self.eid=eid   
        super().__init__(fn,ln) #invoke overridden method
    
    def get_info(self):
        print('Employee id', self.eid)
        super().get_info();


if __name__ =='__main__':  
    e = Employee('v4004','rachel', 'rustel')
    print(__name__)
    print(e.__dict__) # everyobject maintains its dictionary and this way store values in memory
    e.email ='abc@gmail.com'
    print(e.__dict__) # dict will be updated with email
    e.get_info()
