# gui/billing.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from db import get_conn
from utils import save_invoice_text, save_invoice_csv
from models import Invoice
from datetime import datetime
from utils import save_invoice_text, save_invoice_csv


class BillingWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Billing")
        tk.Button(self, text="Create Invoice", command=self.create_invoice).pack(pady=8)
        self.txt = tk.Text(self, width=80, height=20)
        self.txt.pack()

    def create_invoice(self):
        try:
            appointment_id = simpledialog.askinteger("Appointment ID", "Enter appointment ID:", parent=self)
            if not appointment_id:
                return
            # load appointment + prescriptions
            conn = get_conn()
            c = conn.cursor()
            appt = c.execute("SELECT a.*, p.name as patient_name FROM appointments a LEFT JOIN patients p ON a.patient_id = p.id WHERE a.id=?", (appointment_id,)).fetchone()
            if not appt:
                messagebox.showerror("Error", "Appointment not found")
                return
            # gather prescriptions
            pres = c.execute("SELECT * FROM prescriptions WHERE appointment_id=?", (appointment_id,)).fetchall()
            medicines_total = 0.0
            items = []
            for pr in pres:
                row_total = pr["qty"] * pr["unit_price"]
                medicines_total += row_total
                items.append(f"{pr['drug_name']} x {pr['qty']} = {row_total}")

            consultation_fee = simpledialog.askfloat("Consultation Fee", "Enter consultation fee:", parent=self, minvalue=0)
            tax = simpledialog.askfloat("Tax %", "Enter tax percent (eg 5 for 5%):", parent=self, minvalue=0)
            if consultation_fee is None or tax is None:
                messagebox.showinfo("Cancelled", "Invoice cancelled")
                return

            # create Invoice record in DB
            created_at = datetime.now().isoformat()
            c.execute("INSERT INTO invoices (patient_id, appointment_id, consultation_fee, medicines_total, tax_percent, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                      (appt["patient_id"], appointment_id, consultation_fee, medicines_total, tax, created_at))
            invoice_id = c.lastrowid
            conn.commit()
            conn.close()

            inv = Invoice(invoice_id, appt["patient_id"], appointment_id, consultation_fee, medicines_total, tax)
            totals = inv.compute_totals()
            invoice_data = {
                "patient_name": appt["patient_name"],
                "items": items,
                "subtotal": totals["subtotal"],
                "tax_amount": totals["tax_amount"],
                "total": totals["total"],
                "created_at": created_at
            }
            txt_path = save_invoice_text(invoice_id, invoice_data)
            csv_path = save_invoice_csv(invoice_id, invoice_data)
            self.txt.insert("end", f"Invoice {invoice_id} saved: {txt_path} and {csv_path}\nTotal: {totals['total']}\n")
            messagebox.showinfo("Invoice Created", f"Saved: {txt_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
