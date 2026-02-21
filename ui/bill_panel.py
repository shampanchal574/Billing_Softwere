import customtkinter as ctk
import os

from utils.excel_sales import save_sale_to_excel
from logic.billing import calculate_total
from logic.pdf_generator import generate_pdf
from logic.whatsapp import open_whatsapp
from logic.products_store import reduce_stock
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

        ctk.CTkButton(self, text="Generate & Share", command=self.share).pack(pady=10)

    # ================= ADD ITEM =================
    def add_item(self, product):
        name = product["name"]

        if not reduce_stock(name, 1):
            return  # insufficient stock

        if name in self.items:
            self.items[name]["qty"] += 1
        else:
            self.items[name] = {
                "name": name,
                "price": product["price"],
                "qty": 1
            }

        self.update_bill()

    # ================= UPDATE BILL =================
    def update_bill(self):
        self.box.delete("1.0", "end")
        for i in self.items.values():
            self.box.insert(
                "end",
                f"{i['name']} x{i['qty']} = ₹{i['price'] * i['qty']}\n"
            )

        total = calculate_total(self.items.values())
        self.total_label.configure(text=f"Total: ₹{total}")

    # ================= FINALIZE & SHARE =================
    def share(self):
        if not self.items:
            return

        items = list(self.items.values())
        total = calculate_total(items)

        # ---- Generate PDF ----
        pdf_path = generate_pdf(
            self.customer.get(),
            self.phone.get(),
            items,
            total
        )

        # ---- Save to history DB ----
        add_history(
            self.customer.get(),
            self.phone.get(),
            total,
            pdf_path
        )

        # ✅ SAVE SALE TO EXCEL (MONTH-WISE)
        save_sale_to_excel(
            customer=self.customer.get(),
            phone=self.phone.get(),
            items=items,
            total=total
        )

        # ---- WhatsApp message with FULL DETAILS ----
        msg = "🧾 Panchal Store\n\n"
        msg += f"Customer: {self.customer.get()}\n\n"
        for i in items:
            msg += f"{i['name']} x{i['qty']} = ₹{i['price'] * i['qty']}\n"
        msg += f"\nTotal Amount: ₹{total}\n\n"
        msg += "Thank you for shopping with us 🙏\nVisit again!"

        open_whatsapp(self.phone.get(), msg)

        # Open invoice folder
        os.startfile(os.path.dirname(pdf_path))

        # ---- Clear for next customer ----
        self.items.clear()
        self.box.delete("1.0", "end")
        self.customer.delete(0, "end")
        self.phone.delete(0, "end")
        self.total_label.configure(text="Total: ₹0")