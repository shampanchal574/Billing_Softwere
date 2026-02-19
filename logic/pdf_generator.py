from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_pdf(customer, phone, items, total):
    os.makedirs("invoices", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"invoices/invoice_{phone}_{timestamp}.pdf"

    c = canvas.Canvas(path, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "INVOICE")

    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Customer: {customer}")
    c.drawString(50, 750, f"Phone: {phone}")
    c.drawString(50, 730, f"Date: {datetime.now()}")

    y = 690
    c.drawString(50, y, "Product")
    c.drawString(250, y, "Qty")
    c.drawString(320, y, "Price")
    c.drawString(400, y, "Total")

    y -= 20
    for i in items:
        c.drawString(50, y, i["name"])
        c.drawString(250, y, str(i["qty"]))
        c.drawString(320, y, str(i["price"]))
        c.drawString(400, y, str(i["qty"] * i["price"]))
        y -= 20

    c.drawString(50, y - 20, f"Grand Total: ₹{total}")
    c.save()

    return os.path.abspath(path)
