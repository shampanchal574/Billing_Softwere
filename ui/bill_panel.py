import customtkinter as ctk
import os

from logic.billing import calculate_total
from logic.pdf_generator import generate_pdf
from logic.whatsapp import open_whatsapp
from database.history_db import add_history


class BillPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.items = {}

        ctk.CTkLabel(self, text="Bill", font=("Arial", 20)).pack(pady=10)

        self.customer = ctk.CTkEntry(self, placeholder_text="Customer Name")
        self.customer.pack(pady=5)

        self.phone = ctk.CTkEntry(self, placeholder_text="WhatsApp Number")
        self.phone.pack(pady=5)

        self.box = ctk.CTkTextbox(self, height=220)
        self.box.pack(fill="both", padx=10, pady=10)

        self.total_label = ctk.CTkLabel(self, text="Total: ₹0")
        self.total_label.pack()

        ctk.CTkButton(
            self,
            text="Generate & Share",
            command=self.share
        ).pack(pady=10)

    def add_item(self, product):
        name = product["name"]
        if name in self.items:
            self.items[name]["qty"] += 1
        else:
            self.items[name] = {
                "name": name,
                "price": product["price"],
                "qty": 1
            }
        self.update_bill()

    def update_bill(self):
        self.box.delete("1.0", "end")
        for i in self.items.values():
            self.box.insert(
                "end",
                f"{i['name']} x{i['qty']} = ₹{i['price'] * i['qty']}\n"
            )
        total = calculate_total(self.items.values())
        self.total_label.configure(text=f"Total: ₹{total}")

    def share(self):
        if not self.items:
            return
        if not self.customer.get() or not self.phone.get():
            return

        items = list(self.items.values())
        total = calculate_total(items)

        pdf_path = generate_pdf(
            self.customer.get(),
            self.phone.get(),
            items,
            total
        )

        add_history(
            self.customer.get(),
            self.phone.get(),
            total,
            pdf_path
        )

        open_whatsapp(
            self.phone.get(),
            f"🧾 Panchal Store Invoice\n\n"
            f"Customer: {self.customer.get()}\n"
            f"Total Amount: ₹{total}\n\n"
            f"Thank you for shopping with us 🙏\n"
            f"Please visit again!"
        )

        # Open invoice folder for quick attach
        os.startfile(os.path.dirname(pdf_path))

        # 🔥 Clear bill for next customer
        self.items.clear()
        self.box.delete("1.0", "end")
        self.customer.delete(0, "end")
        self.phone.delete(0, "end")
        self.total_label.configure(text="Total: ₹0")
