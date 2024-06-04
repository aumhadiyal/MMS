import sqlite3
import os
import sys


class Item:
    def __init__(self):
        self.db_path = self.get_db_path()
        self.initialize_db()

    def get_db_path(self):
        return "E:\malkhana_management\MMS\malkhana\databases\database.db"

    def initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                barcode INTEGER PRIMARY KEY,
                fir_no TEXT,
                seized_items TEXT,
                ipc_section TEXT,
                crime_location TEXT,
                crime_date TEXT,
                crime_time TEXT,
                crime_witness TEXT,
                crime_inspector TEXT,
                item_status TEXT,
                where_kept TEXT,
                description_of_items TEXT,
                entry_time TEXT,
                attachments BLOB
            )
        """)
        conn.commit()
        conn.close()

    def insert_item(self, barcode, fir_no, seized_items, ipc_section, crime_location, crime_date, crime_time, crime_witness,
                    crime_inspector, item_status, where_kept, description_of_items, entry_time, attachments):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO items (barcode, fir_no, seized_items, ipc_section, crime_location, 
                          crime_date, crime_time, crime_witness, crime_inspector, item_status, where_kept, 
                          description_of_items, entry_time, attachments) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (barcode, fir_no, seized_items, ipc_section, crime_location, crime_date, crime_time, crime_witness,
                                                                                 crime_inspector, item_status, where_kept, description_of_items, entry_time, attachments))

            conn.commit()
            conn.close()
        except Exception as e:
            raise e

    def save_attachment(self, barcode, file_path):
        with open(file_path, 'rb') as file:
            attachment_data = file.read()

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM attachments WHERE barcode = ?", (barcode,))
        cursor.execute(
            "INSERT INTO attachments (barcode, attachment_data) VALUES (?, ?)", (barcode, attachment_data))
        conn.commit()
        conn.close()

    def convert_to_column(self, field_name):
        columnname = {
            "Barcode": "barcode",
            "FIR Number": "fir_no",
            "Seized Items": "seized_items",
            "IPC Section": "ipc_section",
            "Crime Location": "crime_location",
            "Crime Date": "crime_date",
            "Crime Time": "crime_time",
            "Crime Witness": "crime_witness",
            "Crime Inspector": "crime_inspector",
            "Item Status": "item_status",
            "Where Kept": "where_kept",
            "Item Description": "description_of_items"

        }
        print(columnname.get(field_name, field_name))
        return columnname.get(field_name, field_name)

    def search_items(self, search_field, search_text):
        search_field = self.convert_to_column(search_field)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'''
                SELECT * FROM items
                WHERE {search_field} LIKE ?
            ''', ('%' + search_text + '%',))
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return rows

    def view_filler(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''SELECT barcode, fir_no, seized_items, ipc_section, crime_location, crime_date, crime_time, crime_witness, crime_inspector, item_status, where_kept, description_of_items
                          FROM items ORDER BY entry_time DESC''')
        rows = cursor.fetchall()
        conn.close()
        return rows
