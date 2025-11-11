# gui/patient_form.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from db import get_conn
from datetime import datetime

class PatientForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Patients")
        self.geometry("600x400")
        tk.Button(self, text="Add Patient", command=self.add_patient).pack(pady=6)
        tk.Button(self, text="List Patients", command=self.list_patients).pack(pady=6)
        self.text = tk.Text(self, width=80, height=20)
        self.text.pack()

    def add_patient(self):
        name = simpledialog.askstring("Name", "Patient name:", parent=self)
        if not name:
            return
        age = simpledialog.askinteger("Age", "Age:", parent=self, minvalue=0, maxvalue=150)
        gender = simpledialog.askstring("Gender", "Gender:", parent=self)
        contact = simpledialog.askstring("Contact", "Contact number:", parent=self)
        notes = simpledialog.askstring("Notes", "Notes (disease, history):", parent=self)
        conn = get_conn()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO patients (name, age, gender, contact, notes) VALUES (?, ?, ?, ?, ?)",
                      (name, age or 0, gender or "", contact or "", notes or ""))
            conn.commit()
            messagebox.showinfo("Success", "Patient saved.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def list_patients(self):
        conn = get_conn()
        c = conn.cursor()
        rows = c.execute("SELECT * FROM patients ORDER BY id DESC").fetchall()
        conn.close()
        self.text.delete("1.0", "end")
        for r in rows:
            self.text.insert("end", f"ID:{r['id']} Name:{r['name']} Age:{r['age']} Contact:{r['contact']} Notes:{r['notes']}\n")
