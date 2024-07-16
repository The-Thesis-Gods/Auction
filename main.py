import buyer as customer
import seller as merchant

from feedback import FeedbackSystem

feedback_system = FeedbackSystem()  # Global feedback system

users = {}  # Global dictionary to store users


def main():
    # Add admin users
    admin_seller = merchant.Seller("Seller Admin", "seller@email.com", "1234", "", "", "", "")
    users[admin_seller.email] = admin_seller

    admin_buyer = customer.Buyer("Buyer Admin", "buyer@email.com", "1234", "", "", "")
    users[admin_buyer.email] = admin_buyer

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
            print("Invalid input. Please try again.\n")


def main_menu():
    print("\nWelcome to the online marketplace!")
    print("1. Create an account")
    print("2. Log in")
    print("3. Exit")
    print("Please enter a number to select an option:", end=" ")


def create_account():
    print("\nAre you a buyer or a seller?")
    print("1. Buyer")
    print("2. Seller")
    user_input = input("Enter your choice (1 or 2): ").strip()
    if user_input == "1":
        buyer = customer.Buyer("", "", "", "", "", "")
        try:
            buyer.account_creation()
            users[buyer.email] = buyer
            print("Buyer account created successfully!\n")
        except Exception as e:
            print(f"Failed to create buyer account: {e}\n")
    elif user_input == "2":
        seller = merchant.Seller("", "", "", "", "", "", "")
        try:
            seller.account_creation()
            users[seller.email] = seller
            print("Seller account created successfully!\n")
        except Exception as e:
            print(f"Failed to create seller account: {e}\n")
    else:
        print("Invalid input. Please try again.\n")


def login():
    email = input("\nPlease enter your email: ").strip()
    password = input("Please enter your password: ").strip()
    user = users.get(email)
    if user and user.get_password() == password:
        print(f"\nWelcome back, {user.name}!")
        try:
            if isinstance(user, customer.Buyer):
                buyer_actions(user)
            elif isinstance(user, merchant.Seller):
                seller_actions(user)
        except Exception as e:
            print(f"Error during user session: {e}\n")
    else:
        print("Invalid email or password. Please try again.\n")


def buyer_actions(buyer):
    while True:
        buyer_menu()
        choice = input().strip()
        if choice == "1":
            items = get_all_items()
            buyer.view_items(items)
        elif choice == "2":
            item_id = input("Enter the item ID to place a bid: ").strip()
            item = find_item_by_id(item_id)
            if item:
                try:
                    bid_amount = float(input(f"Enter your bid amount (current bid is {item['current_bid']}): "))
                    buyer.place_bid(item, bid_amount)
                except ValueError:
                    print("Invalid bid amount. Please enter a valid number.\n")
            else:
                print("Item not found.\n")
        elif choice == "3":
            buyer.view_bids()
        elif choice == "4":
            items = get_buyer_items(buyer)
            buyer.view_auction_results(items)
        elif choice == "5":
            item_id = input("\nEnter the item ID for which you want to leave feedback: ").strip()
            item = find_item_by_id(item_id)
            buyer.leave_feedback(item, item_id)
        elif choice == "6":
            print("Logging out...\n")
            break
        else:
            print("Invalid input. Please try again.\n")


def seller_actions(seller):
    while True:
        seller_menu()
        choice = input().strip()
        if choice == "1":
            seller.list_item()
        elif choice == "2":
            seller.view_items()
        elif choice == "3":
            seller.edit_item()
        elif choice == "4":
            seller.remove_item()
        elif choice == "5":
            seller.view_auction_results()
        elif choice == "6":
            seller.leave_feedback()
        elif choice == "7":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Please try again.\n")


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


def get_buyer_items(buyer):
    all_items = get_all_items()
    buyer_items = [item for item in all_items if item['item_id'] in buyer.bids]
    return buyer_items


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
