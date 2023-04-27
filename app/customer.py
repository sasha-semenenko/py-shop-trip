from math import dist
from typing import List

from app.shop import Shop


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
        return (self.car["fuel_consumption"] * distance / 100) * fuel_price

    def product_cost(self, product: dict) -> float:
        milk = self.product["milk"] * product["milk"]
        bread = self.product["bread"] * product["bread"]
        butter = self.product["butter"] * product["bread"]
        return milk + bread + butter

    def cheap_store(self, fuel_price: float, shops: List[Shop]) -> tuple:
        cheap_shop_price = {}
        for shop in shops:
            fuel_cost = self.fuel_cost(fuel_price, shop.location) * 2
            product_price = self.product_cost(shop.product)
            total_cost = round(fuel_cost + product_price, 2)
            cheap_shop_price[total_cost] = shop.name
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
        return cheap_shop_price[min(cheap_shop_price)], min(cheap_shop_price)

    def shopping(self, shop: Shop, fuel_price: float, product_cost: float) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location
        fuel_cost = round(self.fuel_cost(fuel_price, shop.location) * 2, 2)
        self.money -= fuel_cost
        self.money -= product_cost

    def way_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money}")

