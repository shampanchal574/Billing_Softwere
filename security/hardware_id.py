import uuid
import hashlib

def get_hardware_id():
    mac = uuid.getnode()
    hwid = hashlib.sha256(str(mac).encode()).hexdigest()
    return hwid