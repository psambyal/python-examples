'''
Created on 06-Jun-2018

@author: Pritika
'''
from timeit import timeit

def demo1():
    items = [1,2,3,4,5,6,3,5]
    
    temp = []
     
    for item in items:
        temp.append(bin(item))
    
    return temp

#list comprehension
def demo2():
    items = [1,2,3,4,5,6,3,5]
    
    temp2 =[bin(item) for item in items]

    return temp2

print(timeit('sin(90)', setup='from math import sin'))
print(timeit('demo1()', setup='from __main__ import demo1'))
print(timeit('demo2()', setup='from __main__ import demo2'))