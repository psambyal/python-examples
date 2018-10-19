'''
Created on 06-Jun-2018

@author: Pritika

yield will create generator object on method call
'''
def demo():
    '''
    generator function
    '''
    print('before 1')
    yield 123
    print ('after 1')
    
    print('before 2')
    yield 456
    print ('after 2')
    
    print('before 3')
    yield 789
    print ('after 3')
    
g = demo()

for demo_obj in g:
    print "<<{}>>>".format(demo_obj)
    print "----------"