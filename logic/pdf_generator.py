from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_pdf(customer, phone, items, total):
    os.makedirs("invoices", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"invoices/invoice_{phone}_{ts}.pdf"

    c = canvas.Canvas(path, pagesize=A4)

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 800, "PANCHAL STORE")

    c.setFont("Helvetica", 10)
    c.drawString(50, 780, "Quality you can trust")

    c.line(50, 770, 550, 770)

    c.setFont("Helvetica", 12)
    c.drawString(50, 750, f"Customer: {customer}")
    c.drawString(50, 730, f"Phone: {phone}")
    c.drawString(50, 710, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}")

    # Table
    y = 670
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Product")
    c.drawString(250, y, "Qty")
    c.drawString(320, y, "Price")
    c.drawString(400, y, "Total")

    y -= 20
    c.setFont("Helvetica", 11)
    for i in items:
        c.drawString(50, y, i["name"])
        c.drawString(250, y, str(i["qty"]))
        c.drawString(320, y, str(i["price"]))
        c.drawString(400, y, str(i["qty"] * i["price"]))
        y -= 18

    c.line(50, y - 10, 550, y - 10)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y - 30, f"Grand Total: ₹{total}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 80, "Thank you for shopping with us!")
    c.drawString(50, 65, "Please visit again 🙏")

    c.save()
    return os.path.abspath(path)
