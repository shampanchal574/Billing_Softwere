from cryptography.fernet import Fernet
import base64
import hashlib

SECRET_KEY = hashlib.sha256(b"billing_software_secret").digest()
FERNET_KEY = base64.urlsafe_b64encode(SECRET_KEY)
fernet = Fernet(FERNET_KEY)

def encrypt_data(data):
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data):
    return fernet.decrypt(data.encode()).decode()