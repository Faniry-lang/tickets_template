import mysql.connector
from mysql.connector import Error

class DbConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_conn(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def fetch(self, query, params=None):
        conn = None
        cursor = None
        try:
            conn = self.get_conn()
            cursor = conn.cursor(dictionary=True)

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
                            
            rows = cursor.fetchall()
            return rows
                
        except Error as e:
            raise Exception(f"Error while fetching data: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def execute(self, query, params=None):
        conn = None
        cursor = None
        try:
            conn = self.get_conn()
            cursor = conn.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            conn.commit()
            return cursor.rowcount
                
        except Error as e:
            if conn:
                conn.rollback()
            raise Exception(f"Error while executing query: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()