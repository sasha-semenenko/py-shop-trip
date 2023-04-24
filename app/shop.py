class Shop:
    def __init__(self, shops: dict) -> None:
        self.name: str = shops["name"]
        self.location: list = shops["location"]
        self.product: dict = shops["products"]

    def product_cost(self, name: str, product_cart: dict) -> None:
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought: ")
        print(f"{product_cart['milk']} milks for {self.product['milk'] * product_cart['milk']}")
        print(f"{product_cart['bread']} breads for {self.product['bread'] * product_cart['bread']}")
        print(f"{product_cart['butter']} butters for {self.product['butter'] * product_cart['butter']}")
