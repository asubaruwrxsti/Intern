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
            print(f"Error {e} occurred while trying to connect to the database.")
            return False
        return True

    def close_connection(self):
        """ Close the database connection """
        if self.conn:
            try:
                self.conn.close()
            except Error as e:
                print(f"Error {e} occurred while trying to close the database.")
                return False
        return True

    def execute_query(self, query):
        """ Execute a query """
        if self.conn is None:
            if not self.open_connection():
                return None

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return cursor.fetchall()
        except Error as e:
            print(f"Error {e} occurred while trying to execute the query.")
            return None