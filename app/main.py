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

        for shop in shops:
