from datetime import datetime


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name: str = shop["name"]
        self.location: list = shop["location"]
        self.product: dict = shop["products"]

    def purchase_receipt(self, name: str, product_cart: dict,) -> None:
        date = datetime.now().strftime("%d/%m/%Y %h:%m:%s")
        print(f"Date: {date}"
              f"Thanks, {name}, for your purchase!"
              f"You have bought: ")
        overall_cost = 0
        for product, cost in product_cart.items():
            cost_product = self.product[product] * cost
            overall_cost += cost_product
            print(f"{cost} {product}s for {cost * cost_product} dollars"
                  f"Total cost is {overall_cost}"
                  f"See you again!")
