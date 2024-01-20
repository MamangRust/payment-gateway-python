from models.transfer import Transfer

class TransferRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_transfer(self, transfer_from, transfer_to, transfer_amount, transfer_time):
        query = """
            INSERT INTO transfers (transfer_from, transfer_to, transfer_amount, transfer_time)
            VALUES (?, ?, ?, ?)
        """
        parameters = (transfer_from, transfer_to, transfer_amount, transfer_time)
        cursor = self.connection.execute_query(query, parameters)
        transfer_id = cursor.lastrowid
        self.connection.commit()

        return Transfer(transfer_id, transfer_from, transfer_to, transfer_amount, transfer_time)

    def get_transfer_by_id(self, transfer_id):
        query = "SELECT * FROM transfers WHERE transfer_id=?"
        parameters = (transfer_id,)
        transfer_data = self.connection.fetch_one(query, parameters)
        return Transfer(*transfer_data) if transfer_data else None

    def get_transfer_by_user_id(self, user_id):
        query = "SELECT * FROM transfers WHERE transfer_from=? OR transfer_to=?"
        parameters = (user_id, user_id)
        transfers_data = self.connection.fetch_all(query, parameters)
        return [Transfer(*transfer_data) for transfer_data in transfers_data]

    def get_all_transfers(self):
        query = "SELECT * FROM transfers"
        transfers_data = self.connection.fetch_all(query)
        return [Transfer(*transfer_data) for transfer_data in transfers_data]

    def update_transfer(self, transfer_id, new_transfer_amount, new_transfer_time):
        query = """
            UPDATE transfers
            SET transfer_amount=?, transfer_time=?
            WHERE transfer_id=?
        """
        parameters = (new_transfer_amount, new_transfer_time, transfer_id)
        self.connection.execute_query(query, parameters)
        self.connection.commit()

        # Assuming you want to return the updated transfer
        updated_transfer_data = self.connection.fetch_one("SELECT * FROM transfers WHERE transfer_id=?", (transfer_id,))
        return Transfer(*updated_transfer_data) if updated_transfer_data else None

    def delete_transfer(self, transfer_id):
        query = "DELETE FROM transfers WHERE transfer_id=?"
        parameters = (transfer_id,)
        transfer_data = self.connection.fetch_one("SELECT * FROM transfers WHERE transfer_id=?", parameters)
        
        if transfer_data:
            self.connection.execute_query(query, parameters)
            self.connection.commit()

        return Transfer(*transfer_data) if transfer_data else None
