class Warehouse:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price, quantity):
        if name in self.products:
            raise ValueError(f"Produkt '{name}' już istnieje")

        self.products[name] = {
            "price": price,
            "quantity": quantity
        }

    def update_product(self, name, price=None, quantity=None):
        if name not in self.products:
            raise ValueError(f"Produkt '{name}' nie istnieje")

        if price is not None:
            self.products[name]["price"] = price

        if quantity is not None:
            self.products[name]["quantity"] = quantity

    def delete_product(self, name):
        if name not in self.products:
            raise ValueError(f"Produkt '{name}' nie istnieje")

        del self.products[name]

    def get_all_products(self):
        return self.products