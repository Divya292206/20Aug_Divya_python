# utils.py
import os
import csv
from datetime import datetime
from typing import Dict

INVOICE_DIR = "invoices"

def ensure_invoice_dir():
    if not os.path.exists(INVOICE_DIR):
        os.makedirs(INVOICE_DIR)

def save_invoice_text(invoice_id: int, invoice_data: Dict):
    """
    invoice_data: dict with keys patient_name, items, subtotal, tax_amount, total, created_at
    """
    ensure_invoice_dir()
    fname = os.path.join(INVOICE_DIR, f"invoice_{invoice_id}.txt")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(f"Invoice ID: {invoice_id}\n")
        f.write(f"Patient: {invoice_data.get('patient_name')}\n")
        f.write(f"Created: {invoice_data.get('created_at')}\n")
        f.write("\nItems:\n")
        for row in invoice_data.get("items", []):
            f.write(f" - {row}\n")
        f.write("\n")
        f.write(f"Subtotal: {invoice_data.get('subtotal')}\n")
        f.write(f"Tax: {invoice_data.get('tax_amount')}\n")
        f.write(f"Total: {invoice_data.get('total')}\n")
    return fname

def save_invoice_csv(invoice_id: int, invoice_data: Dict):
    ensure_invoice_dir()
    fname = os.path.join(INVOICE_DIR, f"invoice_{invoice_id}.csv")
    with open(fname, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Invoice ID", invoice_id])
        writer.writerow(["Patient", invoice_data.get("patient_name")])
        writer.writerow(["Created", invoice_data.get("created_at")])
        writer.writerow([])
        writer.writerow(["Item", "Value"])
        for row in invoice_data.get("items", []):
            writer.writerow([row])
        writer.writerow([])
        writer.writerow(["Subtotal", invoice_data.get("subtotal")])
        writer.writerow(["Tax", invoice_data.get("tax_amount")])
        writer.writerow(["Total", invoice_data.get("total")])
    return fname
