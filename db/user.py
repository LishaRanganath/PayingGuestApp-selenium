from .my_sql_connector import MySqlConnector


class User(MySqlConnector):

    def get_user_id(self, email):
        db = self.db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM users WHERE email = '{email}'")
        result = cursor.fetchone()[0]
        return result

    def check_complaints(self, user_id):
        db = self.db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT complaints FROM bookings WHERE user_id = {user_id}")
        result = cursor.fetchone()[0]
        return result

    def check_role(self, user_id):
        db = self.db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT role FROM users WHERE id = {user_id}")
        result = cursor.fetchone()[0]
        return result
