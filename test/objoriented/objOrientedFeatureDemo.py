'''
Created on 06-Jun-2018

@author: pritika sambyal
'''
import os
import pprint
import xml.etree 
#from xml import etree --> cherry picking , create etree as local variable

class SystemInformation:
    pass

si =SystemInformation()
print(si) #object for class SystemInformation
print(SystemInformation) # class reside inside __main__ namespace
print(__name__) #get default namespace of python module
print(pprint.__name__) 
