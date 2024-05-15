import mysql.connector

class MySqlConnector():
    def __init__(self):
        pass
    def db_connect(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='lisha123',
            port='3306',
            database='paying_guest_app_new_development'
        )
        return mydb
