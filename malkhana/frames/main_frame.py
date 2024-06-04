import tkinter as tk


class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tabs = [
            ("Malkhana", self.malkhana_frame),
            ("FSL Records", self.fsl_records_frame),
            ("Court Records", self.court_records_frame),
            ("View Logs", self.view_logs_frame),
            ("Print Details", self.print_details),
            ("Log Out", self.log_out),
        ]

        for text, command in tabs:
            if text == "Add Items":
                tab_button = tk.Button(self.sidebar, text=text, background="#16a085", foreground="#ecf0f1", command=command, font=(
                    "Helvetica", 12), width=20, height=2, relief=tk.FLAT)
            else:
                tab_button = tk.Button(self.sidebar, text=text, background="#34495e", foreground="#ecf0f1", command=command, font=(
                    "Helvetica", 12), width=20, height=2, relief=tk.FLAT)
            tab_button.pack(fill=tk.X, pady=5, padx=10)

        self.content_frame = tk.Frame(self, bg="#bdc3c7")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.content_frame, text="Main Menu")
        self.label.pack(pady=10)

    def malkhana_frame(self):
        self.controller.show_frame("MalkhanaFrame")

    def fsl_records_frame(self):
        self.controller.show_frame("FSLRecordsFrame")

    def court_records_frame(self):
        self.controller.show_frame("CourtRecordsFrame")

    def view_logs_frame(self):
        self.controller.show_frame("ItemLogsFrame")

    def print_details(self):
        self.controller.show_frame("PrintDetailsFrame")

    def log_out(self):
        self.controller.frames["LoginFrame"].username_entry.delete(0, tk.END)
        self.controller.frames["LoginFrame"].password_entry.delete(0, tk.END)
        self.controller.show_frame("LoginFrame")
