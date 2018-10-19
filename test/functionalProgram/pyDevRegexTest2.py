'''
Created on 06-Jun-2018

@author: Pritika
'''
import re

pattern = 'bash$'
m =filter(lambda line: re.search(pattern, line, re.I), open('/Users/****/Documents/jdevgit/fork/****/api/src/setupenv_local.sh')) # filter return list by default else tuple or string
m2 =filter(lambda line: re.search(pattern, line, re.I), open('/etc/passwd'))

for match in m2:
    print(match)