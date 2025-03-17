from transport import Transport

class Bicycle(Transport):
    def __init__(self, is_motorized=False, speed=20, max_distance=600):
        super().__init__(is_motorized, speed, max_distance)
        self._repair_mileage = 200
    def repair(self):
        self._repair_mileage = 200
    def travel(self, km):
        if self._repair_mileage > 0:
            self._repair_mileage -= km
            return super().travel(km)
        return False