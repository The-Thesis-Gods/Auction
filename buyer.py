from feedback import FeedbackSystem
from user import User


class Buyer(User):
    def __init__(self, name, email, password, home_address, phone_number, shipping_address):
        super().__init__(name, email, password, home_address, phone_number)
        self.shipping_address = shipping_address
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

    @staticmethod
    def view_items(items):
        if not items:
            print("No items found.\n")
            return
        for item in items:
            print(f"\nItem ID: {item['item_id']}")
            print(f"   Title: {item['item_title']}")
            print(f"   Current Bid: {item['current_bid']}")
            print(f"   Auto buy Bid: {item['auto_buy_price']}")
            print(f"   Description: {item['item_description']}\n")

    def place_bid(self, item, bid_amount):
        try:
            if bid_amount <= item['current_bid']:
                raise ValueError("Bid amount must be higher than the current bid.\n")

            if item['item_id'] in self.bids:
                previous_bid = self.bids[item['item_id']]
                if bid_amount <= previous_bid:
                    raise ValueError(f"Your new bid must be higher than your previous bid of {previous_bid}.\n")

            min_increment_bid = item['min_increment_bid']
            if bid_amount < item['current_bid'] + min_increment_bid:
                raise ValueError(f"Bid amount must be at least {min_increment_bid} higher than the current bid.\n")

            if bid_amount >= item['auto_buy_price']:
                item['current_bid'] = item['auto_buy_price']
                item['highest_bidder'] = self.email
                self.bids[item['item_id']] = item['auto_buy_price']
                print(f"Congratulations! You've won the item {item['item_title']} "
                      f"with an auto-buy bid of {item['auto_buy_price']}.\n")
            else:
                item['current_bid'] = bid_amount
                item['highest_bidder'] = self.email
                self.bids[item['item_id']] = bid_amount
                print(f"Bid placed on item {item['item_title']} for {bid_amount}.\n")
        except ValueError as e:
            print(e)

    def view_bids(self):
        if not self.bids:
            print("No bids placed yet.\n")
            return
        for item_id, bid_amount in self.bids.items():
            print(f"Item ID: {item_id}, Bid Amount: {bid_amount}\n")

    def view_auction_results(self, items):
        if not items:
            print("No bids found.\n")
            return
        for item in items:
            if item['item_id'] in self.bids:
                if item['highest_bidder'] == self.email:
                    print(f"Congratulations! You won the auction for {item['item_title']} "
                          f"with a bid of {item['current_bid']}.\n")
                else:
                    print(f"You did not win the auction for {item['item_title']}.\n")

    def leave_feedback(self, item, item_id):
        try:
            if item:
                if item['highest_bidder'] == self.email:
                    feedback_system = FeedbackSystem()
                    feedback_system.leave_feedback(item_id, self.email)
                else:
                    print("You can only leave feedback for items you have won.\n")
            else:
                print("Item not found.\n")
        except Exception as e:
            print(f"An error occurred while leaving feedback: {e}\n")
