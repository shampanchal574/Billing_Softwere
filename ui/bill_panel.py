import customtkinter as ctk
import os
from logic.billing import calculate_total
from logic.pdf_generator import generate_pdf
from logic.whatsapp import open_whatsapp
from database.history_db import add_history

class BillPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.items = []

        ctk.CTkLabel(self, text="Bill & Customer", font=("Arial", 20)).pack(pady=10)

        self.customer = ctk.CTkEntry(self, placeholder_text="Customer Name")
        self.customer.pack(pady=5)

        self.phone = ctk.CTkEntry(self, placeholder_text="WhatsApp Number")
        self.phone.pack(pady=5)

        self.box = ctk.CTkTextbox(self, height=200)
        self.box.pack(padx=10, pady=10, fill="both")

        self.total_label = ctk.CTkLabel(self, text="Total: ₹0")
        self.total_label.pack()

        ctk.CTkButton(self, text="Generate & Share", command=self.share).pack(pady=10)

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price, "qty": 1})
        self.update()

    def update(self):
        self.box.delete("1.0", "end")
        for i in self.items:
            self.box.insert("end", f"{i['name']} x{i['qty']} = ₹{i['price']}\n")
        self.total_label.configure(text=f"Total: ₹{calculate_total(self.items)}")

    def share(self):
        total = calculate_total(self.items)
        pdf = generate_pdf(self.customer.get(), self.phone.get(), self.items, total)

        add_history(self.customer.get(), pdf)

        open_whatsapp(
            self.phone.get(),
            f"🧾 Invoice\nCustomer: {self.customer.get()}\nTotal: ₹{total}"
        )

        os.startfile(os.path.dirname(pdf))
