class Product:
    """
    Represents a product in the store's inventory.

    Attributes:
        name (str): The name of the product.
        price (float): The price of a single unit (must be non-negative).
        quantity (int): The available quantity in stock (must be non-negative).
        active (bool): Indicates whether the product is available for purchase.
    """

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
        """Returns the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity of the product."""
        self.quantity = quantity

    def is_active(self) -> bool:
        """Returns whether the product is available for purchase."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string representation of the product."""
        return "{} {}".format(self.name, self.price, self.quantity)

    def buy(self, quantity: int) -> float:
        """Calculates and Returns the price of the purchase and checks if the entered quantity is valid and available"""

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