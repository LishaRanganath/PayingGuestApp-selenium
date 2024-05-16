from .my_sql_connector import MySqlConnector


class Booking(MySqlConnector):
    def get_booking_status(self, user_id):
        db = self.db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT booking_status FROM bookings WHERE user_id={user_id} ORDER BY id DESC LIMIT 1;")
        result = cursor.fetchone()[0]
        return result

    def get_booking_id(self,user_id):
        db = self.db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM bookings WHERE user_id={user_id} ORDER BY id DESC LIMIT 1;")
        result = cursor.fetchone()[0]
        return result