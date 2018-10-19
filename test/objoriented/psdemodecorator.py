'''
Created on 07-Jun-2018

@author: pritika sambyal

'''

def argument_logger(func):
    '''implementing generic and flexible code'''
    def logger_handler(*args):
        result = func(*args)
        print("{} args={} returns={}".format(func.__name__, args,result))       
        return result
    return logger_handler
 
'''decorator to handle exception'''   
def handle_exception(func):
    
    def handler(*args):
        try:
            result =func(*args)
            print("{} args={} returns={}".format(func.__name__, args,result))
            return result
        except Exception as ex:
            print("exception caught==>",ex)
            return ex
    return handler


def to_json(func):
    
    def json_handler(*args):
        from json import dumps
        return_value = func(*args)
        return dumps(return_value)
    
    return json_handler   

@handle_exception
def compute2(a,b):
    return dict(result=a/b)


''' This decorator will do for us compute=to_json(argument_logger(compute))'''
@to_json
@argument_logger
def compute(a,b):
    return dict(result=a+b)

#compute =argument_logger(compute)
#print(compute)
if __name__ == '__main__':
    print(compute)
    print(compute(4, 5))
    print(compute2(2, 1))
    print(compute2(2, 0))

