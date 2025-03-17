from public_vehicle import PublicVehicle
from bicycle import Bicycle
class BikeCab(PublicVehicle, Bicycle):
    def __init__(self, is_motorized=False):
        speed = 30 if is_motorized else 18
        max_distance = 600
        super().__init__(is_motorized=is_motorized, speed=speed, max_distance=max_distance)
        self.max_riders = 4 if is_motorized else 2

    def board_riders(self, num):
        if num <= self.max_riders:
            super().board_riders(num)
        else:
            print("Cannot board more riders at this time.")