import uuid
import re


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
        while True:
            try:
                self.name = input("\nPlease enter your name: ")
                if not self.name:
                    raise ValueError("Name cannot be empty.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.email = input("Please enter your email: ")
                if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
                    raise ValueError("Invalid email format.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                password = input("Please enter your password: ")
                if len(password) < 8:
                    raise ValueError("Password must be at least 8 characters long.")
                self.set_password(password)
                if not self.get_password():
                    raise ValueError("Password cannot be empty.")
                if not any(char.isdigit() for char in self.get_password()):
                    raise ValueError("Password must contain at least one digit.")
                if not any(char.isupper() for char in self.get_password()):
                    raise ValueError("Password must contain at least one uppercase letter.")
                if not any(char.islower() for char in self.get_password()):
                    raise ValueError("Password must contain at least one lowercase letter.")
                if not any(char in "!@#$%^&*()-+" for char in self.get_password()):
                    raise ValueError("Password must contain at least one special character.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.home_address = input("Please enter your home address: ")
                if not self.home_address:
                    raise ValueError("Home address cannot be empty.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.phone_number = input("Please enter your phone number: ")
                if not self.phone_number.isdigit():
                    raise ValueError("Must input numbers only.")
                if len(self.phone_number) != 11:
                    raise ValueError("Phone number must be 11 digits long.")
                break
            except ValueError as e:
                print(e)
