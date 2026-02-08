import pytest
from app.warehouse import Warehouse


# Fixture that provides a fresh warehouse instance for each test
@pytest.fixture
def warehouse():
    return Warehouse()


def test_add_product_success(warehouse):
    """Test that a product is added correctly to the warehouse."""
    warehouse.add_product("Laptop", 3000, 5)

    products = warehouse.get_all_products()

    assert "Laptop" in products
    assert products["Laptop"].price == 3000
    assert products["Laptop"].quantity == 5


def test_add_existing_product_raises_error(warehouse):
    """Test that adding an existing product raises ValueError."""
    warehouse.add_product("Laptop", 3000, 5)

    with pytest.raises(ValueError, match="already exists"):
        warehouse.add_product("Laptop", 3500, 10)


def test_update_product_price_and_quantity(warehouse):
    """Test updating both price and quantity of a product."""
    warehouse.add_product("Phone", 2000, 3)

    warehouse.update_product("Phone", price=2200, quantity=4)

    product = warehouse.get_all_products()["Phone"]

    assert product.price == 2200
    assert product.quantity == 4


def test_update_non_existing_product_raises_error(warehouse):
    """Test that updating a non-existing product raises ValueError."""
    with pytest.raises(ValueError, match="does not exist"):
        warehouse.update_product("Tablet", price=1000)


def test_delete_product_success(warehouse):
    """Test that a product is deleted successfully."""
    warehouse.add_product("Monitor", 800, 2)

    warehouse.delete_product("Monitor")

    assert "Monitor" not in warehouse.get_all_products()


def test_delete_non_existing_product_raises_error(warehouse):
    """Test that deleting a non-existing product raises ValueError."""
    with pytest.raises(ValueError, match="does not exist"):
        warehouse.delete_product("Mouse")