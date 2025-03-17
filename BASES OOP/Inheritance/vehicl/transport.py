class Transport:
    def __init__(self, is_motorized=False, speed=0, max_distance=1000):
        self.is_motorized = is_motorized
        self.speed = speed
        self.max_distance = max_distance
        self.__is_scrap = False
        print("Ready to roll!")

    def travel(self, km):
        if not self.__is_scrap:
            print(f"Travelling {km} km.")
            self.max_distance -= km
            if self.max_distance < 0:
                self.__is_scrap = True
                return False
            return True
        return False