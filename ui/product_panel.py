import customtkinter as ctk

class ProductPanel(ctk.CTkFrame):
    def __init__(self, parent, add_item):
        super().__init__(parent)
        self.add_item = add_item

        ctk.CTkLabel(self, text="Products", font=("Arial", 20)).pack(pady=10)

        self.create("Tea", 10)
        self.create("Coffee", 30)
        self.create("Biscuit", 20)

    def create(self, name, price):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame, text=name).pack(side="left", padx=10)
        ctk.CTkButton(
            frame,
            text=f"₹{price}  Add",
            command=lambda: self.add_item(name, price)
        ).pack(side="right", padx=10)
