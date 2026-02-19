import customtkinter as ctk
from ui.product_panel import ProductPanel
from ui.bill_panel import BillPanel
from ui.history_panel import HistoryPanel

class BillingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Billing Software")
        self.geometry("1200x600")

        self.grid_columnconfigure((0,1,2), weight=1)

        self.mode = "dark"

        def toggle():
            self.mode = "light" if self.mode == "dark" else "dark"
            ctk.set_appearance_mode(self.mode)

        ctk.CTkButton(self, text="🌙 / ☀ Mode", command=toggle).grid(
            row=1, column=1, pady=5
        )

        bill = BillPanel(self)
        bill.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        ProductPanel(self, bill.add_item).grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        HistoryPanel(self).grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
