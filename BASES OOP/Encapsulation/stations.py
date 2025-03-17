
class Station:
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location   
    def get_name(self):
        return self._name    
    def get_location(self):
        return self._location    
    def __str__(self):
        return f"Station[name={self._name}, location={self._location}]"


class Train:
    def __init__(self, number: str, capacity: int, station: Station):
        self._number = number
        self._capacity = capacity
        self._station = station
    def get_number(self):
        return self._number   
    def get_capacity(self):
        return self._capacity   
    def set_capacity(self, capacity: int):
        self._capacity = capacity   
    def get_station(self):
        return self._station   
    def get_station_name(self):
        return self._station.get_name()   
    def __str__(self):
        return f"Train[number={self._number}, capacity={self._capacity}, station={self._station}]"





if __name__ == "__main__":
    
    station1 = Station("Central", "Berlin")
    station2 = Station("Grand Station", "Paris")
    print(station1)
    print(station2)
    train1 = Train("ICE 789", 300, station1)
    train2 = Train("TGV 450", 350, station2)
    print(train1)
    print(train2)
    train1.set_capacity(320)
    print(f"Updated {train1}")
    print("Train 1 Station Name:", train1.get_station_name())
