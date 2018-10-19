'''
Created on 09-Jun-2018

@author: Pritika
'''
import json
def test():
    monitors = [
        {"display" : True, 
         "name" : "SV DCS - FVT", 
         "order" : 501, 
         "scripts" : [
                        {"customer" : "SV", 
                         "region" : "FVT", 
                         "name" : "SV-DCS"
                         }
                    ],
         "reports" : "cfts"
        },
        {"display" : True, 
         "name" : "SV DCS - FVT", 
         "order" : 501, 
         "scripts" : [
                        {"customer" : "SV", 
                         "region" : "FVT", 
                         "name" : "SV-DCS"
                         }
                    ],
         "reports" : "its"
        }]
    sample = {}

    for monitor in monitors:
        monitor['display'] = True if 'report' in monitor and monitor['report'] else False
    
    #sample['display']=(True if monitor and monitor['reports'] is "cfts" else False for monitor in monitorList)
    for display in sample['display']:
        print(display)
        
    return sample

pList = test()
for p in pList:
    print(p)
