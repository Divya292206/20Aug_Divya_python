# gui/dashboard.py
import tkinter as tk
import re
from tkinter import messagebox
from gui.patient_form import PatientForm
from gui.appointment_form import AppointmentForm
from gui.billing import BillingWindow
#from reports import regex_search_patients
from gui.reports import regex_search_patients



class Dashboard(tk.Frame):
    def __init__(self, master, username, role):
        super().__init__(master)
        self.master = master
        self.username = username
        self.role = role
        self.pack(fill="both", expand=True)
        tk.Label(self, text=f"Welcome {username} ({role})", font=("Arial", 14)).pack(pady=6)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        if role in ("admin", "receptionist"):
            tk.Button(btn_frame, text="Add / Edit Patients", command=self.open_patient_form).grid(row=0, column=0, padx=5)
            tk.Button(btn_frame, text="Appointments", command=self.open_appointment_form).grid(row=0, column=1, padx=5)
        if role in ("admin", "doctor"):
            tk.Button(btn_frame, text="Billing", command=self.open_billing).grid(row=0, column=2, padx=5)

        # regex search
        tk.Label(self, text="Regex Search (disease/status):").pack()
        self.search_entry = tk.Entry(self)
        self.search_entry.pack()
        tk.Button(self, text="Search", command=self.do_search).pack(pady=6)
        self.result_box = tk.Text(self, height=10, width=80)
        self.result_box.pack()

    def open_patient_form(self):
        PatientForm(self.master)

    def open_appointment_form(self):
        AppointmentForm(self.master)

    def open_billing(self):
        BillingWindow(self.master)

    def do_search(self):
        pattern = self.search_entry.get().strip()
        if not pattern:
            messagebox.showinfo("Info", "Enter a regex pattern")
            return
        try:
            rows = regex_search_patients(pattern)
            self.result_box.delete("1.0", "end")
            for r in rows:
                self.result_box.insert("end", f"{r}\n")
        except re.error as e:
            messagebox.showerror("Regex error", str(e))
