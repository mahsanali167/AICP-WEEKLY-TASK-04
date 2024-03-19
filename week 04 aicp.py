class Item:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.number_of_bids = 0
        self.highest_bid = 0


class AuctionSystem:
    def __init__(self):
        self.items = []

    def setup_auction(self):
        while True:
            item_number = input("Enter item number (0 to finish setup): ")
            if item_number == '0':
                break
            description = input("Enter item description: ")
s            reserve_price = float(input("Enter reserve price: "))
            item = Item(item_number, description, reserve_price)
            self.items.append(item)

    def display_items(self):
        print("\nItems in Auction:")
        for item in self.items:
            print(f"Item Number: {item.item_number}, Description: {item.description}, "
                  f"Reserve Price: ${item.reserve_price}, Number of Bids: {item.number_of_bids}, "
                  f"Highest Bid: ${item.highest_bid}")

    def find_item(self, item_number):
        for item in self.items:
            if item.item_number == item_number:
                return item
        return None

    def place_bid(self, buyer_number):
        while True:
            item_number = input("Enter item number you want to bid on: ")
            item = self.find_item(item_number)
            if item is None:
                print("Item not found. Please enter a valid item number.")
                continue
            current_bid = item.highest_bid
            new_bid = float(input(f"Enter your bid for item {item.item_number} (Current highest bid: ${current_bid}): "))
            if new_bid <= current_bid:
                print("Your bid must be higher than the current highest bid.")
                continue
            item.number_of_bids += 1
            item.highest_bid = new_bid
            print("Bid successfully placed!")
            break

    def end_auction(self):
        total_fee = 0
        items_sold = 0
        items_not_sold = 0
        items_with_no_bids = 0

        print("\nAuction Results:")
        for item in self.items:
            if item.highest_bid >= item.reserve_price:
                items_sold += 1
                fee = item.highest_bid * 0.1
                total_fee += fee
                print(f"Item {item.item_number} sold for ${item.highest_bid} (Fee: ${fee})")
            else:
                if item.number_of_bids == 0:
                    items_with_no_bids += 1
                else:
                    items_not_sold += 1
                print(f"Item {item.item_number} did not meet reserve price.")

        print(f"\nTotal Fee for Sold Items: ${total_fee}")
        print(f"Number of Items Sold: {items_sold}")
        print(f"Number of Items Not Sold (Didn't meet reserve price): {items_not_sold}")
        print(f"Number of Items with No Bids: {items_with_no_bids}")


def main():
    auction_system = AuctionSystem()

    print("Welcome to the Auction System!")
    num_items = int(input("Enter the number of items to set up for auction (minimum 10): "))
    if num_items < 10:
        print("Error: Minimum 10 items required for the auction.")
        return

    print("\nSetting up Auction...")
    for _ in range(num_items):
        auction_system.setup_auction()

    print("\nAuction Setup Complete!")
    auction_system.display_items()

    while True:
        option = input("\nEnter 'B' to place a bid, 'E' to end the auction: ").upper()
        if option == 'B':
            auction_system.place_bid(1)  # Assuming a fixed buyer number for simplicity
        elif option == 'E':
            auction_system.end_auction()
            break
        else:
            print("Invalid option. Please enter 'B' or 'E'.")


if __name__ == "__main__":
    main()
