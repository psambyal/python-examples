'''
Created on 07-Jun-2018

@author: Pritika
'''
import logging

#logging root, logging is thread safe by default
fmt_str =' %(asctime)s::%(levelname)s::%(name)s::%(process)s::%(filename)s::%(ipaddr)s::%(message)s'
logging.basicConfig(level =logging.DEBUG,format =fmt_str, filename ='access.log') # used to alter behaviour of logger and to be used before logging start
#filename to write logs in a file
#fmt_str format of string log will be printed

#change logger name from root to User
logging.getLogger().name ='User'

logging.debug("debug message", extra =dict(ipaddr ='127.0.0.1'))
logging.info("info message", extra =dict(ipaddr ='127.0.0.1'))
logging.warning("warning message" ,extra =dict(ipaddr ='127.0.0.1'))
#logging.error("error message")
#logging.critical("critical message")  # root denotes name of default logger 
