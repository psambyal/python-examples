'''
Created on 08-Jun-2018

@author: Pritika
'''
from test.objoriented.psoopsssh import CustomSSHClient
import threading
import xml.etree.ElementTree as et
from time import sleep 
import logging

fmt_str ='%(threadName)s:%(message)s'
logging.basicConfig(format= fmt_str)
logging.getLogger().name ='ThreadSynchro'

class ThreadSSHClient():
    def __init__(self,host_file):
        self.host_file = host_file
        #self.lock = threading.Lock() # instance for class Lock of threading module
        self.lock = threading.Semaphore(2) # mutex, binary semaphore, count will decide number of threads allowed in critical section
        self.__thread_handler()
        
    def __get_host_info(self,xml_file):
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
        
    def __thread_handler(self):
            for host_info in self.__get_host_info(self.host_file):
                host_info.append('a.out') #target file
                
                host_info.append(self.lock) # sync child thread using lock object
                t = threading.Thread(target=SSHClientHandler, args=host_info)
                t.start()
                
            for child in threading.enumerate():
                if child is not threading.current_thread():
                    t.join()
        

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
             
            
    
if __name__ == '__main__':
    ThreadSSHClient('hosts.xml')