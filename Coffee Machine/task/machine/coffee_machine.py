#
# supplies = {"water": 400, "milk": 540, "coffee_beans": 120, "cups": 9, "money": 550}
#
# def show_supplies():
#     print(f"The coffee machine has:\n"
#           f"{supplies['water']} of water\n"
#           f"{supplies['milk']} of milk\n"
#           f"{supplies['coffee_beans']} of coffee beans\n"
#           f"{supplies['cups']} of disposable cups\n"
#           f"{supplies['money']} of money")
#
#
# def modify_supplies(water, milk, coffee_beans, cups, money):
#     supplies["water"] += water
#     supplies["milk"] += milk
#     supplies["coffee_beans"] += coffee_beans
#     supplies["cups"] += cups
#     supplies["money"] += money
#
#
# def buy():
#     coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
#     if coffee_type == "1":
#         if is_enough_resources(250, 0, 16, 1):
#             modify_supplies(-250, 0, -16, -1, 4)
#     elif coffee_type == "2":
#         if is_enough_resources(350, 75, 20, 1):
#             modify_supplies(-350, -75, -20, -1, 7)
#     elif coffee_type == "3":
#         if is_enough_resources(200, 100, 12, 1):
#             modify_supplies(-200, -100, -12, -1, 6)
#     else:
#         return
#
#
# def fill():
#     water = int(input("Write how many ml of water do you want to add:"))
#     milk = int(input("Write how many ml of milk do you want to add:"))
#     coffee_beans = int(input("Write how many ml of coffee_beans do you want to add:"))
#     cups = int(input("Write how many ml of disposable cups do you want to add:"))
#     modify_supplies(water, milk, coffee_beans, cups, 0)
#
#
# def take():
#     print(f"I gave you {supplies['money']} {'$'}")
#     supplies["money"] = 0
#
#
# def is_enough_resources(water, milk, coffee_beans, cups):
#     if supplies["water"] <= water:
#         print("Sorry, not enough water!")
#         return False
#     elif supplies["milk"] <= milk:
#         print("Sorry, not enough milk!")
#         return False
#     elif supplies["coffee_beans"] <= coffee_beans:
#         print("Sorry, not enough coffee beans!")
#         return False
#     elif supplies["cups"] <= cups:
#         print("Sorry, not enough disposable cups!")
#         return False
#     else:
#         print("I have enough resources, making you a coffee!")
#         return True
#
# while True:
#     action = input("Write action (buy, fill, take, remaining, exit):")
#     if action == "remaining":
#         show_supplies()
#     elif action == "buy":
#         buy()
#     elif action == "fill":
#         fill()
#     elif action == "take":
#         take()
#     else:
#         break


class CoffeeMachine:
    FILLING_STATES = ["filling water", "filling milk", "filling coffee beans", "filling cups"]
    COFFEE_SUPPLIES = {"espresso": {"water": 250, "milk": 0, "coffee_beans": 16, "cups": 1, "money": 4},
                       "latte": {"water": 350, "milk": 75, "coffee_beans": 20, "cups": 1, "money": 7},
                       "cappuccino": {"water": 200, "milk": 100, "coffee_beans": 12, "cups": 1, "money": 6}}

    def __init__(self):
        self.state = ""
        self.supplies = {"water": 400, "milk": 540, "coffee_beans": 120, "cups": 9, "money": 550}
        self.write_action()

    def write_action(self):
        self.state = "choosing an action"
        print("Write action (buy, fill, take, remaining, exit):")

    def show_supplies(self):
        print(f"The coffee machine has:\n"
              f"{self.supplies['water']} of water\n"
              f"{self.supplies['milk']} of milk\n"
              f"{self.supplies['coffee_beans']} of coffee beans\n"
              f"{self.supplies['cups']} of disposable cups\n"
              f"{self.supplies['money']} of money")
        self.write_action()

    def modify_supplies(self, coffee_supplies):
        self.supplies["water"] += coffee_supplies["water"]
        self.supplies["milk"] += coffee_supplies["milk"]
        self.supplies["coffee_beans"] += coffee_supplies["coffee_beans"]
        self.supplies["cups"] += coffee_supplies["cups"]
        self.supplies["money"] += coffee_supplies["money"]

    def is_enough_resources(self, ingredients):
        if self.supplies["water"] <= ingredients["water"]:
            print("Sorry, not enough water!")
            self.write_action()
            return False
        elif self.supplies["milk"] <= ingredients["milk"]:
            print("Sorry, not enough milk!")
            self.write_action()
            return False
        elif self.supplies["coffee_beans"] <= ingredients["coffee_beans"]:
            print("Sorry, not enough coffee beans!")
            self.write_action()
            return False
        elif self.supplies["cups"] <= ingredients["cups"]:
            print("Sorry, not enough disposable cups!")
            self.write_action()
            return False
        else:
            print("I have enough resources, making you a coffee!")
            self.write_action()
            return True

    def buy(self, coffee_type):
        if coffee_type == "1":
            if self.is_enough_resources(CoffeeMachine.COFFEE_SUPPLIES["espresso"]):
                self.modify_supplies(CoffeeMachine.COFFEE_SUPPLIES["espresso"])
        elif coffee_type == "2":
            if self.is_enough_resources(CoffeeMachine.COFFEE_SUPPLIES["latte"]):
                self.modify_supplies(CoffeeMachine.COFFEE_SUPPLIES["latte"])
        elif coffee_type == "3":
            if self.is_enough_resources(CoffeeMachine.COFFEE_SUPPLIES["cappuccino"]):
                self.modify_supplies(CoffeeMachine.COFFEE_SUPPLIES["cappuccino"])
        else:
            self.write_action()

    def fill(self, amount):
        if self.state == "filling water":
            self.modify_supplies(amount, 0, 0, 0, 0)
            self.state = "filling milk"
            print("Write how many ml of milk do you want to add:")
        elif self.state == "filling milk":
            self.modify_supplies(0, amount, 0, 0, 0)
            self.state = "filling coffee beans"
            print("Write how many ml of coffee_beans do you want to add:")
        elif self.state == "filling coffee beans":
            self.modify_supplies(0, 0, amount, 0, 0)
            self.state = "filling cups"
            print("Write how many disposable cups of coffee do you want to add:")
        elif self.state == "filling cups":
            self.modify_supplies(0, 0, 0, amount, 0)
            self.write_action()

    def take(self):
        print(f"I gave you {self.supplies['money']} {'$'}")
        self.supplies["money"] = 0
        self.write_action()

    def action(self, users_input):
        if users_input == "remaining":
            self.show_supplies()
        elif users_input == "buy":
            self.state = "choosing a type of coffee"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif users_input == "fill":
            self.state = "filling water"
            print("Write how many ml of water do you want to add:")
        elif users_input == "take":
            self.take()
        else:
            self.state = "exit"

    def input(self, users_input):
        if self.state == "choosing an action":
            self.action(users_input)
        elif self.state == "choosing a type of coffee":
            self.buy(users_input)
        elif self.state in CoffeeMachine.FILLING_STATES:
            self.fill(int(users_input))


def main():
    cm = CoffeeMachine()
    while cm.state != "exit":
        cm.input(input())


if __name__ == "__main__":
    main()
