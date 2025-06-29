from store import Store
from products import Product

product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
def show_products(store):
    """Shows all products in the store"""
    print("\n--- Products in Store ---")
    for idx, product in enumerate(store.get_all_products(), 1):
        print(Product.show(product))

best_buy = Store(product_list)

def start(store):
    """
    Starts an interactive command-line menu for the store.

    Allows the user to:
    1. View all active products
    2. See the total quantity of items in the store
    3. Place an order by selecting products and quantities
    4. Exit the program

    :param store: Store object that manages the product inventory
    """
    while True:
        print("     __________      ")
        print("     Store Menu      ")
        options = ["List all products in store",
                   "Show total amount of products in store",
                   "Make an order",
                    "Quit"]
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\n--- Products in Store ---")
            show_products(store)

        elif choice == "2":
            print(f"\nTotal quantity in store: {store.get_total_quantity()} items")

        elif choice == "3":
            shopping_list = []
            products = store.get_all_products()
            show_products(store)
            print("\nEnter product numbers and quantities (leave empty to finish):")

            while True:
                product_num = input("Product number: ")
                if not product_num:
                    break

                quantity = input("Quantity: ")
                if not quantity:
                    break

                try:
                    product_idx = int(product_num) - 1
                    quantity = int(quantity)
                    product = products[product_idx]
                    shopping_list.append((product, quantity))
                except (ValueError, IndexError):
                    print("Invalid input, try again.")

            try:
                total = store.order(shopping_list)
                print(f"Order successful! Total price: ${total:.2f}")
            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice, please try again.")


def main():
    """Main function"""
    start(best_buy)

if __name__ == "__main__":
    main()


