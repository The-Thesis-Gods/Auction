import uuid


class User:
    def __init__(self, name, email, password, home_address, phone_number):
        self.member_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.__password = password
        self.home_address = home_address
        self.phone_number = phone_number

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def account_creation(self):
        self.name = input("Please enter your name: ")
        self.email = input("Please enter your email: ")
        self.set_password(input("Please enter your password: "))
        self.home_address = input("Please enter your home address: ")
        self.phone_number = input("Please enter your phone number: ")
