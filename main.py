from security.license_guard import is_first_time, validate_license
from setup.first_setup import FirstSetup
from ui.app_ui import AppUI

if is_first_time():
    app = FirstSetup()
    app.mainloop()

if not validate_license():
    print("This software is licensed to another device.")
    exit()

app = AppUI()
app.mainloop()