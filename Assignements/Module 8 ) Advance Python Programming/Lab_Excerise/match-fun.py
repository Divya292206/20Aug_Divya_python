# import re

# mystr = "Hello My name is Divya"

# x = re.match("My",mystr)

# print(x)

# if x:
#     print("Sucesss!")
# else:
#     print("Error!")

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import re
import csv
import io
import datetime

# --- 1. OOP Data Models (Abstraction of records) ---

class Patient:
    """Represents a Patient record."""
    def __init__(self, patient_id, name, dob, contact, history):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob  # Date of Birth (YYYY-MM-DD)
        self.contact = contact
        self.history = history # Simple medical history summary

class Appointment:
    """Represents an Appointment record."""
    def __init__(self, appointment_id, patient_id, doctor_assigned, date_time, reason, status):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_assigned = doctor_assigned
        self.date_time = date_time # YYYY-MM-DD HH:MM
        self.reason = reason
        self.status = status # e.g., 'Scheduled', 'Complete', 'Follow-up'

class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class AccessDeniedError(CustomError):
    """Raised when a user attempts an action outside their role."""
    def __init__(self, role, action):
        self.role = role
        self.action = action
        super().__init__(f"Access Denied: Role '{role}' cannot perform action '{action}'.")

# --- 2. Database Manager (SQLite3) ---

class DatabaseManager:
    """Handles all SQLite database connections and operations."""
    def __init__(self, db_name='meditrack.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()
        self._setup_db()
        self._seed_data()

    def _connect(self):
        """Establishes a connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            messagebox.showerror("DB Error", "Failed to connect to the database.")

    def _setup_db(self):
        """Creates the necessary tables if they don't exist."""
        # Note: In a real application, passwords would be hashed.
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                dob TEXT,
                contact TEXT,
                history TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY,
                patient_id INTEGER,
                doctor_assigned TEXT,
                date_time TEXT,
                reason TEXT,
                status TEXT,
                FOREIGN KEY (patient_id) REFERENCES patients(id)
            )
        """)
        self.conn.commit()

    def _seed_data(self):
        """Inserts initial user data if the user table is empty."""
        self.cursor.execute("SELECT COUNT(*) FROM users")
        if self.cursor.fetchone()[0] == 0:
            users_data = [
                ('admin', 'admin123', 'Admin'),
                ('dr_smith', 'docpass', 'Doctor'),
                ('reception', 'recpass', 'Receptionist')
            ]
            self.cursor.executemany("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", users_data)
            self.conn.commit()

        self.cursor.execute("SELECT COUNT(*) FROM patients")
        if self.cursor.fetchone()[0] == 0:
            patients_data = [
                ('Alice Johnson', '1985-05-15', '555-1234', 'Asthma, Penicillin allergy'),
                ('Bob Williams', '1992-11-20', '555-5678', 'Annual checkup')
            ]
            self.cursor.executemany("INSERT INTO patients (name, dob, contact, history) VALUES (?, ?, ?, ?)", patients_data)
            self.conn.commit()
            
            # Seed appointments
            self.cursor.execute("SELECT id FROM patients WHERE name='Alice Johnson'")
            alice_id = self.cursor.fetchone()[0]
            appointments_data = [
                (alice_id, 'dr_smith', '2025-12-10 10:00', 'Routine checkup and prescription refill', 'Complete'),
                (alice_id, 'dr_smith', '2025-12-25 14:30', 'Follow-up on respiratory condition', 'Scheduled')
            ]
            self.cursor.executemany("INSERT INTO appointments (patient_id, doctor_assigned, date_time, reason, status) VALUES (?, ?, ?, ?, ?)", appointments_data)
            self.conn.commit()


    # CRUD Operations
    def execute_query(self, query, params=()):
        """Execute a general query and commit."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            messagebox.showerror("DB Operation Error", f"An error occurred: {e}")
            return False

    def fetch_all(self, query, params=()):
        """Execute a query and fetch all results."""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()

# --- 3. Tkinter GUI Application ---

class MediTrackApp(tk.Tk):
    """The main application class, managing GUI and business logic."""
    def __init__(self):
        super().__init__()
        self.title("MediTrack - Healthcare Management")
        self.geometry("900x600")
        self.db = DatabaseManager()
        self.current_user = None
        self.current_role = None
        
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#e0f7fa')
        self.style.configure('TLabel', background='#e0f7fa', font=('Inter', 10))
        self.style.configure('TButton', font=('Inter', 10, 'bold'), padding=6, background='#00bcd4', foreground='white')
        self.style.map('TButton', background=[('active', '#0097a7')])
        self.style.configure('Header.TLabel', font=('Inter', 16, 'bold'), foreground='#0097a7')
        self.style.configure('Menu.TButton', font=('Inter', 12, 'bold'), background='#4db6ac', foreground='white')
        self.style.map('Menu.TButton', background=[('active', '#26a69a')])


        self.container = tk.Frame(self, bg='#e0f7fa')
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        self._create_frames()
        self.show_frame("LoginFrame")

    def _create_frames(self):
        """Initializes and registers all main frames."""
        for F in (LoginFrame, DashboardFrame, PatientFrame, AppointmentFrame, BillingFrame, ReportFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        """Brings the requested frame to the front."""
        frame = self.frames[page_name]
        frame.tkraise()

    def login(self, username, password):
        """Authenticates user and sets role."""
        if not username or not password:
            messagebox.showerror("Login Error", "Please enter both username and password.")
            return

        user_data = self.db.fetch_all("SELECT username, role FROM users WHERE username=? AND password=?", (username, password))

        if user_data:
            self.current_user = user_data[0][0]
            self.current_role = user_data[0][1]
            messagebox.showinfo("Success", f"Welcome, {self.current_user} ({self.current_role})!")
            self.frames["DashboardFrame"].update_role_info()
            self.show_frame("DashboardFrame")
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def logout(self):
        """Logs out the current user and returns to the login screen."""
        self.current_user = None
        self.current_role = None
        messagebox.showinfo("Logout", "You have been logged out.")
        self.show_frame("LoginFrame")
    
    # --- Billing Logic (File I/O and Calculation) ---
    def generate_invoice(self, patient_id, consultation_charge, medicine_cost, tax_rate=0.10):
        """Calculates billing, handles errors, and saves invoice to CSV."""
        try:
            consultation_charge = float(consultation_charge)
            medicine_cost = float(medicine_cost)
            tax_rate = float(tax_rate)

            if consultation_charge < 0 or medicine_cost < 0:
                raise ValueError("Charges cannot be negative.")
                
            tax_amount = (consultation_charge + medicine_cost) * tax_rate
            total_due = consultation_charge + medicine_cost + tax_amount
            
            # Fetch patient name for the invoice file
            patient_record = self.db.fetch_all("SELECT name FROM patients WHERE id=?", (patient_id,))
            if not patient_record:
                messagebox.showerror("Billing Error", f"Patient ID {patient_id} not found.")
                return

            patient_name = patient_record[0][0].replace(' ', '_')
            filename = f"invoice_{patient_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

            # Use in-memory string IO to prepare the CSV content
            output = io.StringIO()
            writer = csv.writer(output)
            
            writer.writerow(['Field', 'Value'])
            writer.writerow(['Invoice ID', datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')])
            writer.writerow(['Patient ID', patient_id])
            writer.writerow(['Patient Name', patient_record[0][0]])
            writer.writerow(['Consultation Charge', consultation_charge])
            writer.writerow(['Medicine Cost', medicine_cost])
            writer.writerow(['Tax Rate (10%)', f"{tax_rate*100}%"])
            writer.writerow(['Tax Amount', round(tax_amount, 2)])
            writer.writerow(['TOTAL DUE', round(total_due, 2)])
            
            csv_content = output.getvalue()
            
            # File I/O: Write to the local file system
            with open(filename, 'w', newline='') as f:
                f.write(csv_content)

            messagebox.showinfo("Success", f"Invoice generated successfully and saved as {filename}")

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid charge or ID format: {e}")
        except Exception as e:
            # General exception handling for file system errors or unexpected issues
            messagebox.showerror("Critical Error", f"An unexpected error occurred during billing: {e}")

# --- 4. Tkinter Frames (GUI Components) ---

class LoginFrame(ttk.Frame):
    """The initial login screen."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Layout configuration
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(5, weight=1)

        login_panel = ttk.Frame(self, padding="30 20", relief='groove')
        login_panel.grid(row=1, column=1, sticky="nsew")

        ttk.Label(login_panel, text="MediTrack Login", style='Header.TLabel').grid(row=0, column=0, columnspan=2, pady=20)

        # Username
        ttk.Label(login_panel, text="Username:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.username_entry = ttk.Entry(login_panel)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        self.username_entry.insert(0, 'reception')

        # Password
        ttk.Label(login_panel, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.password_entry = ttk.Entry(login_panel, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        self.password_entry.insert(0, 'recpass')

        # Login Button
        ttk.Button(login_panel, text="Login", command=self._handle_login).grid(row=3, column=0, columnspan=2, pady=20, sticky='ew')
        
        # Bind <Return> to login function
        self.bind('<Return>', lambda e: self._handle_login())

    def _handle_login(self):
        """Calls the main controller's login method."""
        uname = self.username_entry.get()
        pword = self.password_entry.get()
        self.controller.login(uname, pword)

class DashboardFrame(ttk.Frame):
    """The main application dashboard with role-based features."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Main Layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)

        # Header Frame
        header = ttk.Frame(self)
        header.grid(row=0, column=0, columnspan=2, sticky='ew', padx=10, pady=10)
        self.role_label = ttk.Label(header, text="Logged in as: ", font=('Inter', 12, 'bold'), foreground='#0097a7')
        self.role_label.pack(side=tk.LEFT)
        ttk.Button(header, text="Logout", command=self.controller.logout, style='TButton').pack(side=tk.RIGHT)

        # Navigation Menu (Column 0)
        menu_frame = ttk.Frame(self, width=200, style='TFrame')
        menu_frame.grid(row=1, column=0, sticky='ns', padx=10, pady=10)
        
        ttk.Label(menu_frame, text="Main Menu", style='Header.TLabel').pack(pady=10)

        self.buttons = [
            ("Patient Management", "PatientFrame"),
            ("Appointment Scheduling", "AppointmentFrame"),
            ("Billing & Invoicing", "BillingFrame"),
            ("Regex Reports", "ReportFrame")
        ]

        for text, frame_name in self.buttons:
            ttk.Button(menu_frame, text=text, style='Menu.TButton', 
                       command=lambda name=frame_name: controller.show_frame(name)).pack(fill='x', padx=10, pady=5)
            
        # Main Content Area (Column 1)
        self.content_frame = ttk.Frame(self, style='TFrame', padding="20")
        self.content_frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
        ttk.Label(self.content_frame, text="Welcome to MediTrack!", style='Header.TLabel').pack(pady=20)
        ttk.Label(self.content_frame, text="Use the menu on the left to navigate the system.", style='TLabel').pack()
        ttk.Label(self.content_frame, text="Current Date/Time: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), style='TLabel').pack(pady=10)
        
    def update_role_info(self):
        """Updates the role display label on the dashboard."""
        if self.controller.current_role:
            self.role_label.config(text=f"Logged in as: {self.controller.current_user} ({self.controller.current_role})")

class PatientFrame(ttk.Frame):
    """Frame for creating and viewing patient profiles."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.db = controller.db
        
        self.patient_id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.contact_var = tk.StringVar()
        self.history_text = tk.Text(self, height=5, width=40)

        self._build_ui()

    def _build_ui(self):
        """Lays out the Patient Management UI."""
        ttk.Label(self, text="Patient Management", style='Header.TLabel').pack(pady=10)
        
        # Form
        form_frame = ttk.Frame(self, padding=10)
        form_frame.pack(pady=10, padx=10)

        # Row 0: Patient ID (for lookup/update)
        ttk.Label(form_frame, text="Patient ID (Lookup):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(form_frame, textvariable=self.patient_id_var).grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        ttk.Button(form_frame, text="Load Patient", command=self._load_patient).grid(row=0, column=2, padx=5, pady=5)

        # Row 1: Name
        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(form_frame, textvariable=self.name_var).grid(row=1, column=1, padx=5, pady=5, sticky='ew', columnspan=2)

        # Row 2: DOB
        ttk.Label(form_frame, text="DOB (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(form_frame, textvariable=self.dob_var).grid(row=2, column=1, padx=5, pady=5, sticky='ew', columnspan=2)

        # Row 3: Contact
        ttk.Label(form_frame, text="Contact:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(form_frame, textvariable=self.contact_var).grid(row=3, column=1, padx=5, pady=5, sticky='ew', columnspan=2)

        # Row 4: History
        ttk.Label(form_frame, text="Medical History:").grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.history_text.grid(row=4, column=1, padx=5, pady=5, sticky='ew', columnspan=2)

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Create Profile", command=self._create_patient).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Update Profile", command=self._update_patient).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Back to Dashboard", command=lambda: self.controller.show_frame("DashboardFrame")).pack(side=tk.LEFT, padx=5)

    def _clear_form(self):
        """Clears all input fields."""
        self.patient_id_var.set("")
        self.name_var.set("")
        self.dob_var.set("")
        self.contact_var.set("")
        self.history_text.delete(1.0, tk.END)

    def _create_patient(self):
        """Creates a new patient record."""
        try:
            if self.controller.current_role not in ['Admin', 'Receptionist']:
                raise AccessDeniedError(self.controller.current_role, "Create Patient Profile")
            
            name = self.name_var.get()
            dob = self.dob_var.get()
            contact = self.contact_var.get()
            history = self.history_text.get(1.0, tk.END).strip()

            if not all([name, dob, contact]):
                 messagebox.showerror("Input Error", "Name, DOB, and Contact fields are required.")
                 return

            if self.db.execute_query("INSERT INTO patients (name, dob, contact, history) VALUES (?, ?, ?, ?)", (name, dob, contact, history)):
                # Get the ID of the newly created patient
                new_id = self.db.cursor.lastrowid 
                new_patient = Patient(new_id, name, dob, contact, history)
                messagebox.showinfo("Success", f"Patient created successfully! ID: {new_patient.patient_id}")
                self._clear_form()

        except AccessDeniedError as e:
            messagebox.showerror("Permission Denied", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            
    def _load_patient(self):
        """Loads patient data into the form for updating."""
        try:
            patient_id = self.patient_id_var.get()
            if not patient_id.isdigit():
                messagebox.showerror("Input Error", "Patient ID must be a number.")
                return

            record = self.db.fetch_all("SELECT name, dob, contact, history FROM patients WHERE id=?", (patient_id,))

            if record:
                self.name_var.set(record[0][0])
                self.dob_var.set(record[0][1])
                self.contact_var.set(record[0][2])
                self.history_text.delete(1.0, tk.END)
                self.history_text.insert(1.0, record[0][3])
                messagebox.showinfo("Loaded", f"Patient ID {patient_id} loaded successfully.")
            else:
                messagebox.showerror("Not Found", f"Patient ID {patient_id} does not exist.")
                self._clear_form()
                self.patient_id_var.set(patient_id) # Keep the ID for retry
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def _update_patient(self):
        """Updates an existing patient record."""
        try:
            if self.controller.current_role not in ['Admin', 'Receptionist']:
                raise AccessDeniedError(self.controller.current_role, "Update Patient Profile")
                
            patient_id = self.patient_id_var.get()
            name = self.name_var.get()
            dob = self.dob_var.get()
            contact = self.contact_var.get()
            history = self.history_text.get(1.0, tk.END).strip()

            if not patient_id.isdigit():
                messagebox.showerror("Input Error", "Patient ID must be a number.")
                return

            if self.db.execute_query("UPDATE patients SET name=?, dob=?, contact=?, history=? WHERE id=?", 
                                     (name, dob, contact, history, patient_id)):
                messagebox.showinfo("Success", f"Patient ID {patient_id} updated successfully.")
            else:
                messagebox.showerror("Error", "Update failed. Check ID.")

        except AccessDeniedError as e:
            messagebox.showerror("Permission Denied", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

class AppointmentFrame(ttk.Frame):
    """Frame for scheduling and viewing appointments."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.db = controller.db
        
        # Input Variables
        self.patient_id_var = tk.StringVar()
        self.doctor_var = tk.StringVar()
        self.date_time_var = tk.StringVar(value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.reason_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Scheduled")

        self._build_ui()

    def _build_ui(self):
        """Lays out the Appointment UI."""
        ttk.Label(self, text="Appointment Scheduling & Tracking", style='Header.TLabel').pack(pady=10)
        
        # Form
        form_frame = ttk.Frame(self, padding=10)
        form_frame.pack(pady=10, padx=10)

        # Inputs
        fields = [
            ("Patient ID:", self.patient_id_var),
            ("Doctor Assigned:", self.doctor_var),
            ("Date/Time (Y-M-D H:M):", self.date_time_var),
            ("Reason:", self.reason_var),
        ]
        
        for i, (label_text, var) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky='w')
            ttk.Entry(form_frame, textvariable=var).grid(row=i, column=1, padx=5, pady=5, sticky='ew')
            
        # Status Dropdown
        ttk.Label(form_frame, text="Status:").grid(row=len(fields), column=0, padx=5, pady=5, sticky='w')
        status_options = ["Scheduled", "Complete", "Cancelled", "Follow-up"]
        ttk.Combobox(form_frame, textvariable=self.status_var, values=status_options, state='readonly').grid(row=len(fields), column=1, padx=5, pady=5, sticky='ew')


        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Schedule Appointment", command=self._schedule_appointment).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="View All Appointments", command=self._view_appointments).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Back to Dashboard", command=lambda: self.controller.show_frame("DashboardFrame")).pack(side=tk.LEFT, padx=5)

    def _schedule_appointment(self):
        """Schedules a new appointment."""
        try:
            if self.controller.current_role not in ['Admin', 'Receptionist']:
                raise AccessDeniedError(self.controller.current_role, "Schedule Appointment")
            
            p_id = self.patient_id_var.get()
            doctor = self.doctor_var.get()
            dt = self.date_time_var.get()
            reason = self.reason_var.get()
            status = self.status_var.get()
            
            if not p_id.isdigit():
                messagebox.showerror("Input Error", "Patient ID must be a number.")
                return
            
            # Check if patient exists
            if not self.db.fetch_all("SELECT id FROM patients WHERE id=?", (p_id,)):
                messagebox.showerror("Error", f"Patient ID {p_id} not found.")
                return

            if self.db.execute_query("INSERT INTO appointments (patient_id, doctor_assigned, date_time, reason, status) VALUES (?, ?, ?, ?, ?)", 
                                     (p_id, doctor, dt, reason, status)):
                # Note: No need to instantiate Appointment class for simple DB save, but we can here for demonstration:
                # new_appt = Appointment(self.db.cursor.lastrowid, p_id, doctor, dt, reason, status)
                messagebox.showinfo("Success", f"Appointment scheduled for Patient {p_id}.")
                self.patient_id_var.set("")
                self.doctor_var.set("")
                self.reason_var.set("")

        except AccessDeniedError as e:
            messagebox.showerror("Permission Denied", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def _view_appointments(self):
        """Displays all appointments in a new Toplevel window."""
        # This is allowed for all roles as it's viewing history/schedule
        
        view_window = tk.Toplevel(self.controller)
        view_window.title("All Appointments")
        view_window.geometry("800x400")
        
        # Fetch all appointments with patient name join
        query = """
            SELECT a.id, p.name, a.doctor_assigned, a.date_time, a.reason, a.status 
            FROM appointments a JOIN patients p ON a.patient_id = p.id
            ORDER BY a.date_time DESC
        """
        records = self.db.fetch_all(query)
        
        # Create Treeview
        tree = ttk.Treeview(view_window, columns=('ID', 'Patient Name', 'Doctor', 'Date/Time', 'Reason', 'Status'), show='headings')
        tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Configure columns and headings
        for col in tree['columns']:
            tree.heading(col, text=col, anchor=tk.W)
            tree.column(col, width=100)
            
        tree.column('ID', width=30)
        tree.column('Patient Name', width=150)
        tree.column('Date/Time', width=120)
        tree.column('Reason', width=200)

        # Insert data
        for record in records:
            tree.insert('', tk.END, values=record)

class BillingFrame(ttk.Frame):
    """Frame for calculating and generating patient invoices."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.p_id_var = tk.StringVar()
        self.consult_var = tk.StringVar()
        self.med_var = tk.StringVar()

        self._build_ui()

    def _build_ui(self):
        """Lays out the Billing UI."""
        ttk.Label(self, text="Billing and Invoice Generation", style='Header.TLabel').pack(pady=10)
        
        form_frame = ttk.Frame(self, padding=10)
        form_frame.pack(pady=10, padx=10)

        fields = [
            ("Patient ID:", self.p_id_var, 'Enter Patient ID'),
            ("Consultation Charge:", self.consult_var, 'e.g., 150.00'),
            ("Medicine/Procedure Cost:", self.med_var, 'e.g., 50.00'),
        ]
        
        for i, (label_text, var, placeholder) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky='w')
            entry = ttk.Entry(form_frame, textvariable=var)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky='ew')
            entry.insert(0, placeholder)
            
        ttk.Label(form_frame, text="Tax Rate: 10% (Fixed for demo)").grid(row=len(fields), column=0, columnspan=2, padx=5, pady=10)


        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Generate & Save Invoice (CSV)", command=self._handle_billing).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Back to Dashboard", command=lambda: self.controller.show_frame("DashboardFrame")).pack(side=tk.LEFT, padx=5)

    def _handle_billing(self):
        """Validates input and calls the invoice generation logic."""
        try:
            if self.controller.current_role not in ['Admin', 'Receptionist']:
                raise AccessDeniedError(self.controller.current_role, "Generate Billing")

            p_id = self.p_id_var.get()
            consult = self.consult_var.get()
            med = self.med_var.get()
            
            if not p_id.isdigit():
                messagebox.showerror("Input Error", "Patient ID must be a number.")
                return

            self.controller.generate_invoice(p_id, consult, med)
            
        except AccessDeniedError as e:
            messagebox.showerror("Permission Denied", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

class ReportFrame(ttk.Frame):
    """Frame for generating reports using Regular Expressions."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.db = controller.db
        
        self.regex_pattern_var = tk.StringVar(value="Follow-up|Routine")

        self._build_ui()

    def _build_ui(self):
        """Lays out the Reporting UI."""
        ttk.Label(self, text="Regex-Based Appointment Reports", style='Header.TLabel').pack(pady=10)
        ttk.Label(self, text="Search Reason/Status using Regular Expression:", style='TLabel').pack(pady=5)
        
        search_frame = ttk.Frame(self, padding=10)
        search_frame.pack(pady=5, padx=10)

        ttk.Entry(search_frame, textvariable=self.regex_pattern_var, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Run Report", command=self._run_regex_report).pack(side=tk.LEFT, padx=5)

        # Treeview for results
        self.tree = ttk.Treeview(self, columns=('ID', 'Patient Name', 'Doctor', 'Date/Time', 'Reason', 'Status'), show='headings')
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        for col in self.tree['columns']:
            self.tree.heading(col, text=col, anchor=tk.W)
            self.tree.column(col, width=120)
        self.tree.column('ID', width=30)
        self.tree.column('Reason', width=200)

        ttk.Button(self, text="Back to Dashboard", command=lambda: self.controller.show_frame("DashboardFrame")).pack(pady=10)

    def _run_regex_report(self):
        """Fetches and filters appointments using the user-provided regex pattern."""
        try:
            if self.controller.current_role not in ['Admin', 'Doctor']:
                raise AccessDeniedError(self.controller.current_role, "Generate Regex Report")
                
            pattern = self.regex_pattern_var.get()
            
            # Clear previous results
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            # Fetch all appointments with patient name join
            query = """
                SELECT a.id, p.name, a.doctor_assigned, a.date_time, a.reason, a.status 
                FROM appointments a JOIN patients p ON a.patient_id = p.id
            """
            all_records = self.db.fetch_all(query)
            
            compiled_regex = re.compile(pattern, re.IGNORECASE)
            
            filtered_count = 0
            # Iterate and filter using regex
            for record in all_records:
                appt_id, p_name, doctor, dt, reason, status = record
                
                # Check if the regex matches in either the reason or the status
                if compiled_regex.search(reason) or compiled_regex.search(status):
                    self.tree.insert('', tk.END, values=record)
                    filtered_count += 1
                    
            messagebox.showinfo("Report Complete", f"{filtered_count} appointments matched the pattern '{pattern}'.")

        except AccessDeniedError as e:
            messagebox.showerror("Permission Denied", str(e))
        except re.error as e:
            messagebox.showerror("Regex Error", f"Invalid Regular Expression: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


# --- 5. Application Startup ---

if __name__ == "__main__":
    app = MediTrackApp()
    app.mainloop()

# Cleanup database connection when the application exits
if 'app' in locals():
    app.db.close()