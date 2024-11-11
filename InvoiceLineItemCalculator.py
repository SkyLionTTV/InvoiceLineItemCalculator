def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("The Invoice Line Item Calculator")

    while True:
        # Get valid inputs
        price = get_price()
        quantity = get_quantity()

        # Calculate and display total
        total = price * quantity
        print("\nPRICE:     {:.2f}".format(price))
        print("QUANTITY:  {}".format(quantity))
        print("TOTAL:     {:.2f}".format(total))

        # Ask if the user wants to enter another line item
        another = input("\nEnter another line item? (y/n): ").strip().lower()
        if another != 'y':
            print("\nBye!")
            break

if __name__ == "__main__":
    main()
