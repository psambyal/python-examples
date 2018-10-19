'''
Created on 06-Jun-2018

@author: Pritika
'''
items =['pam',1 ,2 ]

li= iter(items) #First takes an object and return iterator object and in case of dictionary it return iterator object of keys
#it get next object of iterator till we get topIterator
print(next(li))
print(next(li))
print(next(li))

'''
for item in items:
    print(item)
    '''
String="Hello World"
for s in String:
    print(s)