from abc import ABC, abstractmethod


class Promotion(ABC):
    """Promotion class that will expose a simple interface.
    It consists of an instance variable (member) for name, and only one method.  add promotions to a product instance and remove them.
    We also want to be able to add the same promotion to multiple products without repeating code."""

    def __init__(self, name):
        self._name = name

    def apply_promotion(self, product, quantity):
        """Apply the promotion"""
        pass


class PercentageDiscount(Promotion):
    """apply specific percentage discount to the product"""
    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * (1 - self.percentage / 100)
        return discounted_price


class SecondItemHalfPrice(Promotion):
    """Apply 50% discount on second item"""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity % 2 == 0:
            return (quantity // 2) * (product.price * 1.5)
        else:
            return ((quantity // 2) * (product.price * 1.5)) + product.price


class Buy2Get1Free(Promotion):
    """apply 1 free item fOR every two purchased """

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_item = quantity // 3
        return (quantity - free_item) * product.price
