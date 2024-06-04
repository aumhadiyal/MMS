import tkinter as tk


class MiscFuncs(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller

    @staticmethod
    def entry_clearer(self):
        self.controller.frames["LoginFrame"].username_entry.delete(0, tk.END)
        self.controller.frames["LoginFrame"].password_entry.delete(0, tk.END)
        self.controller.frames["AddItemsFrame"].barcode_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].fir_no_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].seized_items_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].ipc_section_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].crime_location_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].crime_witness_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].crime_inspector_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].where_kept_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].description_of_items_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].crime_date_entry.delete(
            0, tk.END)
        self.controller.frames["AddItemsFrame"].hour_var.set('00')
        self.controller.frames["AddItemsFrame"].minute_var.set('00')
        self.controller.frames["ViewItemsFrame"].checkbox_vars.set({})
        self.controller.frames["ViewItemsFrame"].search_entry.delete(0, tk.END)
        self.controller.frames["ViewItemsFrame"].search_field_var.set(
            'Barcode')
        self.controller.frames["ViewItemsFrame"].populate_tree(self)
