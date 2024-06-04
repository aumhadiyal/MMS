import tkinter as tk
from tkinter import ttk

# Assuming the Item class is defined in malkhana/models/Item.py
from malkhana.frames.MiscFuncs import MiscFuncs
from malkhana.models.Item import Item


class ViewItemsFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.item = Item()
        self.create_widgets()
        self.populate_tree()

    def create_widgets(self):
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tabs = [
            ("Add Items", self.add_item),
            ("View Items", None),
            ("Checkout Items", self.checkout_item),
            ("Checkin Items", self.checkin_item),
            ("Back", self.go_back),
            ("Log Out", self.log_out),
        ]

        for text, command in tabs:
            if text == "View Items":
                tab_button = tk.Button(self.sidebar, text=text, background="#16a085", foreground="#ecf0f1", command=command, font=(
                    "Helvetica", 12), width=20, height=2, relief=tk.FLAT)
            else:
                tab_button = tk.Button(self.sidebar, text=text, background="#34495e", foreground="#ecf0f1", command=command, font=(
                    "Helvetica", 12), width=20, height=2, relief=tk.FLAT)
            tab_button.pack(fill=tk.X, pady=5, padx=10)

        self.content_frame = tk.Frame(self, bg="#bdc3c7")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.content_frame)

        self.x_scrollbar = ttk.Scrollbar(
            self.content_frame, orient=tk.HORIZONTAL, command=self.tree.xview)

        self.tree.configure(xscrollcommand=self.x_scrollbar.set)
        self.x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree["columns"] = (
            "Barcode",
            "FIR Number",
            "Seized Items",
            "IPC Section",
            "Crime Location",
            "Crime Date",
            "Crime Time",
            "Crime Witness",
            "Crime Inspector",
            "Item Status",
            "Where Kept",
            "Item Description"
        )

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Barcode", anchor=tk.W, width=80,
                         stretch=tk.NO, minwidth=80)
        self.tree.column("FIR Number", anchor=tk.W, stretch=tk.NO, width=100)
        self.tree.column("Seized Items", anchor=tk.W, stretch=tk.NO, width=200)
        self.tree.column("IPC Section", anchor=tk.W, stretch=tk.NO, width=150)
        self.tree.column("Crime Location", anchor=tk.W,
                         stretch=tk.NO, width=200)
        self.tree.column("Crime Date", anchor=tk.W, stretch=tk.NO, width=120)
        self.tree.column("Crime Time", anchor=tk.W, stretch=tk.NO, width=120)
        self.tree.column("Crime Witness", anchor=tk.W,
                         stretch=tk.NO, width=200)
        self.tree.column("Crime Inspector", anchor=tk.W,
                         stretch=tk.NO, width=150)
        self.tree.column("Item Status", anchor=tk.W, stretch=tk.NO, width=100)
        self.tree.column("Where Kept", anchor=tk.W, stretch=tk.NO, width=150)
        self.tree.column("Item Description", anchor=tk.W,
                         stretch=tk.NO, width=700)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Barcode", text="Barcode", anchor=tk.W)
        self.tree.heading("FIR Number", text="FIR Number", anchor=tk.W)
        self.tree.heading("Seized Items", text="Seized Items", anchor=tk.W)
        self.tree.heading("IPC Section", text="IPC Section", anchor=tk.W)
        self.tree.heading("Crime Location", text="Crime Location", anchor=tk.W)
        self.tree.heading("Crime Date", text="Crime Date", anchor=tk.W)
        self.tree.heading("Crime Time", text="Crime Time", anchor=tk.W)
        self.tree.heading("Crime Witness", text="Crime Witness", anchor=tk.W)
        self.tree.heading("Crime Inspector",
                          text="Crime Inspector", anchor=tk.W)
        self.tree.heading("Item Status", text="Item Status", anchor=tk.W)
        self.tree.heading("Where Kept", text="Where Kept", anchor=tk.W)
        self.tree.heading("Item Description",
                          text="Item Description", anchor=tk.W)

        sh = self.master.winfo_screenheight()
        self.tree.pack(fill=tk.BOTH, expand=True, side=tk.TOP,
                       pady=(0, sh//6))
        self.create_search_frame()

    def create_filter_window(self):
        def apply_filters():
            for column, var in checkbox_vars.items():
                if var.get() == 1:
                    self.tree.column(column, stretch=tk.NO, width=150)
                else:
                    self.tree.column(column, width=0, stretch=tk.NO)

        filter_window = tk.Toplevel(self.content_frame)
        filter_window.title("Select Filters")

        global checkbox_vars
        checkbox_vars = {}

        for idx, column in enumerate(self.tree["columns"]):
            var = tk.IntVar(value=1)
            checkbox_vars[column] = var
            cb = tk.Checkbutton(filter_window, text=column, variable=var)
            cb.grid(row=idx, column=0, sticky="w")

        apply_button = tk.Button(
            filter_window, text="Apply Filters", command=apply_filters)
        apply_button.grid(row=len(self.tree["columns"]), column=0, pady=5)

    def create_search_frame(self):

        search_frame = tk.Frame(self.content_frame)
        search_frame.pack(side=tk.BOTTOM, fill=tk.X)

        search_label = tk.Label(search_frame, text="Search Field:",
                                background="#FFFFFF", font=("Helvetica", 13))
        search_label.grid(row=1, column=0, padx=5, pady=5)

        search_field_var = tk.StringVar(value="Barcode")
        search_field_menu = ttk.Combobox(search_frame, textvariable=search_field_var,
                                         values=self.tree["columns"], background="#FFFFFF", state='readonly', font=("Helvetica", 13))
        search_field_menu.grid(row=1, column=1, padx=5, pady=5)

        search_entry = tk.Entry(search_frame, background="#D3D3D3",
                                textvariable=tk.StringVar(), font=("Helvetica", 13))
        search_entry.grid(row=1, column=2, padx=5, pady=5)

        search_button = tk.Button(search_frame, text="Search", background="#9a9a9a",
                                  command=lambda: self.search_items(search_field_var.get(), search_entry.get()), font=("Helvetica", 13))
        search_button.grid(row=1, column=3, padx=15, pady=5)

        select_filter_button = tk.Button(search_frame, text="Select Filter",
                                         command=self.create_filter_window, background="#9a9a9a", font=("Helvetica", 13))
        select_filter_button.grid(row=2, column=2, padx=(0, 100), pady=5)

        show_all_btn = tk.Button(search_frame, text="Show All",
                                 background="#9a9a9a", command=self.populate_tree, font=("Helvetica", 13))
        show_all_btn.grid(row=2, column=2, padx=(100, 0), pady=5)

        view_attachment_button = tk.Button(search_frame, background="#9a9a9a",
                                           text="View Attachment", command=self.view_attachment, font=("Helvetica", 13))
        view_attachment_button.grid(row=1, column=6, padx=15, pady=5)

        print_details_button = tk.Button(search_frame, background="#9a9a9a",
                                         text="Print Item Details",  font=("Helvetica", 13))
        print_details_button.grid(row=1, column=7, padx=15, pady=5)

        previous_button = tk.Button(search_frame, text="Previous",
                                    background="#9a9a9a", font=("Helvetica", 13), width=12)
        previous_button.grid(row=1, column=8, padx=(180, 0), pady=5)

        next_button = tk.Button(search_frame, text="Next",
                                background="#9a9a9a", font=("Helvetica", 13), width=12)
        next_button.grid(row=1, column=9, padx=10, pady=5)

        go_back_button = tk.Button(search_frame, background="#9a9a9a",
                                   text="Go Back", font=("Helvetica", 13), width=12)
        go_back_button.grid(row=1, column=10, pady=5)

    def add_item(self):
        self.controller.show_frame("AddItemsFrame")

    def checkout_item(self):
        self.controller.show_frame("CheckoutItemFrame")

    def checkin_item(self):
        MiscFuncs.entry_clearer(self)

    def search_items(self, search_field, search_entry):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in self.item.search_items(search_field, search_entry):
            self.tree.insert('', 'end', values=row)

    def view_attachment(self):
        pass

    def go_back(self):
        self.controller.show_frame("MalkhanaFrame")

    def log_out(self):
        self.controller.frames["LoginFrame"].username_entry.delete(0, tk.END)
        self.controller.frames["LoginFrame"].password_entry.delete(0, tk.END)
        self.controller.show_frame("LoginFrame")

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def populate_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in self.item.view_filler():
            self.tree.insert('', 'end', values=row)
