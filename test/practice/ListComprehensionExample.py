'''
Created on 06-Jun-2018
when output is expected in form of list we can use list comprehension 
@author: Pritika
'''
items = [1,2,3,4,5,6,3,5]

temp =[i ** i for i in items]
print(temp)

temp2 =[i for i in items]
print(temp2)

temp3 =[i for i in items if i % 2] #compound list comprehension (list comprehension with condition )
print(temp3) #even number i%2 ==0 which is false so print odd numbers

temp4 =[i for i in range(1,6)]
print(temp4) # list 

temp5 ={i:hex(i) for i in range(1,6)}
print(temp5) #dictionary doesn't follow order , we can use ordered dictionary to follow the order

temp6 ={hex(i) for i in range(1,6)}
print(temp6) # create set comprehension doesn't follow order