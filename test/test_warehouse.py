from app.warehouse import Warehouse

import pytest
from app.warehouse import Warehouse


def test_add_product():
    warehouse = Warehouse()
    warehouse.add_product("Laptop", 3000, 5)

    products = warehouse.get_all_products()
    assert "Laptop" in products
    assert products["Laptop"]["price"] == 3000
    assert products["Laptop"]["quantity"] == 5


def test_add_existing_product_raises_error():
    warehouse = Warehouse()
    warehouse.add_product("Laptop", 3000, 5)

    with pytest.raises(ValueError, match="już istnieje"):
        warehouse.add_product("Laptop", 3500, 10)


def test_update_product_price_and_quantity():
    warehouse = Warehouse()
    warehouse.add_product("Phone", 2000, 3)

    warehouse.update_product("Phone", price=2200, quantity=4)

    product = warehouse.get_all_products()["Phone"]
    assert product["price"] == 2200
    assert product["quantity"] == 4


def test_update_non_existing_product_raises_error():
    warehouse = Warehouse()

    with pytest.raises(ValueError, match="nie istnieje"):
        warehouse.update_product("Tablet", price=1000)


def test_delete_product():
    warehouse = Warehouse()
    warehouse.add_product("Monitor", 800, 2)

    warehouse.delete_product("Monitor")

    assert "Monitor" not in warehouse.get_all_products()


def test_delete_non_existing_product_raises_error():
    warehouse = Warehouse()

    with pytest.raises(ValueError, match="nie istnieje"):
        warehouse.delete_product("Mouse")