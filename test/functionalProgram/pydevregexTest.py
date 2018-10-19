'''
Created on 06-Jun-2018

@author: Pritika
'''
import re

pattern ='python'
s ='the pYthon and the perl'

print(re.search(pattern, s, re.I))