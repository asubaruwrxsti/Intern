import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        """ Initialize database class with db file """
        self.db_file = db_file
        self.conn = None

    def open_connection(self):
        """ Open a database connection to a SQLite database """
        try:
            self.conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

    def close_connection(self):
        """ Close the database connection """
        if self.conn:
            self.conn.close()

    def execute_query(self, query):
        """ Execute a query """
        if self.conn is None:
            self.open_connection()

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
        except Error as e:
            print(e)