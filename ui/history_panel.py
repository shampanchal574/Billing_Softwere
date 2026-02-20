import customtkinter as ctk
from tkinter import simpledialog
from database.history_db import (
    search_history,
    get_sales_summary,
    get_yearly_income
)

PASSWORD = "989094"


class HistoryPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="History", font=("Arial", 16)).pack(pady=5)

        self.search = ctk.CTkEntry(self, placeholder_text="Search")
        self.search.pack(fill="x", padx=5)
        self.search.bind("<KeyRelease>", lambda e: self.load())

        self.box = ctk.CTkTextbox(self, height=220)
        self.box.pack(fill="both", expand=True, padx=5, pady=5)

        # Buttons
        top = ctk.CTkFrame(self)
        top.pack(pady=2)

        ctk.CTkButton(top, text="Today", width=60,
                      command=lambda: self.sales("today")).pack(side="left", padx=2)
        ctk.CTkButton(top, text="Week", width=60,
                      command=lambda: self.sales("week")).pack(side="left", padx=2)

        bottom = ctk.CTkFrame(self)
        bottom.pack(pady=2)

        ctk.CTkButton(bottom, text="Month", width=60,
                      command=lambda: self.sales("month")).pack(side="left", padx=2)
        ctk.CTkButton(bottom, text="Year", width=60,
                      command=self.yearly).pack(side="left", padx=2)

        self.sales_label = ctk.CTkLabel(self, text="")
        self.sales_label.pack(pady=5)

        self.load()

    def load(self):
        self.box.delete("1.0", "end")
        for c, p, t, d, _ in search_history(self.search.get()):
            self.box.insert("end", f"{c}\n₹{t} | {d}\n\n")

    def sales(self, period):
        total = get_sales_summary(period)
        self.sales_label.configure(text=f"{period.title()} Sales: ₹{total}")

    def yearly(self):
        pwd = simpledialog.askstring("Password", "Enter password:", show="*")
        if pwd != PASSWORD:
            return

        total = get_yearly_income()
        self.sales_label.configure(text=f"Yearly Income: ₹{total}")

        self.after(60000, lambda: self.sales_label.configure(text=""))
