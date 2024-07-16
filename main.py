import buyer as customer
import seller as merchant
#from feedback import FeedbackSystem

users = {}  # Global dictionary to store users
#feedback_system = FeedbackSystem()  # Global feedback system

def main():
    # Add admin users
    admin_seller = merchant.Seller("Seller Admin", "seller@email.com", "1234", "", "", "", "")
    users[admin_seller.email] = admin_seller

    admin_buyer = customer.Buyer("Buyer Admin", "buyer@email.com", "1234", "", "", "")
    users[admin_buyer.email] = admin_buyer

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
    print("Please enter a number to select an option:", end=" ")


def create_account():
    print("Are you a buyer or a seller?")
    print("1. Buyer")
    print("2. Seller")
    user_input = input("Enter your choice (1 or 2): ")
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
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    user = users.get(email)
    if user and user.get_password() == password:
        print(f"Welcome back, {user.name}!")

        if isinstance(user, customer.Buyer):
            buyer_actions(user)
        elif isinstance(user, merchant.Seller):
            seller_actions(user)
    else:
        print("Invalid email or password. Please try again.")


def buyer_actions(buyer):
    while True:
        buyer_menu()
        choice = input()
        if choice == "1":
            items = get_all_items()
            buyer.view_items(items)
        elif choice == "2":
            item_id = input("Enter the item ID to place a bid: ")
            item = find_item_by_id(item_id)
            if item:
                bid_amount = float(input(f"Enter your bid amount (current bid is {item['current_bid']}): "))
                buyer.place_bid(item, bid_amount)
            else:
                print("Item not found.")
        elif choice == "3":
            buyer.view_bids()
        elif choice == "4":
            items = get_all_items()
            buyer.view_auction_results(items)
        elif choice == "5":
            buyer.leave_feedback()
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid input. Please try again.")


def seller_actions(seller):
    while True:
        print("1. List an item for auction")
        print("2. View your listed items")
        print("3. Edit a listed item")
        print("4. Remove a listed item")
        print("5. View auction results for your items")
        print("6. Leave feedback")
        print("7. Log out")
        choice = input("Please enter a number to select an option: ")
        
        if choice == '1':
            seller.list_item()
        elif choice == '2':
            seller.view_items()
        elif choice == '3':
            seller.edit_item()
        elif choice == '4':
            seller.remove_item()
        elif choice == '5':
            seller.view_auction_results()
        #elif choice == '6':
           #seller.leave_feedback(feedback_system)
        elif choice == '7':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def buyer_menu():
    print("1. View items")
    print("2. Place a bid")
    print("3. View your bids")
    print("4. View auction results")
    print("5. Leave feedback")
    print("6. Log out")
    print("Please enter a number to select an option:", end=" ")


def seller_menu():
    print("1. List an item for auction")
    print("2. View your listed items")
    print("3. Edit a listed item")
    print("4. Remove a listed item")
    print("5. View auction results for your items")
    print("6. Leave feedback")
    print("7. Log out")
    print("Please enter a number to select an option:", end=" ")


def get_all_items():
    all_items = []
    for user in users.values():
        if isinstance(user, merchant.Seller):
            all_items.extend(user.items)
    return all_items


def find_item_by_id(item_id):
    for item in get_all_items():
        if item['item_id'] == item_id:
            return item
    return None


if __name__ == '__main__':
    main()
