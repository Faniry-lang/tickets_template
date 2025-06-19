import mysql.connector

class DbConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def fetch(self, query):
        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    def execute(self, query):
        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()  

        cursor.close()
        conn.close()
