import customtkinter as ctk
from ui.app_ui import BillingApp
from logic.products_store import load_products

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


load_products()

app = BillingApp()
app.mainloop()