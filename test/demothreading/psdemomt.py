'''
Created on 08-Jun-2018

@author: Pritika
MULTITHREADING EXAMPLE WITH MAIN AND CHILD THREAD AND USAGE OF JOIN
'''
import threading
from time import sleep
from random import random

class Demo:

    def __init__(self, delay):
        t_name = threading.currentThread().name
        t_id = threading.current_thread().ident
        sleep(delay)
        print("from init",t_name, "with id ", t_id, 'waited for:', delay)

    def task_set(self,delay):
        '''threading function as child thread'''
        t_name=threading.currentThread().name
        t_id = threading.current_thread().ident
        sleep(delay)
        print(t_name,"with id ",t_id, 'waited for:', delay)
    
    
def main():
    "main method"
    list_of_threads =list()
    
    for item in range(1,6):
        rand_value= random()
        #d = Demo(rand_value) # instantiate the class
        
        '''
            # target can be any callable e.g. a function reference, a class or a lambda,
            # args is to pass argument to thread 
            # name is to change name of thread
        '''
        #t = threading.Thread(target=d.task_set, args=(rand_value,), name ='t'+str(item))

        t = threading.Thread(target=Demo, args=(rand_value,), name='t' + str(item)) # this will call init method od demo class
        
        list_of_threads.append(t)
        t.start()
        #t.join() # wait for each child thread to finish and then invoke another thread
        #print(threading.enumerate()) # print list of current running threads
        
    '''
    for t in list_of_threads:
        t.join()  #block execution of main thread until child execution terminates i.e. join thread terminates
    '''
    
    for t in threading.enumerate():
        if t is not threading.current_thread(): # it will avoid condition to put join to 2 same thread in this case main thread with main thread
            t.join()
        
    print(threading.current_thread().name,"prepare terminate")
    
if __name__ == '__main__':
    main()
    
