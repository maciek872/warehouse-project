from typing import Optional, Dict
from dataclasses import dataclass
import copy


@dataclass
class Product:
    # Represents a single product in the warehouse
    price: int
    quantity: int


class Warehouse:
    def __init__(self):
        # Dictionary storing products by name
        self.products: Dict[str, Product] = {}

    def add_product(self, name: str, price: int, quantity: int) -> None:
        # Add a new product to the warehouse
        if name in self.products:
            raise ValueError(f"Product '{name}' already exists")

        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative")

        self.products[name] = Product(price, quantity)

    def update_product(
        self,
        name: str,
        price: Optional[int] = None,
        quantity: Optional[int] = None
    ) -> None:
        # Update an existing product's price and/or quantity
        if name not in self.products:
            raise ValueError(f"Product '{name}' does not exist")

        product = self.products[name]

        if price is not None:
            if price < 0:
                raise ValueError("Price cannot be negative")
            product.price = price

        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            product.quantity = quantity

    def delete_product(self, name: str) -> None:
        # Remove a product from the warehouse
        if name not in self.products:
            raise ValueError(f"Product '{name}' does not exist")

        del self.products[name]

    def get_all_products(self) -> Dict[str, Product]:
        # Return a safe copy of all products
        return copy.deepcopy(self.products)
