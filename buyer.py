# buyer.py

from user import User

class Buyer(User):
    def __init__(self, name, email, password, home_address, phone_number, shipping_address):
        super().__init__(name, email, password, home_address, phone_number)
        self.shipping_address = shipping_address
        self.cart = []
        self.bids = {}

    def account_creation(self):
        super().account_creation()
        while True:
            try:
                self.shipping_address = input("Please enter your shipping address: ")
                if not self.shipping_address:
                    raise ValueError("Shipping address cannot be empty.")
                break
            except ValueError as e:
                print(e)

    def view_items(self, items):
        for item in items:
            print(f"Item ID: {item['item_id']}, Title: {item['item_title']}, Current Bid: {item['current_bid']}")

    def add_to_cart(self, item):
        self.cart.append(item)
        print(f"Item {item['item_title']} added to cart.")

    def remove_from_cart(self, item_id):
        for item in self.cart:
            if item['item_id'] == item_id:
                self.cart.remove(item)
                print(f"Item {item['item_title']} removed from cart.")
                return
        print("Item not found in cart.")

    def view_cart(self):
        for item in self.cart:
            print(f"Item ID: {item['item_id']}, Title: {item['item_title']}, Current Bid: {item['current_bid']}")

    def place_bid(self, item, bid_amount):
        if bid_amount <= item['current_bid']:
            print("Bid amount must be higher than the current bid.")
            return
        item['current_bid'] = bid_amount
        item['highest_bidder'] = self.email
        self.bids[item['item_id']] = bid_amount
        print(f"Bid placed on item {item['item_title']} for {bid_amount}.")

    def checkout(self):
        for item in self.cart:
            if item['highest_bidder'] == self.email:
                print(f"Proceeding to transaction for item {item['item_title']} at {item['current_bid']}.")
            else:
                print(f"Cannot proceed with transaction. You are not the highest bidder for item {item['item_title']}.")
