class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money

    def get_report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Money: ${self.money}")
        
    def turn_off(self):
        print("Turning off the coffee machine.")
        
    def check_resources(self, water_needed, milk_needed, beans_needed):
        if self.water < water_needed:
            print("Not enough water!")
            return False
        if self.milk < milk_needed:
            print("Not enough milk!")
            return False
        if self.coffee_beans < beans_needed:
            print("Not enough coffee beans!")
            return False
        return True
        
    def make_coffee(self, coffee_type, cost, water_needed, milk_needed, beans_needed):
        if self.check_resources(water_needed, milk_needed, beans_needed):
            print(f"Making {coffee_type}...")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= beans_needed
            self.money += cost
            print(f"{coffee_type} is ready! Enjoy!")
        else:
            print(f"Sorry, we can't make {coffee_type}.")

    def insert_coins(self):
        coins = float(input("Insert coins: $"))
        return coins
    
    def check_transaction(self, cost):
        coins_inserted = self.insert_coins()
        if coins_inserted < cost:
            print("Not enough money. Please insert more.")
            return False
        else:
            self.give_change(coins_inserted, cost)
            return True
        
    def give_change(self, coins_inserted, cost):
        change = coins_inserted - cost
        if change > 0:
            print(f"Here is ${change} in change.")
        
    def serve_coffee(self, coffee_type):
        if coffee_type == "espresso":
            self.make_coffee("Espresso", 1.5, 50, 0, 18)
        elif coffee_type == "latte":
            self.make_coffee("Latte", 2.5, 200, 150, 24)
        elif coffee_type == "cappuccino":
            self.make_coffee("Cappuccino", 3.0, 250, 100, 24)
    
    def check_resource_alert(self):
        if self.water < 50:
            print("Warning: Water is low!")
        if self.milk < 50:
            print("Warning: Milk is low!")
        if self.coffee_beans < 10:
            print("Warning: Coffee beans are low!")


def main():
    coffee_machine = CoffeeMachine(1000, 1000, 100, 0)
    
    while True:
        coffee_machine.check_resource_alert()
        choice = input("What would you like? (espresso/latte/cappuccino/off/report): ")
        
        if choice == "off":
            coffee_machine.turn_off()
            break
        elif choice == "report":
            coffee_machine.get_report()
        elif choice in ["espresso", "latte", "cappuccino"]:
            if coffee_machine.check_transaction(1.5 if choice == "espresso" else 2.5 if choice == "latte" else 3.0):
                coffee_machine.serve_coffee(choice)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()