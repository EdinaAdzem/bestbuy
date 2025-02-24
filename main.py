import products
import store
import promotions


def show_menu():
    """Displays the menu options."""
    print("\n-------- \U0001F579Store Menu\U0001F579 ---------")
    print("1. List all products")
    print("2. Show total amount")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_obj):
    """List all products from the inventory"""
    products_list = store_obj.get_all_products()
    print("\n--- Products in Store ---")
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product.name} - Quantity: {product.quantity} - Price: ${product.price}")


def show_total_amount(store_obj):
    """total amount of items """
    total_quantity = store_obj.get_total_quantity()
    print(f"\nTotal number of items in the store: {total_quantity}")
    print("=" * 40)


def make_order(store_obj):
    """Separate function to handle the make an order option"""
    products_list = store_obj.get_all_products()
    shopping_list = []

    print("\n=== Make an Order ===")
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product.name}")

    while True:
        user_input = input("Which product would you like to order? ").strip().lower()
        print("-------> When you want to finish order, enter empty text.")
        if user_input == "":
            break

        selection = int(user_input)
        if 1 <= selection <= len(products_list):
            product = products_list[selection - 1]

            # Check for NonStockedProduct
            if isinstance(product, products.NonStockedProduct):
                print(f"{product.name} is not stockable!")
                continue

            quantity_input = input("Please enter the quantity? ").strip().lower()
            if quantity_input == "":
                print("Quantity cannot be empty. Please enter a valid quantity.")
                continue
            quantity = int(quantity_input)

            if quantity <= 0:
                print("Quantity to buy must be greater than zero.")
                continue

            # Check for LimitedProduct
            if isinstance(product, products.LimitedProduct):
                if quantity > product.max_count:
                    print(f"Cannot purchase more than {product.max_count} {product.name}(s).")
                    continue

            if quantity <= product.quantity:
                shopping_list.append((product, quantity))
                print("Product added to list!")
            else:
                print(f"Not in Stock! Please note the {product.quantity} {product.name} availability.")

    if shopping_list:
        total_cost = store_obj.order(shopping_list)
        # check where the promotions were applied and display to the user
        for product, quantity in shopping_list:
            if product.promotion:
                print(f"\033[91m🌟 Promotions applied for: {product.name}: {product.promotion._name}🌟\033[0m")
        print(f"********\nOrder made! Total payment:\033[91m🌟 {total_cost}🌟\033[0m********")
        print("=" * 40)
    else:
        print("No items added to the cart.")
        print("=" * 40)


def start(store_object):
    """Start the store interface."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            list_products(store_object)
        elif choice == '2':
            show_total_amount(store_object)
        elif choice == '3':
            make_order(store_object)
        elif choice == '4':
            print("\033[91m🌟Thank you for shopping at Best Buy!🌟\033[0m")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, max_count=1)
    ]

    # Create promotion catalog
    second_half_price = promotions.SecondItemHalfPrice("Second Half price!")
    third_one_free = promotions.Buy2Get1Free("Third One Free!")
    thirty_percent = promotions.PercentageDiscount("50% off!", percentage=50)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[2].set_promotion(thirty_percent)

    #To show the active promotions
    print("🌟Active Promotions🌟\033[0m")
    for product in product_list:
        if product.promotion:
            print(f"\033[91m🌟 Promotions applied for {product.name}: {product.promotion._name} 🌟\033[0m")
        else:
            print(f"\033[91m{product.show()}\033[0m")

    store_object = store.Store(product_list)
    start(store_object)