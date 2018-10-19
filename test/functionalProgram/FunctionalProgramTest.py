'''
Created on 06-Jun-2018
Demo for the lambda operator
@author: Pritika
'''

'''
syntax :

lambda arg1,arg2 :expression
annonymous runtime function 
'''

power = lambda x,n: x ** n #never use lambda with named function i.e. using def
print(power)
print(power(3,3))
