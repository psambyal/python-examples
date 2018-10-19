'''
Created on 06-Jun-2018
Demo without context manager to do file IO
@author: Pritika
'''
from pipenv.patched.safety.formatter import FileNotFoundError
try:
    fp =None
    fp = open('test')
    print (fp)
except (FileNotFoundError,IOError) as err:
    print('Error found in reading file',err)
finally:
    if fp:
        fp.close()