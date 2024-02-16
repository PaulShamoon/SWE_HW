import random

class TreasureChest:
    def __init__(self):
        self.items = []

    def populate(self, num_items):
        self.items = list(range(1, num_items + 1))
        random.shuffle(self.items)

    def grab_item(self):
        if self.items:
            return self.items.pop()
        else:
            return None

class Bank:
    def __init__(self, initial_funds):
        self.funds = initial_funds

    def deposit(self, amount):
        self.funds += amount

    def withdraw(self, amount):
        if self.funds >= amount:
            self.funds -= amount
            return amount
        else:
            return 0

def play_game():
    # Set up initial values
    bank = Bank(100)  # Starting funds
    wager = 5  # Wager per grab

    print("Welcome to the Treasure Chest Game of Chance!")
    print(f"You have ${bank.funds} in your bank account.")

    # Prompt the user to populate the treasure chest
    num_items = int(input("How many items do you want to put in the treasure chest? "))
    chest = TreasureChest()
    chest.populate(num_items)
    print(f"The treasure chest has been populated with {num_items} items.")

    print(f"Each grab from the treasure chest costs ${wager}.")

    # Play the game loop
    while bank.funds >= wager:
        input("Press Enter to grab an item from the treasure chest...")
        grabbed_item = chest.grab_item()
        if grabbed_item is not None:
            print(f"You grabbed item {grabbed_item} from the treasure chest!")
            bank.withdraw(wager)  # Deduct the wager amount
            bank.deposit(grabbed_item)
            print(f"Your bank account balance is now ${bank.funds}.")
        else:
            print("The treasure chest is empty!")
            break

    # Game over message
    print("Game over! You can no longer afford to play.")

if __name__ == "__main__":
    play_game()
