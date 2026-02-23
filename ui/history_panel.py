import customtkinter as ctk
from database.history_db import load_history
from ui.owner_dashboard import OwnerDashboard
from security.license_guard import get_store_data

class HistoryPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Sales History", font=("Arial", 20)).pack(pady=10)

        self.display_history()

        ctk.CTkButton(
            self,
            text="Owner Section",
            fg_color="darkred",
            command=self.open_owner_login
        ).pack(pady=20)

    def display_history(self):
        history = load_history()

        for record in history:
            text = f"{record['date']}  -  ₹{record['total']}"
            ctk.CTkLabel(self, text=text).pack()

    def open_owner_login(self):
        dialog = ctk.CTkInputDialog(
            text="Enter Owner Password",
            title="Owner Login"
        )
        password = dialog.get_input()

        store_data = get_store_data()

        if password == store_data["password"]:
            OwnerDashboard()
        else:
            ctk.CTkMessagebox(title="Error", message="Wrong Password")