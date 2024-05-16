from .my_sql_connector import MySqlConnector


class Building(MySqlConnector):

    def get_building_id(self,name):
        db = self.db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM pg_buildings WHERE name='{name}'")
        result = cursor.fetchone()[0]
        return result