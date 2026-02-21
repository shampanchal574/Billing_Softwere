import json
import os

DATA_FILE = "data/products.json"

_products = {}


# ================= LOAD ON APP START =================
def load_products():
    global _products
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            _products = json.load(f)
    else:
        _products = {}


# ================= SAVE TO FILE =================
def save_products():
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(_products, f, indent=4)


# ================= CRUD OPERATIONS =================
def get_products():
    return _products


def add_product(name, price, stock):
    _products[name] = {
        "name": name,
        "price": price,
        "stock": stock
    }
    save_products()


def remove_product(name):
    if name in _products:
        del _products[name]
        save_products()


def reduce_stock(name, qty):
    if name in _products and _products[name]["stock"] >= qty:
        _products[name]["stock"] -= qty
        save_products()
        return True
    return False