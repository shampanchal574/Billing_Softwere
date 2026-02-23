import webbrowser
import urllib.parse
from security.license_guard import get_store_data

def send_whatsapp(phone, customer, bill_no, total):
    store = get_store_data()["store"]

    message = f"""
Hello {customer},

Thank you for shopping at {store} 😊

Bill No: {bill_no}
Total Amount: ₹{total}

Please find your invoice attached.

Regards,
{store}
"""

    encoded = urllib.parse.quote(message)
    webbrowser.open(f"https://wa.me/{phone}?text={encoded}")