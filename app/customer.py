from math import dist


class Customer:
    def __init__(self, customers: dict) -> None:
        self.name: str = customers["name"]
        self.product: dict = customers["product_cart"]
        self.location: list = customers["location"]
        self.money: int = customers["money"]
        self.car: dict = customers["car"]

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def fuel_cost(self, fuel_price: float, shop_location: list) -> float:
        distance = dist(self.location, shop_location)
        return round(((self.car["fuel_consumption"] * distance / 100) * fuel_price) * 2, 2)

    def product_cost(self, product: dict) -> float:
        milk = self.product["milk"] * product["milk"]
        bread = self.product["bread"] * product["bread"]
        butter = self.product["butter"] * product["bread"]
        return milk + bread + butter

    def way_home(self, overall_cost: float) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - overall_cost}")
