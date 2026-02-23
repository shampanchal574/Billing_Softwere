import json
import os

CONFIG_FILE = "config/store.json"

def get_store_name():
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["store_name"]

def save_store_name(name):
    os.makedirs("config", exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"store_name": name}, f, indent=4)