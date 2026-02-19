import os, urllib.parse

def open_whatsapp(phone, message):
    encoded = urllib.parse.quote(message)
    os.startfile(f"whatsapp://send?phone={phone}&text={encoded}")
