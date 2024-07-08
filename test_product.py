import pytest
from products import Product


def test_create_product():
    """Test that creating a normal product works."""
    p = Product("Item", 10, 10)
    assert p.name == "Item"
    assert p.price == 10
    assert p.quantity == 10
    assert p.is_active()  # Call the method from products.py


def test_create_product_invalid_details():
    """Test that creating a product with invalid details (empty name, negative price) invokes an exception."""
    with pytest.raises(ValueError):
        Product("", 10, 10)
    with pytest.raises(ValueError):
        Product("Item", -10, 10)
    with pytest.raises(ValueError):
        Product("Item", 10, -10)


def test_product_quantity_zero():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    p = Product("Item", 10.0, 1)
    p.set_quantity(0)
    assert p.quantity == 0
    assert not p.is_active()  # Check if the product is inactive


def test_product_purchase():
    """Test that product purchase modifies the quantity and returns the right output."""
    p = Product("Item", 10, 10)
    p.buy(5)
    assert p.quantity == 5


def test_product_purchase_invalid_quantity():
    """Test that buying a larger quantity than exists invokes exception."""
    p = Product("Item", 10, 10)
    with pytest.raises(ValueError):
        p.buy(11)
    assert p.quantity == 10  # Check the quantity after the failed buy



if __name__ == "__main__":
    pytest.main()
