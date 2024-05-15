from .my_sql_connector import MySqlConnector
class Owner(MySqlConnector):
    def get_total_number_of_owners(self):
        db=self.db_connect()
        cursor=db.cursor()
        cursor.execute("SELECT COUNT(*) FROM owners")
        result = cursor.fetchone()[0]
        return result

    def check_status_of_owner(self,name):
        db=self.db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT status FROM owners WHERE name='{name}';")
        result = cursor.fetchone()[0]
        return result