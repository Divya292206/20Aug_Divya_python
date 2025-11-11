# main.py
import tkinter as tk
from db import init_db
from gui.login import LoginWindow
from gui.dashboard import Dashboard

def start_app():
    init_db()
    root = tk.Tk()
    root.title("MediTrack")
    root.geometry("200x200")

    def on_login_success(username, role):
        for widget in root.winfo_children():
            widget.destroy()
        Dashboard(root, username, role)

    # show login dialog
    login = LoginWindow(root, on_login_success)
    root.mainloop()

if __name__ == "__main__":
    start_app()
