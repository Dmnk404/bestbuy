class Product:
    
    total_quantity = 0

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Please enter product name.")
        if price < 0:
            raise ValueError("Please enter price greater than zero.")
        if quantity < 0:
            raise ValueError("Please enter quantity greater than zero.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        Product.total_quantity += quantity

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return "{} {}".format(self.name, self.price, self.quantity)

    def buy(self, quantity: int) -> float:

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if self.quantity < quantity:
            raise ValueError("Not enough in storage.")

        total_price = quantity * self.price
        self.quantity -= quantity
        Product.total_quantity -= quantity
        return total_price