import tkinter as tk


class CheckoutItemFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        sidebar = tk.Frame(self, bg="#2c3e50", width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tabs = [
            ("Check Out to FSL", self.checkout_fsl),
            ("Check Out to Court", self.checkout_court),
            ("Home", self.home),
            ("Back", self.back)
        ]

        for text, command in tabs:
            if text == "Checkout Items":
                tab_button = tk.Button(sidebar, text=text, background="#16a085", foreground="#ecf0f1", command=command, font=(
                    "Helvetica", 12), width=20, height=2, relief=tk.FLAT)
            else:
                tab_button = tk.Button(sidebar, text=text, background="#34495e", foreground="#ecf0f1", command=command, font=(
                    "Helvetica", 12), width=20, height=2, relief=tk.FLAT)
            tab_button.pack(fill=tk.X, pady=5, padx=10)

        content_frame = tk.Frame(self, bg="#bdc3c7")
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def checkout_fsl(self):
        self.controller.show_frame("CheckoutFSLFrame")

    def checkout_court(self):
        self.controller.show_frame("CheckoutCourtFrame")

    def back(self):
        self.controller.show_frame("MalkhanaFrame")

    def home(self):
        self.controller.show_frame("MainFrame")
