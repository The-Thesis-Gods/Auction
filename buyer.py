from user import User


class Buyer(User):
    def __init__(self, name, email, password, home_address, phone_number, shipping_address):
        super().__init__(name, email, password, home_address, phone_number)
        self.shipping_address = shipping_address

    def account_creation(self):
        super().account_creation()
        self.shipping_address = input("Please enter your shipping address: ")
