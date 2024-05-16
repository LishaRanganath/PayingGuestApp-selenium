from .my_sql_connector import MySqlConnector


class Room(MySqlConnector):

    def check_room_count(self, building_id, booking_id):
        db = self.db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT availability FROM available_rooms WHERE pg_building_id={building_id} AND (SELECT "
                       f"available_room_id FROM bookings WHERE id={booking_id})")
        result = cursor.fetchone()[0]
        return result
    def check_current_room_count(self, room_id):
        db = self.db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT availability FROM available_rooms WHERE id={room_id}")
        result = cursor.fetchone()[0]
        return result
