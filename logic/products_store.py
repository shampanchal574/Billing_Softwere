import json
import os

PRODUCT_FILE = "data/products.json"


def load_products():
    if not os.path.exists(PRODUCT_FILE):
        return []

    with open(PRODUCT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_products(products):
    os.makedirs("data", exist_ok=True)
    with open(PRODUCT_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4)


def add_product(name, price, stock):
    products = load_products()

    products.append({
        "name": name,
        "price": price,
        "stock": stock
    })

    save_products(products)


def delete_product(index):
    products = load_products()

    if 0 <= index < len(products):
        products.pop(index)
        save_products(products)