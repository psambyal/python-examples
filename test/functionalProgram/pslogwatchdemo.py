'''
Created on 06-Jun-2018

@author: Pritika
'''

def tail_f(file_name):
    '''log watch using generator function'''
    try:
        with open(file_name, 'rb') as fp:
            fp.seek(0,2) #move the file pointer to the end of file
            
            while True:
                content = fp.read()
                if content:
                    yield content
                    
    except (IOError, FileNotFoundError) as err:
        print (err)

for line in tail_f('dummy.log'):
    print('line-------') 
    print (line)