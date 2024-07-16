from user import User
import re
import uuid


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
            item_id = str(uuid.uuid4())
            if not any(item['item_id'] == item_id for item in self.items):
                return item_id

    def list_item(self):
        item_id = self.generate_unique_item_id()
        item_title = input("Enter item title: ")
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
        print("Item listed successfully!")

    def view_items(self):
        if not self.items:
            print("No items listed.")
            return
        for item in self.items:
            print(f"ID: {item['item_id']}, Title: {item['item_title']}, "
                  f"Description: {item['item_description']}, "
                  f"Starting Price: {item['starting_price']}, "
                  f"Current Bid: {item['current_bid']}, "
                  f"Highest Bidder: {item['highest_bidder']}, "
                  f"Start Date: {item['start_date']}, "
                  f"End Date: {item['end_date']}")

    def edit_item(self):
        item_id = input("Enter the item ID of the item you want to edit: ")
        for item in self.items:
            if item['item_id'] == item_id:
                item['item_title'] = input("Enter new item title: ")
                item['item_description'] = input("Enter new item description: ")
                item['starting_price'] = float(input("Enter new starting price: "))
                item['min_increment_bid'] = float(input("Enter new minimum increment bid: "))
                item['auto_buy_price'] = float(input("Enter new auto buy price: "))
                item['start_date'] = input("Enter new start date (YYYY-MM-DD): ")
                item['end_date'] = input("Enter new end date (YYYY-MM-DD): ")
                print("Item updated successfully!")
                return
        print("Item not found.")

    def remove_item(self):
        item_id = input("Enter the item ID of the item you want to remove: ")
        for item in self.items:
            if item['item_id'] == item_id:
                self.items.remove(item)
                print("Item removed successfully!")
                return
        print("Item not found.")

    def view_auction_results(self):
        for item in self.items:
            print(f"ID: {item['item_id']}, Title: {item['item_title']}, Highest Bid: {item['current_bid']}, "
                  f"Highest Bidder: {item['highest_bidder']}")

    def leave_feedback(self, feedback_system):
        feedback_system.leave_feedback(self.email)
