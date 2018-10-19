'''
Created on 08-Jun-2018

@author: Pritika
'''
from test.objoriented.psoopsssh import CustomSSHClient
import threading
import xml.etree.ElementTree as et
from time import sleep 
import logging
from multiprocessing.pool import ThreadPool

fmt_str ='%(threadName)s:%(message)s'
logging.basicConfig(format= fmt_str)
logging.getLogger().name ='ThreadSynchro'

class SSHClientHandler(CustomSSHClient):
    def __init__(self, host, port, user, pwd,job, target_file,lock): 
        super().__init__(host, port, user, pwd) 
        self.job = job
        self.target_file = target_file
        self.lock_obj = lock
        self.t_name = threading.current_thread().name
        self.__ssh_handler()
        
    def __ssh_handler(self):
        payload = self.check_output(self.job)
        caption = '{} ran {} @ {}'.format(self.t_name, self.job, self.host)
        
        logging.warning("waiting for lock ")
        with self.lock_obj :
            '''content manager help to '''
            logging.warning("acquired for lock ")
            sleep(1)
            with open(self.target_file, 'a') as fw:
                """critical section as 2 or more threads can write at same time so we need to execute thread synchronization for this"""
                fw.write(caption.center(80, '-') + '\n')
                fw.write(payload)
                fw.write('-' * 80 + '\n')
            
            logging.warning("releases the lock ")
        
def get_host_info(xml_file):
    try:
        xml_doc = et.parse(xml_file)
        #print(xml_doc.getroot().tag)
        #print(xml_doc.getroot().text)
        #print(xml_doc.getroot().attribute)
        
        for host_info_tag in xml_doc.getiterator('host-info'):
            host_configuration = list()
            #print(host_info_tag.tag) this is to print tag name

            host_configuration.append(host_info_tag.get('address'))
            host_configuration.append(int(host_info_tag.get('port')))
            
            for host_info_child_tag in host_info_tag:
                host_configuration.append(host_info_child_tag.text) # get the text note from child tag value from parent tag
                
            yield host_configuration
          
    except Exception as ex:
        print(ex)
 
lock = threading.Lock()
       
def task_set(host_info):
    host_info.extend(['b.out',lock])
    SSHClientHandler(*host_info)
                    
    
if __name__ == '__main__':
    pool = ThreadPool(2)
    pool.map(task_set, get_host_info('hosts.xml')) # it will have a generator/iterate able object
    