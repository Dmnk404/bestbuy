from typing import List

from products import Product


class Store():
    def __init__(self, products=None):
        if products is None:
            products = []
        self.list_of_products = products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.list_of_products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.list_of_products if product.active]

    def order(self, shopping_list) -> float:
        total_price = 0.00

        for product_to_buy, quantity_to_buy in shopping_list:
            if quantity_to_buy > product_to_buy.quantity:
                raise Exception("Not enough quantity")

            total_price += product_to_buy.buy(quantity_to_buy)

        return total_price


