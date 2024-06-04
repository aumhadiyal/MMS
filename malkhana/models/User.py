import sqlite3
import os
import sys


class User:
    def __init__(self):
        self.db_path = self.get_db_path()
        self.initialize_db()

    def get_db_path(self):
        return "E:\malkhana_management\malkhana\databases\database.db"

    def initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                level TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def add_user(self, username, password, level):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, level) VALUES (?, ?, ?)",
                       (username, password, level))
        conn.commit()
        conn.close()

    def check_credentials(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT password FROM users WHERE username=?", (username,))
        stored_password = cursor.fetchone()
        conn.close()

        if stored_password and stored_password[0] == password:
            return True
        else:
            return False
