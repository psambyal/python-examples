'''
Created on 08-Jun-2018

@author: Pritika
'''
import multiprocessing

def worker():
    '''function for child process'''
    p_name = multiprocessing.current_process().name
    p_id = multiprocessing.current_process().pid
    
    print(p_name ,":", p_id)

def main():   
    '''parent process'''
    for item in range(1,6):
        p = multiprocessing.Process(target=worker)
        p.start()
        
    for child in multiprocessing.active_children():
        child.join()
        

if __name__ =='__main__':
    main()
        
    