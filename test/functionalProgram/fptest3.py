'''
Created on 06-Jun-2018

@author: Pritika
'''
ascii_values =[112, 101, 116, 101, 114, 32, 112, 97, 97, 110]
'''
<ascii char ='p'>112</acsii>
'''
def tag_it(av):
    return '<ascii char="{}">{}</ascii>'.format(chr(av),av)

m=map(tag_it,ascii_values)
for tag in m:
    print(tag)
 
 
print()   
'''rewrite above code as lambda'''
m=map(lambda av:'<ascii char="{}">{}</ascii>'.format(chr(av),av),ascii_values)
for tag_l in m:
    print(tag_l)
    