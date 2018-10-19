'''
Created on 06-Jun-2018

@author: Pritika
'''
items = [1,2,3,4,5,6,3,5]
m = map(oct, items) #oct is built in function and return octal representation
print(m)  # in 2.7 it gives us physical list and 3.6 it return map object which is iterate able 

for value in m:
    print(value)
    
print()

m= map(ord, 'peter paan')
print(list(m))

'''def demo():
    print('demo functions arguments')
    
print(demo) #function as demo
demo() #print demo function content
'''