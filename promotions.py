from abc import ABC, abstractmethod


class Promotion(ABC):
    """Promotion class that will expose a simple interface.
    It consists of an instance variable (member) for name, and only one method.  add         promotions to a product instance and remove them. We also want to be able to add the same promotion to multiple products without repeating code."""

    # The promotions you should implement are:
    # Percentage discount (i.e. 20% off)
    # Second item at half price
    # Buy 2, get 1 free

    def __init__(self, name):
        self._name = name

    def apply_promotion(self, product, quantity):
        """Apply the promotion to the cart.
        This method will be called by the Store class."""
        pass


class PercentageDiscount(Promotion):
    """apply specific percentage to the product"""
    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * (1 - self.percentage / 100)
        return discounted_price


class SecondItemHalfPrice(Promotion):
    """apply 505 discount on second item"""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity % 2 == 0:
            return (quantity // 2) * (product.price * 1.5)
        else:
            return ((quantity // 2) * (product.price * 1.5)) + product.price


class Buy2Get1Free(Promotion):
    """apply 1 free item fro every two purchased """

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_item = quantity // 3
        return (quantity - free_item) * product.price
