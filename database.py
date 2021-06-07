import sqlite3
from sqlite3.dbapi2 import Error

class Database:
    def __init__(self,data):
        self.data = data

    def createDB(self):
        try:
            conn = sqlite3.connect("test.db")
            print("opened db")

        except Error as e:
            print(e)
        finally:
            cursor = conn.cursor()
            conn.execute(" DROP TABLE IF EXISTS data")  # drop the table if it exists
            conn.execute("CREATE TABLE data (symbol TEXT, date TEXT, close TEXT)")
            print("table created")
            for name, values in self.data.items():
                for value in values:
                    cursor.execute(
                        "INSERT INTO data values ('%s', '%s', '%s')"
                        %(name, value[0], value[1])
                    )
            print("data added")
            conn.commit()
            conn.close()
