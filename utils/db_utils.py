import sqlite3

class DbUtils:

    def connect_db(self):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        return conn
