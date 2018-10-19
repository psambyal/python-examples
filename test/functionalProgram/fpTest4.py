'''
Created on 06-Jun-2018

@author: Pritika
'''
items =list(range(1,200))
print(items)

m = filter(lambda n: n%7 == 0,items) #filter will pick the True value and short list that values, its a callable object i.e. lambda function
print(list(m))

