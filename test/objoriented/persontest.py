'''
Created on 06-Jun-2018

@author: pritika sambyal
'''
class Person:
    def __init__(self,first_name,last_name):
        self.fn =first_name
        self.ln = last_name
    
    def get_info(self):
        print('fn==>',self.fn)
        print('ln==>',self.ln)


if __name__ == '__main__':  # this is to avoid when we run this script from another script these should b=not be printed, and run this when we try to namespace from main   
    p=Person('marry', 'claire')
    p.get_info()
    print(__name__)
