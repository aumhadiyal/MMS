import tkinter as tk


class MalkhanaFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tabs = [
            ("Add Items", self.add_item),
            ("View Items", self.view_items),
            ("Checkout Items", self.checkout_item),
            ("Checkin Items", self.checkin_item),
            ("Back", self.go_back),
            ("Log Out", self.log_out),
        ]

        for text, command in tabs:
            tab_button = tk.Button(self.sidebar, text=text, background="#34495e", foreground="#ecf0f1", command=command, font=(
                "Helvetica", 12), width=20, height=2, relief=tk.FLAT)
            tab_button.pack(fill=tk.X, pady=5, padx=10)

        self.content_frame = tk.Frame(self, bg="#bdc3c7")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.welcome_label = tk.Label(
            self.content_frame, text="Malkhana Page", font=("Helvetica", 20), bg="#bdc3c7")
        self.welcome_label.pack(pady=20)
        self.instructions_label = tk.Label(
            self.content_frame, text="You can Add, View, Checkin, Checkout items", font=("Helvetica", 20), bg="#bdc3c7")
        self.instructions_label.pack(pady=20)

    def add_item(self):
        self.controller.show_frame("AddItemsFrame")

    def view_items(self):
        self.controller.show_frame("ViewItemsFrame")

    def checkout_item(self):
        self.clear_content_frame()

    def checkin_item(self):
        self.clear_content_frame()

    def go_back(self):
        self.controller.show_frame("MainFrame")

    def log_out(self):
        self.controller.frames["LoginFrame"].username_entry.delete(0, tk.END)
        self.controller.frames["LoginFrame"].password_entry.delete(0, tk.END)
        self.controller.show_frame("LoginFrame")

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
