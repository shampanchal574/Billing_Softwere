import customtkinter as ctk

from ui.products_panel import ProductsPanel
from ui.bill_panel import BillPanel
from ui.history_panel import HistoryPanel


class BillingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Billing Software")
        self.geometry("1200x600")

        # Products big, Bill medium, History small
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.bill_panel = BillPanel(self)
        self.bill_panel.grid(row=0, column=1, sticky="nsew", padx=8, pady=8)

        ProductsPanel(self, self.bill_panel).grid(
            row=0, column=0, sticky="nsew", padx=8, pady=8
        )

        HistoryPanel(self).grid(
            row=0, column=2, sticky="nsew", padx=8, pady=8
        )
