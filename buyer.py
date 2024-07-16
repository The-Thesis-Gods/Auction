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

    def view_items(self, items):
        if not items:
            print("No items found.")
            return
        for item in items:
            print(f"Item ID: {item['item_id']}")
            print(f"Title: {item['item_title']}")
            print(f"Current Bid: {item['current_bid']}")
            print(f"Auto buy Bid: {item['auto_buy_price']}")
            print(f"Description: {item['item_description']}")

    def place_bid(self, item, bid_amount):
        if bid_amount <= item['current_bid']:
            print("Bid amount must be higher than the current bid.")
            return

        if item['item_id'] in self.bids:
            previous_bid = self.bids[item['item_id']]
            if bid_amount <= previous_bid:
                print(f"Your new bid must be higher than your previous bid of {previous_bid}.")
                return

        min_increment_bid = item['min_increment_bid']
        if bid_amount < item['current_bid'] + min_increment_bid:
            print(f"Bid amount must be at least {min_increment_bid} higher than the current bid.")
            return

        if bid_amount >= item['auto_buy_price']:
            item['current_bid'] = item['auto_buy_price']
            item['highest_bidder'] = self.email
            self.bids[item['item_id']] = item['auto_buy_price']
            print(f"Congratulations! You've won the item {item['item_title']} with an auto-buy bid of {item['auto_buy_price']}.")
        else:
            item['current_bid'] = bid_amount
            item['highest_bidder'] = self.email
            self.bids[item['item_id']] = bid_amount
            print(f"Bid placed on item {item['item_title']} for {bid_amount}.")

    def view_bids(self):
        if not self.bids:
            print("No bids placed yet.")
            return
        for item_id, bid_amount in self.bids.items():
            print(f"Item ID: {item_id}, Bid Amount: {bid_amount}")

    def view_auction_results(self, items):
        if not items:
            print("No bids found.")
            return
        for item in items:
            if item['item_id'] in self.bids:
                if item['highest_bidder'] == self.email:
                    print(f"Congratulations! You won the auction for {item['item_title']} with a bid of {item['current_bid']}.")
                else:
                    print(f"You did not win the auction for {item['item_title']}.")

    @staticmethod
    def leave_feedback():
        item_id = input("Enter the item ID for which you want to leave feedback: ")
        feedback = input("Enter your feedback: ")
        print(f"Feedback for item {item_id}: {feedback}")
