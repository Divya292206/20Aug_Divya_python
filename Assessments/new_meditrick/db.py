# db.py
import sqlite3
from sqlite3 import Connection
from datetime import datetime
import os

DB_FILE = "meditrack.db"

def get_conn() -> Connection:
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()

    # Users table
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    # Patients
    c.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        contact TEXT,
        notes TEXT
    )
    ''')

    # Appointments
    c.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        doctor TEXT,
        datetime TEXT,
        reason TEXT,
        status TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    ''')

    # Prescriptions (linked to appointment)
    c.execute('''
    CREATE TABLE IF NOT EXISTS prescriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        appointment_id INTEGER,
        drug_name TEXT,
        qty INTEGER,
        unit_price REAL,
        FOREIGN KEY(appointment_id) REFERENCES appointments(id)
    )
    ''')

    # Invoices
    c.execute('''
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        appointment_id INTEGER,
        consultation_fee REAL,
        medicines_total REAL,
        tax_percent REAL,
        created_at TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id),
        FOREIGN KEY(appointment_id) REFERENCES appointments(id)
    )
    ''')

    # Seed a default admin user if not exists
    c.execute("SELECT COUNT(*) as c FROM users")
    if c.fetchone()["c"] == 0:
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ("admin", "admin123", "admin"))
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ("reception", "rec123", "receptionist"))
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ("doc1", "doc123", "doctor"))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
