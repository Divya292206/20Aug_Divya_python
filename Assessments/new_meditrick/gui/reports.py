# reports.py
import re
import sqlite3
from db import get_conn
from typing import List, Dict

def regex_search_patients(pattern: str) -> List[Dict]:
    """
    Search disease names or patient notes/ status with regex pattern.
    Example: pattern = r'Followup' or r'covid|fever'
    """
    conn = get_conn()
    c = conn.cursor()
    rows = []
    try:
        patients = c.execute("SELECT * FROM patients").fetchall()
        prog = re.compile(pattern, re.IGNORECASE)
        for p in patients:
            # check name, notes
            if prog.search(str(p["name"])) or prog.search(str(p["notes"])):
                rows.append(dict(p))
        # Also search appointments reason/status
        appts = c.execute("SELECT a.*, p.name as patient_name FROM appointments a LEFT JOIN patients p ON a.patient_id = p.id").fetchall()
        for a in appts:
            if prog.search(str(a["reason"])) or prog.search(str(a["status"])):
                rows.append(dict(a))
    finally:
        conn.close()
    return rows
