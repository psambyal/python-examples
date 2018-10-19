'''
Created on 07-Jun-2018

@author: Pritika
'''
import logging
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler

fmt_str ='%(asctime)s::%(levelname)s::%(name)s::%(process)s::%(filename)s::%(message)s'
formatter_object = logging.Formatter(fmt_str)
log_file_name ='messgae.log'

rotating_handler = RotatingFileHandler(log_file_name, maxBytes=32, backupCount=15)
rotating_handler.setFormatter(formatter_object)

log_file_time_name ='time.log'
rotating_timehandler = TimedRotatingFileHandler(log_file_time_name,when='s', interval=1, backupCount=10)
rotating_timehandler.setFormatter(formatter_object)

logger_4_rollover =logging.getLogger('forrolloverByte')
logger_4_rollover.setLevel(logging.DEBUG)
logger_4_rollover.addHandler(rotating_handler)

logger_4time_rollover =logging.getLogger('forrolloverTime')
logger_4time_rollover.setLevel(logging.DEBUG)
logger_4time_rollover.addHandler(rotating_timehandler)

if __name__ == '__main__':
    from time import sleep
    
    for item in range(10):
        logger_4time_rollover.debug('dummy message for debug ='.format(item))
        sleep(1)
