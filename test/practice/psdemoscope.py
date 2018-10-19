'''
Created on 07-Jun-2018

@author: Pritika
'''

n =100 #global scope
counter =0 

def demo(x,n):
    #embedded scope
    def dummy(y):
        return x ** y #local scope for y and x get resolved from embedded scope
    
    return dummy(n)

print(demo(5,2))

def test():
    #counter +=1 # we can read function value but to update anything we should use global keyword
    global counter
    counter +=1
    
test()
test()
test()

print(counter)