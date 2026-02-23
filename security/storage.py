import os

LOCK_FILE = os.path.join("data", "device.lock")

def save_uuid(uuid):
    os.makedirs("data", exist_ok=True)
    with open(LOCK_FILE, "w") as f:
        f.write(uuid)

def load_uuid():
    if os.path.exists(LOCK_FILE):
        with open(LOCK_FILE, "r") as f:
            return f.read().strip()
    return None