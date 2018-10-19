'''
Created on 07-Jun-2018

@author: pritika sambyal
'''
from copy import deepcopy

content ={'eid': 'v4004', 'fn': 'rachel', 'ln': 'rustel', 'email': 'abc@gmail.com'}

backup = content # this two will refer to same location in memory and so pop on content will reflect in backup also, this is called shallow copy
backup2 =deepcopy(content) # clone an object always use deepcopy

print(id(content))
print(id(backup))
print(id(backup2))

content.pop('fn')


print(content)
print()
print(backup)
print(backup2)
