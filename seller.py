import user


class Seller(user):
    def __init__(self, name, email, password, home_address, phone_number, bank_account, routing_number):
        super().__init__(name, email, password, home_address, phone_number)
        self.__bank_account = bank_account
        self.__routing_number = routing_number

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
