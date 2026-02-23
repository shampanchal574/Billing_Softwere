import customtkinter as ctk
from security.license_guard import save_license

class FirstSetup(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("First Time Setup")
        self.geometry("400x300")

        self.store_entry = ctk.CTkEntry(self, placeholder_text="Enter Store Name")
        self.store_entry.pack(pady=10)

        self.pass_entry = ctk.CTkEntry(self, placeholder_text="Set Owner Password", show="*")
        self.pass_entry.pack(pady=10)

        ctk.CTkButton(self, text="Save & Activate", command=self.save).pack(pady=20)

    def save(self):
        store = self.store_entry.get()
        password = self.pass_entry.get()

        if store and password:
            save_license(store, password)
            self.destroy()