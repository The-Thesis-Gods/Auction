class User:
    def __init__(self, name, email, password, home_address, phone_number):
        self.name = name
        self.email = email
        self.password = password
        self.home_address = home_address
        self.phone_number = phone_number

    def account_creation(self):
        self.name = input("Enter your name: ")
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")
        self.home_address = input("Enter your home address: ")
        self.phone_number = input("Enter your phone number: ")

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
        self.set_bank_account(input("Please enter your bank account number: "))
        self.set_routing_number(input("Please enter your routing number: "))

    def list_item(self):
        item_id = input("Enter item ID: ")
        item_title = input("Enter item title: ")
        item_description = input("Enter item description: ")
        starting_price = float(input("Enter starting price: "))
        min_increment_bid = float(input("Enter minimum increment bid: "))
        auto_buy_price = float(input("Enter auto buy price: "))
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
