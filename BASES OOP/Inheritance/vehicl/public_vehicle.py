from transport import Transport

class PublicVehicle(Transport):
    def __init__(self, is_motorized=True, speed=0, max_distance=1000):
        super().__init__(is_motorized, speed, max_distance)
        self.__current_riders = 0
    def board_riders(self, num):
        self.__current_riders += num
    def disembark_riders(self, num):
        self.__current_riders -= num
    def get_rider_count(self):
        return self.__current_riders