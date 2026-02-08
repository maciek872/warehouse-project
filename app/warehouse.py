from typing import Optional, Dict


class Warehouse:
    def __init__(self):
        self.products: Dict[str, Dict[str, int]] = {}

    def add_product(self, name: str, price: int, quantity: int) -> None:
        if name in self.products:
            raise ValueError(f"Produkt '{name}' już istnieje")

        self.products[name] = {
            "price": price,
            "quantity": quantity
        }

    def update_product(
        self,
        name: str,
        price: Optional[int] = None,
        quantity: Optional[int] = None
    ) -> None:
        if name not in self.products:
            raise ValueError(f"Produkt '{name}' nie istnieje")

        if price is not None:
            self.products[name]["price"] = price

        if quantity is not None:
            self.products[name]["quantity"] = quantity

    def delete_product(self, name: str) -> None:
        if name not in self.products:
            raise ValueError(f"Produkt '{name}' nie istnieje")

        del self.products[name]

    def get_all_products(self) -> Dict[str, Dict[str, int]]:
        return self.products
