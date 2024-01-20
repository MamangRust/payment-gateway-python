from models.withdraw import Withdraw

class WithdrawRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_withdraw(self, user_id, withdraw_amount, withdraw_time):
        query = """
            INSERT INTO withdraws (user_id, withdraw_amount, withdraw_time)
            VALUES (?, ?, ?)
        """
        parameters = (user_id, withdraw_amount, withdraw_time)
        cursor =  self.connection.execute_query(query, parameters)
        withdraw_id = cursor.lastrowid
        self.connection.commit()

        return Withdraw(withdraw_id, user_id, withdraw_amount, withdraw_time)

    def get_withdraw_by_id(self, withdraw_id):
        query = "SELECT * FROM withdraws WHERE withdraw_id=?"
        parameters = (withdraw_id, )

        withdraw_data = self.connection.fetch_one(query, parameters)

        return Withdraw(*withdraw_data) if withdraw_data is not None else None


    def get_withdraw_by_user_id(self, user_id):
        query = "SELECT * FROM withdraws WHERE user_id=?"
        parameters = (user_id,)
        withdraw_data = self.connection.fetch_all(query, parameters)

        return [Withdraw(*withdraw) for withdraw in withdraw_data]
    def get_all_withdraws(self):
        query = "SELECT * FROM withdraws"

        withdraw_data = self.connection.fetch_all(query)

        return [Withdraw(*withdraw) for withdraw in withdraw_data]

    def update_withdraw(self, withdraw_id, new_withdraw_amount, new_withdraw_time):
        query = """
            UPDATE withdraws
            SET withdraw_amount=?, withdraw_time=?
            WHERE withdraw_id=?
        """
        parameters = (new_withdraw_amount, new_withdraw_time, withdraw_id)
        self.connection.execute_query(query, parameters)
        self.connection.commit()

        updated_withdraw_data = self.connection.fetch_one("SELECT * FROM withdraws WHERE withdraw_id=?", (withdraw_id,))
        return Withdraw(*updated_withdraw_data) if updated_withdraw_data else None

    def delete_withdraw(self, withdraw_id):
        query = "DELETE FROM withdraws WHERE withdraw_id=?"
        parameters = (withdraw_id,)

        withdraw_data = self.connection.fetch_one("SELECT * FROM withdraws WHERE withdraw_id=?", parameters)

        if withdraw_data:
            self.connection.execute_query(query, parameters)
            self.connection.commit()

        
        return Withdraw(*withdraw_data) if withdraw_data else None