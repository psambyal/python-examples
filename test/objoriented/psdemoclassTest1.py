'''
Created on 07-Jun-2018

@author: pritika sambyal
'''
class ConnectionPool:
    connection_counter =0 # class variable
    max_conn = 3
    
    def __init__(self,c_id):
        self.c_id = c_id
        ConnectionPool.connection_counter +=1
        ConnectionPool.check_4_limits(self)
    
    
    ''' class method will accept class reference as its argument'''
    @classmethod   
    def check_4_limits(cls,connection_pool_obj):
        if cls.connection_counter > cls.max_conn:
            error_message = 'Maximum connection limit reached: connection_id {}'.format(connection_pool_obj.c_id)
            
            raise Exception (error_message)  #  throw an exception    

     
    '''instance method so take first value as reference of class '''  
    def __str__(self):
        remaining_connection ="remaining_slot: {}".format(ConnectionPool.max_conn -ConnectionPool.connection_counter)
        
        return '{} connection ={} {}'.format(self.__class__.__name__, self.c_id, remaining_connection)

                                          
if __name__ == '__main__':
    try:
        for item in range(1,5):
            print(ConnectionPool(item))
    except Exception as ex:
        print(ex)
