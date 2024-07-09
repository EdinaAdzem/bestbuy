class Product:
    """The Product class represents a specific type of product available in the store"""
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: Name cannot be empty, price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self._is_active = True
        self.promotion = None #promotion instance variable

    def get_promotion(self):
        """Getter for promotion."""
        return self.promotion

    def set_promotion(self, promotion):
        """Setter for promotion."""
        self.promotion = promotion

    def get_quantity(self):
        """Getter function for quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Getter function for active. Returns True if the product is active, otherwise False."""
        return self._is_active

    def activate(self):
        """Activates the product."""
        self._is_active = True

    def deactivate(self):
        """Deactivates the product."""
        self._is_active = False

    def show(self):
        """Returns a string that represents the product."""
        promotion_text = f"Promotion: {self.promotion._name}" if self.promotion else "No Promotion"
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_text}"

    def buy(self, quantity):
        """Buys a given quantity of the product. Returns the total price (float) of the purchase.
        Updates the quantity of the product. In case of a problem raises an Exception."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price

    #codio - Best buy 2

class NonStockedProduct(Product):
    """Some products in the store are not physical, so we don’t need to keep track of their quantity."""
    def __init__(self, name, price):
        super().__init__(name, price, 0)
        self._is_active = True

    def buy(self, quantity):
        """Overrides the buy method to handle non-stocked products differently."""
        if quantity <= 0:
            raise ValueError("Non-stocked products cannot be purchased.")
        return self.price * quantity

    def show(self):
        """Override show method to display special characteristics."""
        return f"NonStocked Product: {self.name}, Price: {self.price}, Quantity: Not Applicable"




#Codio Best Buy 2
class LimitedProduct(Product):#extends from product
    """Some products can only be purchased X times in an order. If an order is attempted with quantity larger than the maximum one, it should be refused with an exception.
    """
    def __init__(self, name, price, quantity, max_count):
        super().__init__(name, price, quantity)
        self.name = name
        if max_count < 1:
            raise ValueError("Limited to max_count = 1.")
        self.max_count = max_count

    def buy(self, quantity):
        if quantity > self.max_count:
            raise ValueError(f"Cannot purchase more than {self.max_count} {self.name}")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")
        return super().buy(quantity)

    def show(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Max Purchase Limit: {self.max_count}"