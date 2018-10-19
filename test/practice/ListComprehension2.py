'''
Created on 06-Jun-2018

@author: Pritika
'''
from os import listdir
from pprint import pprint as pp

list_of_directorites =['/Users/*****/Downloads','/Users/****/Documents']
content ={dir_name:listdir(dir_name) for dir_name in list_of_directorites}
pp(content)