'''
Created on 07-Jun-2018

@author: Pritika
'''
def power(x,n =None):
    '''positional arguments'''
    return x ** n

print(power(3, 4))

def demo(*args): # take input as tuple and take as many number of arguments as we pass
    print(args)
    
demo()
items =(4, 5, 6, 'dadsad')
demo(items) # passing tupple as argument
demo(*items) # content of content as argument

items =[4, 5, 6, 'dadsad']
demo(items) # passing list as argument

demo(*items) # passing only value of list as argument in functions

demo(4,5,6,'dadsad')