products = {}

def add_product(name, price, stock):
    products[name] = {
        "name": name,
        "price": price,
        "stock": stock
    }

def remove_product(name):
    if name in products:
        del products[name]

def get_products():
    return products

def reduce_stock(name, qty):
    if name in products and products[name]["stock"] >= qty:
        products[name]["stock"] -= qty
        return True
    return False
