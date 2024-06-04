import sqlite3
import os
import sys


class Logs:
    def __init__(self):
        self.db_path = self.get_db_path()
        self.initialize_db()

    def get_db_path(self):
        return "E:\malkhana_management\MMS\malkhana\databases\database.db"

    def initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                barcode INTEGER ,
                activity TEXT NOT NULL,
                entry_time TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def log_item(self, barcode, activity, time):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO logs(barcode,activity,entry_time)VALUES(?,?,?)""",
                       (barcode, activity, time))
        conn.commit()
        conn.close()
