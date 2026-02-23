import os
import json
from security.hardware_id import get_hardware_id
from security.encryptor import encrypt_data, decrypt_data

CONFIG_FILE = "config/store_config.json"
os.makedirs("config", exist_ok=True)

def is_first_time():
    return not os.path.exists(CONFIG_FILE)

def save_license(store_name, password):
    data = {
        "store": store_name,
        "password": password,
        "hwid": get_hardware_id()
    }

    encrypted = encrypt_data(json.dumps(data))

    with open(CONFIG_FILE, "w") as f:
        f.write(encrypted)

def validate_license():
    if not os.path.exists(CONFIG_FILE):
        return False

    with open(CONFIG_FILE, "r") as f:
        encrypted = f.read()

    data = json.loads(decrypt_data(encrypted))

    if data["hwid"] != get_hardware_id():
        return False

    return True

def get_store_data():
    with open(CONFIG_FILE, "r") as f:
        encrypted = f.read()

    return json.loads(decrypt_data(encrypted))