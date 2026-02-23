import customtkinter as ctk
from ui.bill_panel import BillPanel
from ui.history_panel import HistoryPanel

class AppUI(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Billing Software")
        self.geometry("1000x650")

        tabview = ctk.CTkTabview(self)
        tabview.pack(fill="both", expand=True, padx=10, pady=10)

        tabview.add("Billing")
        tabview.add("History")

        BillPanel(tabview.tab("Billing")).pack(fill="both", expand=True)
        HistoryPanel(tabview.tab("History")).pack(fill="both", expand=True)