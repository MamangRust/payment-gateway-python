from typing import List
from models.topup import Topup


class TopupRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_topup(self, user_id, topup_no, topup_amount, topup_method, topup_time) -> Topup:
        query = """
            INSERT INTO topups (user_id, topup_no, topup_amount, topup_method, topup_time)
            VALUES (?, ?, ?, ?, ?)
        """
        parameters = (user_id, topup_no, topup_amount, topup_method, topup_time)
        cursor = self.connection.execute_query(query, parameters)
        topup_id = cursor.lastrowid
        self.connection.commit()

        return Topup(topup_id, user_id, topup_no, topup_amount, topup_method, topup_time)

    def get_topup_by_user_id(self, user_id) -> List[Topup]:
        query = "SELECT * FROM topups WHERE user_id=?"
        parameters = (user_id,)
        topups_data = self.connection.fetch_all(query, parameters)
        return [Topup(*topup_data) for topup_data in topups_data]

    def get_all_topups(self) -> List[Topup]:
        query = "SELECT * FROM topups"
        topups_data = self.connection.fetch_all(query)
        return [Topup(*topup_data) for topup_data in topups_data]


    def get_topup_id(self, topup_id):
        query = "SELECT * FROM topups WHERE topup_id=?"
        parameters = (topup_id,)
        topup_data = self.connection.fetch_one(query, parameters)
        return Topup(*topup_data) if topup_data else None

    def update_topup(self, topup_id, new_topup_amount, new_topup_method, new_topup_time) -> Topup:
        query = """
            UPDATE topups
            SET topup_amount=?, topup_method=?, topup_time=?
            WHERE topup_id=?
        """
        parameters = (new_topup_amount, new_topup_method, new_topup_time, topup_id)
        self.connection.execute_query(query, parameters)
        self.connection.commit()

        
        updated_topup_data = self.connection.fetch_one("SELECT * FROM topups WHERE topup_id=?", (topup_id,))
        return Topup(*updated_topup_data) if updated_topup_data else None

    def delete_topup(self, topup_id) -> Topup:
        query = "DELETE FROM topups WHERE topup_id=?"
        parameters = (topup_id,)
        topup_data = self.connection.fetch_one("SELECT * FROM topups WHERE topup_id=?", parameters)
        
        if topup_data:
            self.connection.execute_query(query, parameters)
            self.connection.commit()

        return Topup(*topup_data) if topup_data else None
