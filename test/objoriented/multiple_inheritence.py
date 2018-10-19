'''
Created on 07-Jun-2018

@author: pritika sambyal
'''

class Alpha:
    def pprint(self):
        print('Print from Alpha')

class Beta:
    def pprint(self):
        print('Print from beta')
        
class Charlie(Beta,Alpha):
    def pprint(self):
        Alpha.pprint(self) #way to print pprint of specific class
        super().pprint() # it will invoke pprint of beta as comes first in hierarchy
        
if __name__ == '__main__':
    Charlie().pprint()
    print()
    print(Charlie.mro()) #method resolution order, order in which inheritance is followed
