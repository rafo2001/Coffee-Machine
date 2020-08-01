# Write your code here
class CoffeeMachine:
    menu = {"espresso": {"water": 250, "coffee beans": 16, "disposable cups": 1, "money": -4},
            "latte": {"water": 350, "milk": 75, "coffee beans": 20, "disposable cups": 1, "money": -7},
            "cappuccino": {"water": 200, "milk": 100, "coffee beans": 12, "disposable cups": 1, "money": -6}}
    supplies = {}
    status = None
    index_supplies = 0
    order = None
    item = None
    cant = 0
    items = []
    # Como emulo un unum??

    def __init__(self):
        self.supplies = {"water": 400, "milk": 540, "coffee beans": 120, "disposable cups": 9, "money": 550}
        self.status = 0  # Idle
        self.index_supplies = 0
        self.print_message()

    def get_action(self, action):
        if self.status == 0:
            if action == "buy":
                self.status = 1
            elif action == "fill":
                self.index_supplies = 0
                self.status = 2
            elif action == "take":
                self.action_take()
            elif action == "remaining":
                self.print_status()
            elif action == "exit":
                return False
            else:
                print("INVALID ACTION")
        elif self.status == 1:
            if action == 'back':
                self.order = action
                self.action_buy()
            else:
                self.order = self.items[int(action) - 1]
                self.action_buy()
        elif self.status == 2:
            self.cant = int(action)
            self.action_fill()
        self.print_message()
        return True

    def print_message(self):
        print()
        if self.status == 0:
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.status == 1:  # Selling
            self.print_menu()
        elif self.status == 2:  # Filling
            self.fill_item()

    def print_menu(self):
        print("What do you want to buy?", end="")
        self.items = []
        items_list = []
        i = 1
        for item in self.menu:
            self.items.append(item)
            items_list.append(" " + str(i) + " - " + item)
            i += 1
        print(','.join(items_list), end="")
        print(", back - to main menu:")

    def print_status(self):
        print()
        print("The coffee machine has:")
        for item, cant in self.supplies.items():
            print(f"{cant} of {item}")

    def action_take(self):
        amount = self.supplies.get("money")
        print()
        print(f"I gave you ${amount}")
        self.supplies["money"] = 0

    def action_fill(self):
        self.supplies[self.item] += self.cant
        if self.index_supplies >= len(self.supplies) - 1:
            self.status = 0

    def fill_item(self):
        index_item = 0
        for item in self.supplies:
            if index_item == self.index_supplies:
                cur_item = item
                if cur_item != "money":
                    self.item = cur_item
                    print(f"Write how many {cur_item} do you want to add:")
            index_item += 1
        self.index_supplies += 1

    def chek_items(self):
        ingredients = self.menu.get(self.order)
        for item in ingredients:
            if self.supplies[item] < ingredients.get(item):
                return item
        return None

    def action_buy(self):
        order = self.order
        if order == "back":
            self.status = 0
            return None
        item = self.chek_items()
        if item is not None:
            print(f"Sorry, not enough {item}!")
            self.status = 0
            return None
        print("I have enough resources, making you a coffee!")
        self.prepare_order()
        self.status = 0

    def prepare_order(self):
        ingredients = self.menu.get(self.order)
        for item in ingredients:
            self.supplies[item] -= ingredients.get(item)


mi_cafetera = CoffeeMachine()
while True:
    if not mi_cafetera.get_action(input()):
        break


