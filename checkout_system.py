# Checkout System

menu = """1. Habbeer ($3.50)
2. Wine ($4.00)
3. Java Coffee ($2.50)
4. Apple Juice ($6.00)
5. Root Access Beer ($1.75)"""

# Implement your functions here!
def show_menu():
    print(menu)

def order():
    string = input("Please write down your order: ")

    prices = {"1": 3.5, "2": 4, "3": 2.5, "4": 6.0, "5": 1.75}

    total_price = 0
    for character in string:
        if character in prices:
            total_price += prices[character]

    return total_price

def add_percentage(price, percentage=15):
    return price * (1 + percentage / 100)

def add_tip(price):
    while True:
        tip = input("How much tip would you like to give? ")
        if tip.isdigit():
            tip = int(tip)
            return price * (1 + tip / 100)

def main():
    show_menu()
    price = order()
    subtotal_price = add_percentage(price)
    total = add_tip(subtotal_price)
    print(f"Total price: ${round(total, 2)}")

if __name__ == "__main__":
    # Call your functions here!
    main()
