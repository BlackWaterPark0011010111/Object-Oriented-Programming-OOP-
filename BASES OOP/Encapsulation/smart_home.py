

# Класс умного устройства
class SmartDevice:
    def __init__(self, name, power_status=False):
        self._name = name
        self._power_status = power_status  # Включено/выключено
    
    def turn_on(self):
        self._power_status = True
        print(f"{self._name} включено.")
    
    def turn_off(self):
        self._power_status = False
        print(f"{self._name} выключено.")
    
    def get_status(self):
        return "Включено" if self._power_status else "Выключено"
    
    def __str__(self):
        return f"SmartDevice[name={self._name}, status={self.get_status()}]"


lamp = SmartDevice("Лампа в гостиной")#с отдельными устройствами
lamp.turn_on()
print(lamp)

tv = SmartDevice("Телевизор")
tv.turn_off()
print(tv)

class Room:
# Класс для комнаты с несколькими устройствами
    def __init__(self, name):
        self._name = name
        self._devices = []
    
    def add_device(self, device: SmartDevice):
        self._devices.append(device)
    
    def turn_on_all(self):
        for device in self._devices:
            device.turn_on()
    
    def turn_off_all(self):
        for device in self._devices:
            device.turn_off()
    
    def __str__(self):
        return f"Room[name={self._name}, devices={[str(d) for d in self._devices]}]"


living_room = Room("Гостиная")# Создаём комнату и добавляем устройства
living_room.add_device(lamp)
living_room.add_device(tv)
print(living_room)


living_room.turn_on_all()# Включаем все устройства в комнате
print(living_room)


class SmartHome:# Класс умного дома
    def __init__(self, owner):
        self._owner = owner
        self._rooms = []
    
    def add_room(self, room: Room):
        self._rooms.append(room)
    
    def turn_off_all_devices(self):
        for room in self._rooms:
            room.turn_off_all()
    
    def __str__(self):
        return f"SmartHome[owner={self._owner}, rooms={[str(r) for r in self._rooms]}]"


my_home = SmartHome("Алекс")# Создаём дом и добавляем комнаты
my_home.add_room(living_room)


kitchen = Room("Кухня")# Добавляем еще одну комнату 
kettle = SmartDevice("Электрочайник")
kitchen.add_device(kettle)
my_home.add_room(kitchen)

print(my_home)


my_home.turn_off_all_devices()# Выключаем все устройства 
print(my_home)