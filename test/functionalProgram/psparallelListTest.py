'''
Created on 06-Jun-2018

@author: Pritika
packaging parallel iteration in python in 3 list
'''
lang =['perl', 'java', 'rb']
author=['larry', 'jerry', 'cell']
version =['3.6','8.0.101','2.3']

print(zip(lang,author,version))
print()

print(list(zip(lang,author,version)))
print()

for l,a,v in zip(lang,author,version):
    print('|{:>12}|{:>12}|{}'.format(l,a,v)) #string formatting