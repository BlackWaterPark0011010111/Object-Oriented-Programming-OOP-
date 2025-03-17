from abc import ABC, abstractmethod
from typing import Dict, List, DefaultDict
from collections import defaultdict

class Device(ABC):
    def __init__(self, name: str):
        self._name = name 

    @property
    def name(self) -> str:  
        return self._name

    @name.setter
    def name(self, new_name: str):  
        if not new_name:
            raise ValueError("Device name cannot be empty!")
        self._name = new_name
#Abstract method (must be implemented in subclasses)
    @abstractmethod
    def turn_on(self) -> str:  
        pass

    @abstractmethod
    def turn_off(self) -> str: 
        pass

    def __str__(self) -> str:  
        return f"{self.__class__.__name__}: {self._name}"

#Device
class SmartLight(Device):
    def turn_on(self) -> str:
        return f"{self._name} is on. The light is bright!"

    def turn_off(self) -> str:
        return f"{self._name} is off. It's dark."

class SmartThermostat(Device):
    def turn_on(self) -> str:
        return f"{self._name} is on. Temperature is being regulated."

    def turn_off(self) -> str:
        return f"{self._name} is off. Temperature is not being controlled."


class DeviceFactory:
    @staticmethod
    def create_device(device_type: str, name: str) -> Device:
        if device_type == "Light":
            return SmartLight(name)
        elif device_type == "Thermostat":
            return SmartThermostat(name)
        else:
            raise ValueError("Unknown device type")

#Smart Home Singleton
class SmartHomeSystem:
    _instance = None
    devices: DefaultDict[str, List[Device]]#нужно объявить devices как атрибут класса с аннотацией, а затем инициализируем его в методе __new__.
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        #   cls._instance.devices: Dict[str, List[Device]] = defaultdict(list) 
 #            Python не позволяет аннотировать тип переменной при её инициализации 
 #            внутри класса.  Проблема аннотации типов для атрибутов класса должны быть указаны на уровне класса,
 # а не внутри методов или конструктора. devices — это атрибут экземпляра,
 #   который инициализируется в методе __new__. аннотация типа для devices должна быть   указана на уровне класса.
            cls._instance.devices= defaultdict(list)# Using defaultdict
        return cls._instance

    def add_device(self, device: Device):# Adding a device
        self.devices[device.__class__.__name__].append(device)

    def turn_on_all_devices(self) -> List[str]:  
        results = []
        for device_type, devices in self.devices.items():
            for device in devices:
                results.append(device.turn_on())
        return results

    def turn_off_all_devices(self) -> List[str]:  
        results = []
        for device_type, devices in self.devices.items():
            for device in devices:
                results.append(device.turn_off())
        return results

    def __str__(self) -> str:  
        return f"Smart Home: {len(self.devices)} device types, total {sum(len(devices) for devices in self.devices.values())} devices"


if __name__ == "__main__":

    #the factory  creating devices 
    light1 = DeviceFactory.create_device("Light", "Living Room Light")
    light2 = DeviceFactory.create_device("Light", "Kitchen Light")
    thermostat = DeviceFactory.create_device("Thermostat", "Living Room Thermostat")


#Singleton
# Create the smart home system
    smart_home = SmartHomeSystem()

    #Add devices
    smart_home.add_device(light1)
    smart_home.add_device(light2)
    smart_home.add_device(thermostat)


    print("Turning on all devices:")
    for result in smart_home.turn_on_all_devices():
        print(result)

    print("\nSystem Information:")
    print(smart_home)