import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
from malkhana.frames.MiscFuncs import MiscFuncs
from malkhana.frames.view_items_frame import ViewItemsFrame
from malkhana.models.Item import Item
from malkhana.models.Log import Logs


class AddItemsFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.create_widgets()
        self.file_entry = ""
        self.item = Item()
        self.log = Logs()
        # self.misc = MiscFuncs(self.parent, self.controller)

    def create_widgets(self):
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tabs = [
            ("Add Items", None),
            ("View Items", self.view_item),
            ("Checkout Items", self.checkout_item),
            ("Checkin Items", self.checkin_item),
            ("Back", self.go_back),
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

        # Define fonts
        textbox_font = ('Helvetica', 12)
        font_style = ('Helvetica', 12)

        self.barcode_label = tk.Label(
            self.content_frame, text="Barcode Number:", background="#f6f4f2", font=font_style)
        self.barcode_label.pack(padx=10, pady=5, anchor="w")
        self.barcode_entry = tk.Entry(
            self.content_frame, background="#FFFFFF", font=textbox_font)
        self.barcode_entry.pack(padx=10, pady=5, anchor="w")

        self.fir_label = tk.Label(
            self.content_frame, text="FIR Number:", background="#f6f4f2", font=font_style)
        self.fir_label.pack(padx=10, pady=5, anchor="w")
        self.fir_no_entry = tk.Entry(
            self.content_frame, background="#FFFFFF", font=textbox_font)
        self.fir_no_entry.pack(padx=10, pady=5, anchor="w")

        self.seized_items_label = tk.Label(
            self.content_frame, text="Seized Items:", background="#f6f4f2", font=font_style)
        self.seized_items_label.pack(padx=10, pady=5, anchor="w")
        self.seized_items_entry = tk.Entry(
            self.content_frame, background="#FFFFFF", font=textbox_font)
        self.seized_items_entry.pack(padx=10, pady=5, anchor="w")

        self.ipc_section_label = tk.Label(
            self.content_frame, text="IPC Section:", background="#f6f4f2", font=font_style)
        self.ipc_section_label.pack(padx=10, pady=5, anchor="w")
        self.ipc_section_entry = tk.Entry(
            self.content_frame, background="#FFFFFF", font=textbox_font)
        self.ipc_section_entry.pack(padx=10, pady=5, anchor="w")

        self.crime_location_label = tk.Label(
            self.content_frame, text="Crime Location:", background="#f6f4f2", font=font_style)
        self.crime_location_label.pack(padx=10, pady=5, anchor="w")
        self.crime_location_entry = tk.Entry(
            self.content_frame, background="#FFFFFF", font=textbox_font)
        self.crime_location_entry.pack(padx=10, pady=5, anchor="w")

        self.crime_date_label = tk.Label(
            self.content_frame, text="Crime Date:", background="#f6f4f2", font=font_style)
        self.crime_date_label.pack(padx=10, pady=5, anchor="w")
        self.crime_date_entry = DateEntry(self.content_frame, font=textbox_font,
                                          width=12, background='darkblue', foreground='white', borderwidth=2)
        self.crime_date_entry.pack(padx=10, pady=5, anchor="w")

        self.crime_time_label = tk.Label(
            self.content_frame, text="Crime Time:", background="#f6f4f2", font=font_style)
        self.crime_time_label.pack(padx=10, pady=5, anchor="w")
        self.time_frame = tk.Frame(self.content_frame, bg="#f6f4f2")
        self.time_frame.pack(padx=10, pady=5, anchor="w")

        self.hour_var = tk.StringVar(self.time_frame, value='00')
        self.hour_menu = ttk.Combobox(self.time_frame, font=textbox_font, textvariable=self.hour_var, values=[
            str(i).zfill(2) for i in range(24)], state='readonly', width=5)

        self.minute_var = tk.StringVar(self.time_frame, value='00')
        self.minute_menu = ttk.Combobox(self.time_frame, font=textbox_font, textvariable=self.minute_var, values=[
            str(i).zfill(2) for i in range(60)], state='readonly', width=5)

        self.hour_menu.pack(side=tk.LEFT, pady=5)
        self.minute_menu.pack(side=tk.LEFT, padx=10, pady=5)

        self.crime_witness_label = tk.Label(
            self.content_frame, text="Crime Witnesses:", background="#f6f4f2", font=font_style)
        self.crime_witness_label.pack(padx=10, pady=5, anchor="w")
        self.crime_witness_entry = tk.Entry(
            self.content_frame, background="#FFFFFF", font=textbox_font)
        self.crime_witness_entry.pack(padx=10, pady=5, anchor="w")

        self.crime_inspector_label = tk.Label(
            self.content_frame, text="Crime Inspector:", background="#f6f4f2", font=font_style)
        self.crime_inspector_label.pack(
            padx=10, pady=5, anchor="w")
        self.crime_inspector_entry = tk.Entry(
            self.content_frame, background="#FFFFFF", font=textbox_font)
        self.crime_inspector_entry.pack(padx=10, pady=5, anchor="w")

        self.where_kept_label = tk.Label(
            self.content_frame, text="Where Kept:", background="#f6f4f2", font=font_style)
        self.where_kept_label.pack(padx=10, pady=5, anchor="w")
        self.where_kept_entry = tk.Entry(
            self.content_frame, background="#FFFFFF", font=textbox_font)
        self.where_kept_entry.pack(padx=10, pady=5, anchor="w")

        self.description_label = tk.Label(
            self.content_frame, text="Description of Item:", background="#f6f4f2", font=font_style)
        self.description_label.pack(padx=10, pady=5, anchor="w")
        self.description_of_items_entry = tk.Entry(
            self.content_frame, background="#FFFFFF", font=textbox_font)
        self.description_of_items_entry.pack(padx=10, pady=5, anchor="w")

        crime_hour = int(self.hour_var.get())
        crime_minute = int(self.minute_var.get())
        crime_time = f"{crime_hour:02d}:{crime_minute:02d}"
        entry_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        button_font = ('Helvetica', 12)
        button_width = 20
        button_height = 2

        self.add_attachment_button = tk.Button(
            self.content_frame, text="Add Attachment", background="#f6f4f2", command=self.browse_file, font=button_font, width=button_width, height=button_height)
        self.add_attachment_button.pack(
            padx=10, pady=5, anchor="w")

        self.add_item_button = tk.Button(self.content_frame, text="Add Item",
                                         background="#f6f4f2", command=lambda: self.add_item(self.barcode_entry.get(), self.fir_no_entry.get(), self.seized_items_entry.get(), self.ipc_section_entry.get(), self.crime_location_entry.get(), self.crime_date_entry.get(), crime_time, self.crime_witness_entry.get(), self.crime_inspector_entry.get(), self.where_kept_entry.get(), self.description_of_items_entry.get(), entry_time, self.file_entry), font=button_font, width=button_width, height=button_height)
        self.add_item_button.pack(padx=10, pady=5, side=tk.LEFT)

        self.back_button = tk.Button(self.content_frame, text="Back",
                                     background="#f6f4f2", command=self.go_back, font=button_font, width=button_width, height=button_height)
        self.back_button.pack(padx=10, pady=5, side=tk.LEFT)

        self.home_button = tk.Button(self.content_frame, text="Home",
                                     background="#f6f4f2", command=self.go_home, font=button_font, width=button_width, height=button_height)
        self.home_button.pack(padx=10, pady=5, side=tk.LEFT)

        self.logout = tk.Button(self.content_frame, text="Log Out",
                                background="#f6f4f2", command=self.log_out, font=button_font, width=button_width, height=button_height)
        self.logout.pack(padx=10, pady=5, side=tk.LEFT)

    def add_item(self, barcode, fir_no, seized_items, ipc_section, crime_location, crime_date, crime_time, crime_witness, crime_inspector, where_kept, description_of_items, entry_time, attachments):
        try:
            self.item.insert_item(barcode, fir_no, seized_items, ipc_section, crime_location, crime_date, crime_time, crime_witness,
                                  crime_inspector, "Malkhana", where_kept, description_of_items, entry_time, attachments)
            MiscFuncs.entry_clearer(self)
            activity = "Added item barcode no: "+barcode
            messagebox.showinfo(
                "Successful", "Item Stored Successfully!" + activity)
            activity = "Added item to Malkhana"
            self.log.log_item(barcode, activity, entry_time)

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

    def browse_file(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            self.file_entry = ", ".join(file_paths)

    def view_item(self):
        self.controller.show_frame("ViewItemsFrame")
        view = ViewItemsFrame(self.parent, self.controller)
        view.populate_tree()
        pass

    def checkout_item(self):
        self.controller.show_frame("CheckoutItemFrame")

    def checkin_item(self):
        MiscFuncs.entry_clearer(self)

    def go_back(self):
        self.controller.show_frame("MalkhanaFrame")

    def go_home(self):
        self.controller.show_frame("MainFrame")

    def log_out(self):

        self.controller.show_frame("LoginFrame")
