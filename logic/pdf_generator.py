from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib import pagesizes
from security.license_guard import get_store_data
from datetime import datetime
import os

os.makedirs("invoices", exist_ok=True)

def generate_pdf(bill_no, customer, items, total):
    store = get_store_data()["store"]

    file = f"invoices/{bill_no}.pdf"
    doc = SimpleDocTemplate(file, pagesize=pagesizes.A4)
    elements = []

    styles = getSampleStyleSheet()

    elements.append(Paragraph(f"<b>{store}</b>", styles["Title"]))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(f"Customer: {customer}", styles["Normal"]))
    elements.append(Paragraph(f"Bill No: {bill_no}", styles["Normal"]))
    elements.append(Paragraph(f"Date: {datetime.now().strftime('%d-%m-%Y')}", styles["Normal"]))
    elements.append(Spacer(1, 20))

    data = [["Product", "Qty", "Price", "Total"]]
    for item in items:
        data.append(item)

    data.append(["", "", "Grand Total", total])

    table = Table(data)
    table.setStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ])

    elements.append(table)
    doc.build(elements)

    return file