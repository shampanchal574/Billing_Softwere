import customtkinter as ctk
import os
from database.history_db import search_history, get_sales_summary

class HistoryPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="History", font=("Arial", 20)).pack(pady=5)

        self.search = ctk.CTkEntry(self, placeholder_text="Search name or phone")
        self.search.pack(fill="x", padx=10)
        self.search.bind("<KeyRelease>", lambda e: self.load())

        self.box = ctk.CTkTextbox(self)
        self.box.pack(fill="both", expand=True, padx=10, pady=10)

        self.sales_label = ctk.CTkLabel(self, text="")
        self.sales_label.pack(pady=5)

        btns = ctk.CTkFrame(self)
        btns.pack()

        ctk.CTkButton(btns, text="Today", command=lambda: self.sales("today")).pack(side="left", padx=5)
        ctk.CTkButton(btns, text="Week", command=lambda: self.sales("week")).pack(side="left", padx=5)
        ctk.CTkButton(btns, text="Month", command=lambda: self.sales("month")).pack(side="left", padx=5)

        self.load()

    def load(self):
        self.box.delete("1.0", "end")
        data = search_history(self.search.get())

        for c, p, t, d, pdf in data:
            self.box.insert(
                "end",
                f"{c} | {p}\n₹{t} | {d}\n{pdf}\n\n"
            )

    def sales(self, period):
        total = get_sales_summary(period)
        self.sales_label.configure(
            text=f"Total Sales ({period.title()}): ₹{total}"
        )

    def open_pdf(self, event):
        try:
            index = self.box.index("@%s,%s" % (event.x, event.y))
            line = self.box.get(f"{index} linestart", f"{index} lineend")
            if line.endswith(".pdf"):
                os.startfile(line.strip())
        except:
            pass
