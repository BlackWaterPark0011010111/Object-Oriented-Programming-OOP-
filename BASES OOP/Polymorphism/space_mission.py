from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

# AbstractBaseClass 
class Astronaut(ABC):
    def __init__(self, name: str, experience: int):
        self._name = name  #Encapsulation
        self._experience = experience

    @property
    def name(self) -> str: 
        return self._name

    @property
    def experience(self) -> int:  
        return self._experience

    @abstractmethod
    def perform_task(self) -> str:  #Abstract method 
        pass

    def __str__(self) -> str:  #Magic method for string representation
        return f"{self.__class__.__name__}: {self._name}, Experience: {self._experience} years"

#Pilot Astronaut (inherits from Astronaut)
class Pilot(Astronaut):
    def perform_task(self) -> str:  #Polymorphism
        return f"{self._name} is piloting the spaceship."

#Engineer Astronaut (inherits from Astronaut)
class Engineer(Astronaut):
    def perform_task(self) -> str:  #Polymorphism
        return f"{self._name} is repairing the spaceship."

#Spaceship Class
@dataclass
class Spaceship:
    name: str
    capacity: int
    astronauts: List[Astronaut] = None  #Composition: spaceship has astronauts

    def __post_init__(self):
        if self.astronauts is None:
            self.astronauts = []

    def add_astronaut(self, astronaut: Astronaut):  #Composition: adding an astronaut
        if len(self.astronauts) >= self.capacity:
            raise ValueError("Spaceship is at full capacity!")
        self.astronauts.append(astronaut)

    def __str__(self) -> str:  #Magic method for string representation
        return f"Spaceship: {self.name}, Capacity: {self.capacity}, Astronauts: {len(self.astronauts)}"






#MissionControlCenter (Singleton)
class MissionControl:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.missions = []
        return cls._instance

    def add_mission(self, mission):  #adding a mission
        self.missions.append(mission)

    def list_missions(self) -> List[str]:  #DRY: 
        return [str(mission) for mission in self.missions]


@dataclass
class Mission:
    name: str
    spaceship: Spaceship 
    #Composition: 
    astronauts: List[Astronaut]  #mission has astronauts
#Polymorphism: 
    def start(self) -> str:  #astronaut performs their task
        tasks = [astronaut.perform_task() for astronaut in self.astronauts]
        return f"Mission {self.name} started!\n" + "\n".join(tasks)

    def __str__(self) -> str:  #Magicmethod for string representation
        return f"Mission: {self.name}, Spaceship: {self.spaceship.name}, Astronauts: {len(self.astronauts)}"

# Factory Method to Create Astronauts
def create_astronaut(role: str, name: str, experience: int) -> Astronaut:
    if role == "Pilot":
        return Pilot(name, experience)
    elif role == "Engineer":
        return Engineer(name, experience)
    else:
        raise ValueError("Invalid astronaut role!")


if __name__ == "__main__":
    #factory method
    pilot = create_astronaut("Pilot", "John", 10)
    engineer = create_astronaut("Engineer", "Alice", 8)

    # Create a spaceship
    spaceship = Spaceship("Galaxy Explorer", capacity=2)
    spaceship.add_astronaut(pilot)
    spaceship.add_astronaut(engineer)

    # Create a mission
    mission = Mission("Mars Landing", spaceship, [pilot, engineer])

  
    print(mission.start())

    #add mission
    mission_control = MissionControl()
    mission_control.add_mission(mission)

    #List  missions
    print("\nMissions in Mission Control:")
    for mission_info in mission_control.list_missions():
        print(mission_info)