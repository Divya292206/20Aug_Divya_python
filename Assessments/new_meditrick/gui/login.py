# gui/login.py
import tkinter as tk
from tkinter import messagebox
from db import get_conn

class LoginWindow(tk.Toplevel):
    def __init__(self, master, on_success):
        super().__init__(master)
        self.title("MediTrack - Login")
        self.geometry("300x150")  # Set smaller size (width x height)
        self.resizable(False, False)  # Disable resizing
        self.on_success = on_success

        tk.Label(self, text="Username").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.user_entry = tk.Entry(self)
        self.pass_entry = tk.Entry(self, show="*")
        self.user_entry.grid(row=0, column=1)
        self.pass_entry.grid(row=1, column=1)
        tk.Button(self, text="Login", command=self.try_login).grid(row=2, column=0, columnspan=2, pady=8)

    def try_login(self):
        username = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()
        if not username or not password:
            messagebox.showerror("Error", "Enter username and password")
            return
        conn = get_conn()
        c = conn.cursor()
        user = c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()
        conn.close()
        if user:
            role = user["role"]
            self.on_success(username, role)
            self.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
