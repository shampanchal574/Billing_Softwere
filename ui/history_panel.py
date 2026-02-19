import customtkinter as ctk
from database.history_db import get_history

class HistoryPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="History", font=("Arial", 20)).pack(pady=10)
        self.box = ctk.CTkTextbox(self)
        self.box.pack(fill="both", expand=True, padx=10, pady=10)

        self.load()

    def load(self):
        self.box.delete("1.0", "end")
        for c, d, p in get_history():
            self.box.insert("end", f"{c} | {d}\n{p}\n\n")
