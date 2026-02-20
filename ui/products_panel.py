import customtkinter as ctk
from logic.products_store import add_product, remove_product, get_products, reduce_stock


class ProductsPanel(ctk.CTkFrame):
    def __init__(self, parent, bill_panel):
        super().__init__(parent)
        self.bill_panel = bill_panel
        self.rows = {}  # cache UI rows

        ctk.CTkLabel(self, text="Products", font=("Arial", 22, "bold")).pack(pady=6)

        self.list_frame = ctk.CTkScrollableFrame(self, height=350)
        self.list_frame.pack(fill="both", expand=True, padx=6, pady=6)

        # ===== BOTTOM CONTROLS =====
        bottom = ctk.CTkFrame(self)
        bottom.pack(fill="x", padx=6, pady=6)

        self.name = ctk.CTkEntry(bottom, placeholder_text="Name", width=150)
        self.name.pack(side="left", padx=4)

        self.price = ctk.CTkEntry(bottom, placeholder_text="Price", width=80)
        self.price.pack(side="left", padx=4)

        self.stock = ctk.CTkEntry(bottom, placeholder_text="Stock", width=80)
        self.stock.pack(side="left", padx=4)

        ctk.CTkButton(bottom, text="Add Product", command=self.add_product)\
            .pack(side="left", padx=6)

        ctk.CTkButton(
            bottom, text="Remove Product", fg_color="gray",
            command=self.remove_product
        ).pack(side="left", padx=6)

        self.load_products()

    # ================= LOAD UI ONCE =================
    def load_products(self):
        self.rows.clear()
        for w in self.list_frame.winfo_children():
            w.destroy()

        for p in get_products().values():
            self.create_row(p)

    def create_row(self, p):
        row = ctk.CTkFrame(self.list_frame)
        row.pack(fill="x", pady=3, padx=4)

        label = ctk.CTkLabel(
            row,
            text=self.product_text(p),
            text_color=self.stock_color(p["stock"])
        )
        label.pack(side="left", padx=6)

        ctk.CTkButton(
            row, text="ADD", width=60,
            command=lambda prod=p: self.add_to_bill(prod)
        ).pack(side="right", padx=6)

        self.rows[p["name"]] = label

    # ================= ACTIONS =================
    def add_product(self):
        add_product(
            self.name.get(),
            float(self.price.get()),
            int(self.stock.get())
        )
        self.clear()
        self.load_products()

    def remove_product(self):
        remove_product(self.name.get())
        self.clear()
        self.load_products()

    def add_to_bill(self, product):
        if reduce_stock(product["name"], 1):
            self.bill_panel.add_item(product)
            self.update_stock(product["name"])

    # ================= UPDATE ONLY LABEL =================
    def update_stock(self, name):
        products = get_products()
        if name in self.rows:
            p = products[name]
            lbl = self.rows[name]
            lbl.configure(
                text=self.product_text(p),
                text_color=self.stock_color(p["stock"])
            )

    # ================= HELPERS =================
    def stock_color(self, stock):
        if stock <= 0:
            return "red"
        elif stock < 50:
            return "orange"
        else:
            return "White"

    def product_text(self, p):
        return f"{p['name']} | ₹{p['price']} | Stock: {p['stock']}"

    def clear(self):
        self.name.delete(0, "end")
        self.price.delete(0, "end")
        self.stock.delete(0, "end")