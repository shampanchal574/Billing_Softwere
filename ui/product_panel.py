import customtkinter as ctk
from database.products_db import products

class ProductPanel(ctk.CTkFrame):
    def __init__(self, parent, add_item):
        super().__init__(parent)
        self.add_item = add_item

        ctk.CTkLabel(self, text="Products", font=("Arial", 20)).pack(pady=10)

        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.pack(fill="both", expand=True)

        self.refresh()

    def refresh(self):
        for w in self.list_frame.winfo_children():
            w.destroy()

        for p in products:
            f = ctk.CTkFrame(self.list_frame)
            f.pack(fill="x", padx=5, pady=3)

            ctk.CTkLabel(f, text=p["name"]).pack(side="left", padx=5)
            ctk.CTkButton(
                f, text=f"₹{p['price']} Add",
                command=lambda x=p: self.add_item(x)
            ).pack(side="right")
