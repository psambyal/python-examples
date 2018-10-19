'''
Created on 06-Jun-2018

@author: Pritika
'''
import re
from sys import getsizeof


pattern = '0x[a-f0-9]+'
matched_lines =[line for line in open('messages') if re.search(pattern,line, re.I)]

print (len(matched_lines))
print ('bytes',getsizeof(matched_lines))

'''
This can create problem when size is huge and can lead of memory exception so cant be sure when this will fail, so we will use Generator
'''
g_matched_line = (log_line for log_line in open('messages') if re.search(pattern, log_line, re.I))
#print(g_matched_line) #get the generator object
#print('bytes',getsizeof(g_matched_line))


line = (line for line in g_matched_line if len(line) < 85)

for line in g_matched_line:
    print (line,end ='')  # with python 3 is print (line, end =' ')
