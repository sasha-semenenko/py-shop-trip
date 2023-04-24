import json
from app.customer import Customer
from app.shop import Shop
from datetime import datetime


def shop_trip():
    with open("app/config.json", "r") as config_file:
        file_json = json.load(config_file)

        fuel_price = file_json["FUEL_PRICE"]
        customers = file_json["customers"]
        shops = file_json["shops"]

        for customer in customers:
            first_customer = Customer(customer)

            first_customer.__str__()
        shop_price = []
        for shop in shops:
            one_shop = Shop(shop)
            one_shop_price = first_customer.fuel_cost(fuel_price, one_shop.location) + first_customer.product_cost(one_shop.product)
            print(f"{first_customer.name}'s trip to the {one_shop.name} costs {one_shop_price}")
            shop_price.append(one_shop_price)
        best_shop = shops[shop_price.index(min(shop_price))]

        if min(shop_price) <= first_customer.money:
            best_shop = Shop(best_shop)
            print(f"{first_customer.name} rides to {best_shop.name}")
            print(f"{datetime.now().strftime('%D/%M/%Y %h:%m:%s')}")
            best_shop.product_cost(first_customer.name, first_customer.product)
            print(f"Total cost is {}")