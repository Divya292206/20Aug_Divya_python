# gui/appointment_form.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from db import get_conn
from datetime import datetime

class AppointmentForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Appointments")
        tk.Button(self, text="Add Appointment", command=self.add_appointment).pack(pady=6)
        tk.Button(self, text="List Appointments", command=self.list_appts).pack(pady=6)
        self.txt = tk.Text(self, width=90, height=20)
        self.txt.pack()

    def add_appointment(self):
        try:
            pid = simpledialog.askinteger("Patient ID", "Enter patient ID:", parent=self)
            if not pid:
                return
            doctor = simpledialog.askstring("Doctor", "Doctor name:", parent=self)
            dt_str = simpledialog.askstring("Datetime", "Enter datetime YYYY-MM-DD HH:MM:", parent=self)
            dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
            reason = simpledialog.askstring("Reason", "Reason/diagnosis:", parent=self)
            status = "Scheduled"
            conn = get_conn()
            c = conn.cursor()
            c.execute("INSERT INTO appointments (patient_id, doctor, datetime, reason, status) VALUES (?, ?, ?, ?, ?)",
                      (pid, doctor or "", dt.isoformat(), reason or "", status))
            conn.commit()
            messagebox.showinfo("Success", "Appointment added.")
        except ValueError:
            messagebox.showerror("Error", "Invalid datetime format. Use YYYY-MM-DD HH:MM")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            try:
                conn.close()
            except:
                pass

    def list_appts(self):
        conn = get_conn()
        c = conn.cursor()
        rows = c.execute("SELECT a.*, p.name as patient_name FROM appointments a LEFT JOIN patients p ON a.patient_id = p.id ORDER BY a.datetime DESC").fetchall()
        conn.close()
        self.txt.delete("1.0", "end")
        for r in rows:
            self.txt.insert("end", f"ID:{r['id']} Patient:{r['patient_name']} Doctor:{r['doctor']} Date:{r['datetime']} Status:{r['status']} Reason:{r['reason']}\n")
