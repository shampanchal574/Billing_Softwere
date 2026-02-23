import json
import os
from security.pc_id import get_pc_id

LICENSE_FILE = "license.lic"

def check_license():
    if not os.path.exists(LICENSE_FILE):
        return False, "License missing"

    try:
        with open(LICENSE_FILE, "r") as f:
            lic = json.load(f)

        if lic["pc_id"] != get_pc_id():
            return False, "License not for this PC"

        return True, lic["store_name"]

    except:
        return False, "Invalid license"