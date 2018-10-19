'''
Created on 07-Jun-2018

@author: pritika sambyal
'''
class Connections:
    '''Borg singleton'''
    shared_state =dict() #class variable
    
    def __init__(self,connection_id):
        self.__dict__ =Connections.shared_state 
        '''every object will refer to our copy, this will help us to achieve singleton behaviour, all 
            reference will point to same dictionary and changes to 1 instances will reflect to all instances of class'''
        self.connection_id = connection_id
        
    def __str__(self):
        return "{}id={}".format(self.__class__.__name__,self.connection_id)
        
c1= Connections(1001)
print(c1)
c2= Connections(1002)
print(c2)
c3= Connections(1003)
print(c3)
print(c2) #sublime singleton and changes in 1 object reflects in all the object e.g. shopping cart even if over from 10 browser it always update in all
print(c1)
