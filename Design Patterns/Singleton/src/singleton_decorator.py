from functools import wraps

def singleton(cls):
    instances = {} 
         #хранение экземпляра


         
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance
