'''
Created on 06-Jun-2018

@author: Pritika
'''
lang =['perl', 'java', 'rb']
author=['larry', 'jerry', 'cell']


#Getting dict of 2 list using zip object
info = dict(zip(lang,author))
print(info)