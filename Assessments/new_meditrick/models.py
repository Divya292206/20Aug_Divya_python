# models.py
from datetime import datetime
from typing import List

class User:
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role  # 'admin', 'receptionist', 'doctor'

class Patient:
    def __init__(self, patient_id: int, name: str, age: int, gender: str, contact: str, notes: str = ""):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.notes = notes
        self.appointments: List[Appointment] = []

    def add_appointment(self, appt):
        self.appointments.append(appt)

class Appointment:
    def __init__(self, appt_id: int, patient_id: int, doctor: str, date_time: datetime, reason: str, status: str = "Scheduled"):
        self.appt_id = appt_id
        self.patient_id = patient_id
        self.doctor = doctor
        self.date_time = date_time
        self.reason = reason
        self.status = status  # Scheduled, Completed, Followup, Cancelled
        self.prescriptions = []  # list of (medicine_name, qty, unit_price)

    def add_prescription(self, name, qty, unit_price):
        self.prescriptions.append((name, qty, unit_price))

class Invoice:
    def __init__(self, invoice_id: int, patient_id: int, appt_id: int, consultation_fee: float, medicines_total: float, tax_percent: float):
        self.invoice_id = invoice_id
        self.patient_id = patient_id
        self.appt_id = appt_id
        self.consultation_fee = float(consultation_fee)
        self.medicines_total = float(medicines_total)
        self.tax_percent = float(tax_percent)

    def compute_totals(self):
        # Step-by-step compute:
        # 1) subtotal = consultation + medicines
        subtotal = self.consultation_fee + self.medicines_total
        # 2) tax_amount = subtotal * tax_percent / 100
        tax_amount = subtotal * (self.tax_percent / 100.0)
        # 3) total = subtotal + tax_amount
        total = subtotal + tax_amount
        return {
            "subtotal": round(subtotal, 2),
            "tax_amount": round(tax_amount, 2),
            "total": round(total, 2)
        }
