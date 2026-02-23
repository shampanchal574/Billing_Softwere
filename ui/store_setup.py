import customtkinter as ctk
from config.store import save_store_name


class StoreSetup(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Store Setup")
        self.geometry("420x220")
        self.resizable(False, False)

        # ===== TITLE =====
        ctk.CTkLabel(
            self,
            text="Welcome!",
            font=("Arial", 22, "bold")
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            self,
            text="Enter your Store Name",
            font=("Arial", 14)
        ).pack(pady=(0, 15))

        # ===== STORE NAME INPUT =====
        self.store_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="e.g. Panchal Store"
        )
        self.store_entry.pack(pady=5)

        # ===== SAVE BUTTON =====
        ctk.CTkButton(
            self,
            text="Save & Continue",
            width=160,
            command=self.save_store
        ).pack(pady=25)

    def save_store(self):
        store_name = self.store_entry.get().strip()

        if not store_name:
            return  # do nothing if empty

        save_store_name(store_name)
        self.destroy()