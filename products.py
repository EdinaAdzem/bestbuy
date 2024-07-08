class Product:
    """The Product class represents a specific type of product available in the store"""
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: Name cannot be empty, price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self._is_active = True

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
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buys a given quantity of the product.Returns the total price (float) of the purchase.
        Updates the quantity of the product.In case of a problem raises an Exception."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price