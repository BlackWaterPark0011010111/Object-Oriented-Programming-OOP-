class AquariumApp:
    def __init__(self, name, fish_count):
        self.name = name
        self.fish_count = fish_count
    def add_fish(self, count):
        self.fish_count += count
        print(f"Added {count} fish. Total fish: {self.fish_count}")
    def remove_fish(self, count):
        if self.fish_count >= count:
            self.fish_count -= count
            print(f"Removed {count} fish. Total fish: {self.fish_count}")
        else:
            print("Not enough fish to remove.")
    def show_aquarium_info(self):
        print(f"Aquarium '{self.name}' has {self.fish_count} fish.")

def main():
    aquarium = AquariumApp("Ocean World", 10)
    aquarium.show_aquarium_info()
    aquarium.add_fish(5)
    aquarium.remove_fish(3)
    aquarium.show_aquarium_info()

if __name__ == "__main__":
    main()
