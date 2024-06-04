import tkinter as tk
from tkinter import messagebox, ttk
from malkhana.models.User import User


class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user = User()
        self.create_widgets()

    def create_widgets(self):
        self.configure(background="#fafafa")

        style = ttk.Style()
        style.theme_use('clam')  # Change to a different theme
        style.configure('Green.TLabel', foreground='#1b4e39',
                        font=("Helvetica", 28, "bold"))
        style.configure('TLabel', font=("Helvetica", 16),
                        background="#fafafa", foreground="#333")
        style.configure('TButton', font=("Helvetica", 16),
                        background="#1b4e39", foreground="white")

        # Title label
        title_label = ttk.Label(
            self, text="Malkhana Management Software", style='Green.TLabel')
        title_label.pack(pady=(50, 20))

        # Username label and entry
        username_label = ttk.Label(self, text="Username:", style='TLabel')
        username_label.pack(pady=10)
        self.username_entry = ttk.Entry(
            self, font=("Helvetica", 16), takefocus=True)
        self.username_entry.pack(pady=5)

        # Password label and entry
        password_label = ttk.Label(self, text="Password:", style='TLabel')
        password_label.pack(pady=10)
        self.password_entry = ttk.Entry(
            self, show="*", font=("Helvetica", 16), takefocus=True)
        self.password_entry.pack(pady=5)

        # Login button
        login_button = ttk.Button(
            self, text="Login", command=self.login, style='TButton')
        login_button.pack(pady=(20, 10))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user.check_credentials(username, password):
            messagebox.showinfo("Successful", "Login Successful!")
            self.controller.show_frame("MainFrame")
        else:
            messagebox.showerror("Error", "Wrong Username or Password.")
