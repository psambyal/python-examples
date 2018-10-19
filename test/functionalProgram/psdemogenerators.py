'''
Created on 06-Jun-2018

@author: Pritika
'''
def get_integers():
    '''generator function'''
    i=1
    while True:
        yield i 
        i +=1

squares =(item ** 2 for item in get_integers()) #generator expression
        
def take_n(count,seq):
    '''generator function'''
    for _ in range(count): #we used _ as named variable as it is not used inside for loop
        yield next(seq)

#iterator over generator object
for value in take_n(5, squares):
    print(value)