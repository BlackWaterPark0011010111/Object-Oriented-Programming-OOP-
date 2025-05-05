class Monostate:
    _shared_state={}

    def __init__(self):
        self.__dict__=self._shared_state
    def __str__(self):
        return f"MONOSTATE: {self._shared_state}"

a = Monostate()
b=Monostate()

a.x=5
print(b.x)
print(a is b)
print("===================================")

class MonoMeta(type):
    _instance={}#здесь  ключ это класс, а значение это его единственный экземпляр.,он нужен чтобы помнить создавали ли мы уже объект этого класса.
    def __call__(cls, *args, **kwds):
        if cls not in cls._instance:
            cls._instance[cls]=super().__call__(*args, **kwds)#если экземпляра cls ещё нет в словарето мы создаём новый объект (super().__call__).
        return cls._instance[cls] # а если класс уже есть в словаре,то мы возвращаем старый объект,уже существующий екземпляр
    
class Singleton(metaclass=MonoMeta):#здесь идет создание не через type(по стандарту, а через MonoMeta )
    pass

s1=Singleton()
s2=Singleton()
print(s1 is s2)