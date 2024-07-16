from user import User
from feedback import FeedbackSystem
import re
import random


class Seller(User):
    def __init__(self, name, email, password, home_address, phone_number, bank_account, routing_number):
        super().__init__(name, email, password, home_address, phone_number)
        self.__bank_account = bank_account
        self.__routing_number = routing_number
        self.items = []

    def get_bank_account(self):
        return self.__bank_account

    def set_bank_account(self, bank_account):
        self.__bank_account = bank_account

    def get_routing_number(self):
        return self.__routing_number

    def set_routing_number(self, routing_number):
        self.__routing_number = routing_number

    def account_creation(self):
        super().account_creation()
        while True:
            try:
                bank_account = input("Please enter your bank account number: ")
                if not re.match(r"^\d+$", bank_account):
                    raise ValueError("Invalid bank account number. Please enter digits only.")
                self.set_bank_account(bank_account)
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                routing_number = input("Please enter your routing number: ")
                if not re.match(r"^\d+$", routing_number):
                    raise ValueError("Invalid routing number. Please enter digits only.")
                self.set_routing_number(routing_number)
                break
            except ValueError as e:
                print(e)

    def generate_unique_item_id(self):
        while True:
            item_id = '{:04d}'.format(random.randint(0, 9999))
            if not any(item['item_id'] == item_id for item in self.items):
                return item_id

    def list_item(self):
        try:
            item_id = self.generate_unique_item_id()
            item_title = input("\nEnter item title: ")
            item_description = input("Enter item description: ")
            starting_price = float(input("Enter starting bid price: "))
            min_increment_bid = float(input("Enter minimum increment bid: "))
            auto_buy_price = float(input("Enter auto buy price (maximum bid): "))
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")

            item = {
                "item_id": item_id,
                "item_title": item_title,
                "item_description": item_description,
                "starting_price": starting_price,
                "min_increment_bid": min_increment_bid,
                "auto_buy_price": auto_buy_price,
                "start_date": start_date,
                "end_date": end_date,
                "current_bid": starting_price,
                "highest_bidder": None
            }

            self.items.append(item)
            print("Item listed successfully!\n")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def view_items(self):
        if not self.items:
            print("No items listed.\n")
            return
        for item in self.items:
            print(f"\nID: {item['item_id']}\n   Title: {item['item_title']}\n"
                  f"   Description: {item['item_description']} "
                  f"\n   Starting Price: {item['starting_price']}\n"
                  f"   Current Bid: {item['current_bid']}, "
                  f"\n   Highest Bidder: {item['highest_bidder']}\n"
                  f"   Start Date: {item['start_date']}\n   End Date: {item['end_date']}\n")

    def edit_item(self):
        try:
            item_id = input("\nEnter the item ID of the item you want to edit: ")
            item = next((item for item in self.items if item['item_id'] == item_id), None)
            if not item:
                print("Item not found.\n")
                return

            item['item_title'] = input("Enter new item title: ")
            item['item_description'] = input("Enter new item description: ")
            item['starting_price'] = float(input("Enter new starting price: "))
            item['min_increment_bid'] = float(input("Enter new minimum increment bid: "))
            item['auto_buy_price'] = float(input("Enter new auto buy price: "))
            item['start_date'] = input("Enter new start date (YYYY-MM-DD): ")
            item['end_date'] = input("Enter new end date (YYYY-MM-DD): ")
            print("Item updated successfully!\n")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def remove_item(self):
        try:
            item_id = input("Enter the item ID of the item you want to remove: ")
            item = next((item for item in self.items if item['item_id'] == item_id), None)
            if not item:
                print("Item not found.\n")
                return

            self.items.remove(item)
            print("Item removed successfully!\n")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def view_auction_results(self):
        if not self.items:
            print("No items found.\n")
            return
        for item in self.items:
            print(f"\nID: {item['item_id']}\n   Title: {item['item_title']}\n"
                  f"   Highest Bid: {item['current_bid']}\n"
                  f"   Highest Bidder: {item['highest_bidder']}\n")

    def leave_feedback(self):
        try:
            item_id = input("\nEnter the item ID for which you want to leave feedback: ")
            item = next((item for item in self.items if item['item_id'] == item_id), None)
            if item:
                feedback_system = FeedbackSystem()
                feedback_system.leave_feedback(item_id, self.email)
            else:
                print("Item not found.\n")
        except Exception as e:
            print(f"An error occurred while leaving feedback: {e}\n")
