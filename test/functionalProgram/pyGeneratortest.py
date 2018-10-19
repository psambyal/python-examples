'''
Created on 06-Jun-2018

@author: Pritika
'''
from pprint import pprint as pp

def change_representation(value):
    print('{} called with {}'.format(change_representation.__name__, value))
    return hex(value),oct(value),bin(value)

content =[change_representation(item) for item in range(1,5)]
pp(content)
print()

content2 = (change_representation(item) for item in range(1,5))
pp(content2)
print()
pp(next(content2))
pp(next(content2))

'''for values in content2:
    print values'''