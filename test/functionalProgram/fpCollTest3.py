'''
Created on 06-Jun-2018

@author: Pritika
'''
from functools import reduce

items =[11,22,33,44,55,6,8]

#print(reduce(lambda a, b : a + b, items)) # this will work as a = a+b, reduce will always take 2 arguments
try:
    min_line = reduce(lambda line1, line2: line1 if len(line1) < len(line2) else line2, open('/etc/passwd'))
    print(min_line)
except Exception as ex:
    print(ex)