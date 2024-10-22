import logging
from models.transfer import Transfer
from .abstract_class.transfer import TransferAbstractRepository

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TransferRepository(TransferAbstractRepository):
    def __init__(self, connection):
        self.connection = connection

    def create_transfer(self, transfer_from, transfer_to, transfer_amount, transfer_time):
        query = """
            INSERT INTO transfers (transfer_from, transfer_to, transfer_amount, transfer_time)
            VALUES (?, ?, ?, ?)
        """
        parameters = (transfer_from, transfer_to, transfer_amount, transfer_time)
        try:

            cursor = self.connection.execute_query(query, parameters)
            transfer_id = cursor.lastrowid
            self.connection.commit()

            logging.info(f"Created transfer: ID {transfer_id}, From {transfer_from}, To {transfer_to}, Amount {transfer_amount}, Time {transfer_time}.")

            return Transfer(transfer_id, transfer_from, transfer_to, transfer_amount, transfer_time)

        except Exception as e:
            logging.error(f"Failed to create transfer: {e}")
            return None

    def get_transfer_by_id(self, transfer_id):
        query = "SELECT * FROM transfers WHERE transfer_id=?"
        parameters = (transfer_id,)

        try:
            transfer_data = self.connection.fetch_one(query, parameters)
            if transfer_data:
                logging.info(f"Retrieved transfer by ID: {transfer_id}.")
                return Transfer(*transfer_data)
            else:
                logging.info(f"No transfer found with ID: {transfer_id}.")
                return None
        
        except Exception as e:
            logging.error(f"Failed to retrieve transfer by ID: {e}")
            return None

    def get_transfer_by_user_id(self, user_id):
        query = "SELECT * FROM transfers WHERE transfer_from=? OR transfer_to=?"
        parameters = (user_id, user_id)


        try:
            transfers_data = self.connection.fetch_all(query, parameters)

            logging.info(f"Retrieved {len(transfers_data)} transfers for user ID {user_id}.")
            return [Transfer(*transfer_data) for transfer_data in transfers_data]
        
        except Exception as e:
            logging.error(f"Failed to retrieve transfer by user ID: {e}")
            return None



    def get_all_transfers(self):
        query = "SELECT * FROM transfers"

        try:
            transfers_data = self.connection.fetch_all(query)

            if transfers_data:
                logging.info(f"Retrieved {len(transfers_data)} transfers.")
                return [Transfer(*transfer_data) for transfer_data in transfers_data]
            else:
                logging.info("No transfers found.")
                return []
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving all transfers: {e}")
            return []


    def update_transfer(self, transfer_id, new_transfer_amount, new_transfer_time):
        query = """
            UPDATE transfers
            SET transfer_amount=?, transfer_time=?
            WHERE transfer_id=?
        """
        parameters = (new_transfer_amount, new_transfer_time, transfer_id)

        try:

            self.connection.execute_query(query, parameters)
            self.connection.commit()

            updated_transfer_data = self.connection.fetch_one("SELECT * FROM transfers WHERE transfer_id=?", (transfer_id,))

            if updated_transfer_data:
                logging.info(f"Updated transfer ID {transfer_id} to transfer_amount {new_transfer_amount}, transfer_time {new_transfer_time}.")
                return Transfer(*updated_transfer_data)
            else:
                logging.warning(f"No transfer found with ID: {transfer_id} for update.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while updating transfer ID {transfer_id}: {e}")
            return None
        

    def delete_transfer(self, transfer_id):
        query = "DELETE FROM transfers WHERE transfer_id=?"
        parameters = (transfer_id,)

        try:
            transfer_data = self.connection.fetch_one("SELECT * FROM transfers WHERE transfer_id=?", parameters)

            if transfer_data:
                self.connection.execute_query(query, parameters)
                self.connection.commit()
                logging.info(f"Deleted transfer ID {transfer_id}.")
                return Transfer(*transfer_data)
            else:
                logging.warning(f"No transfer found with ID: {transfer_id} for deletion.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while deleting transfer ID {transfer_id}: {e}")
            return None
