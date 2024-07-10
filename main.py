import buyer as customer
import seller as merchant
users = {}  # Global dictionary to store users


def main():
    print("Welcome to the online marketplace!")
    while True:
        main_menu()
        user_input = input()
        if user_input == "1":
            create_account()
        elif user_input == "2":
            login()
        elif user_input == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


def main_menu():
    print("1. Create an account")
    print("2. Log in")
    print("3. Exit")
    print("Please enter a number to select an option:")


def create_account():
    print("Are you a buyer or a seller?")
    print("1. Buyer")
    print("2. Seller")
    user_input = input()
    if user_input == "1":
        buyer = customer.Buyer("", "", "", "", "", "")
        buyer.account_creation()
        users[buyer.email] = buyer
        print("Buyer account created successfully!")
    elif user_input == "2":
        seller = merchant.Seller("", "", "", "", "", "", "")
        seller.account_creation()
        users[seller.email] = seller
        print("Seller account created successfully!")
    else:
        print("Invalid input. Please try again.")


def login():
    print("Please enter your email:")
    email = input()
    print("Please enter your password:")
    password = input()
    user = users.get(email)
    if user and user.get_password() == password:
        print(f"Welcome back, {user.name}!")
    else:
        print("Invalid email or password. Please try again.")


if __name__ == '__main__':
    main()
