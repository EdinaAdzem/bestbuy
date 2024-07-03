class Store():
    """The Store class will contain one variable - a list of products that exist in the store."""

    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        """function to add a product"""
        self.product_list.append(product)

    def remove_product(self, product):
        """Removes a product from store."""
        self.product_list.remove(product)

    def get_total_quantity(self):
        """Returns how many items are in the store in total."""
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self):
        """Returns all products in the store that are active."""
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list):
        """Function that executes the buy and returns the total of the order"""
        total_order = 0
        for product, quantity in shopping_list:
            total_order += product.buy(quantity)
        return total_order
