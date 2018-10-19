'''
Created on 06-Jun-2018
Demo with context manager to do file IO
@author: Pritika
'''
from pipenv.patched.safety.formatter import FileNotFoundError
from curses.has_key import python
try:
    with open('test.py') as fp: #context manager
        print (fp)
        print('close',fp.close()) # file closed false
        
    #print(fp.close()) # file closed true
except (FileNotFoundError,IOError) as err:
    print('Error found in reading file',err)