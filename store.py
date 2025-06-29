from typing import List

from products import Product


class Store():
    """
    Represents a store that manages a collection of products.

    The store maintains an inventory of Product instances, and provides
    methods for adding/removing products, checking total stock,
    retrieving active products, and processing customer orders.

    Attributes:
        list_of_products (List[Product]): The current inventory of products in the store.
    """
    def __init__(self, products=None):
        if products is None:
            products = []
        self.list_of_products = products

    def add_product(self, product):
        """Adds a new product to the store."""
        self.list_of_products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.list_of_products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of the store."""
        return sum(product.quantity for product in self.list_of_products)

    def get_all_products(self) -> List[Product]:
        """Returns a list of all products in the store."""
        return [product for product in self.list_of_products if product.active]

    def order(self, shopping_list) -> float:
        """Calculates and Returns the price of the purchase."""
        total_price = 0.00

        for product_to_buy, quantity_to_buy in shopping_list:
            if quantity_to_buy > product_to_buy.quantity:
                raise Exception("Not enough quantity")

            total_price += product_to_buy.buy(quantity_to_buy)

        return total_price


