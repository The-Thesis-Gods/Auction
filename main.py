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
            print("Thank you for visiting the online marketplace. Goodbye!")
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

        if isinstance(user, customer.Buyer):
            buyer_actions()
        elif isinstance(user, merchant.Seller):
            seller_actions()
    else:
        print("Invalid email or password. Please try again.")


def buyer_actions():
    while True:
        buyer_menu()
        break


def seller_actions():
    while True:
        seller_menu()
        break


def buyer_menu():
    print("1. View items")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Log out")
    print("Please enter a number to select an option:")


def seller_menu():
    print("1. View items")
    print("2. Add item")
    print("3. Edit item")
    print("4. Delete item")
    print("5. Log out")
    print("Please enter a number to select an option:")


if __name__ == '__main__':
    main()
