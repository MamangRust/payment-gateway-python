import logging
from models.withdraw import Withdraw
from .abstract_class.withdraw import WithdrawAbstractRepository


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WithdrawRepository(WithdrawAbstractRepository):
    def __init__(self, connection):
        self.connection = connection

    def get_all_withdraws(self):
        query = "SELECT * FROM withdraws"

        try:
            withdraw_data = self.connection.fetch_all(query)
            if withdraw_data:
                logging.info(f"Retrieved {len(withdraw_data)} withdraws.")
                return [Withdraw(*withdraw) for withdraw in withdraw_data]
            else:
                logging.info("No withdraws found.")
                return []
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving all withdraws: {e}")
            return []

    def create_withdraw(self, user_id, withdraw_amount, withdraw_time) -> Withdraw:
        query = """
            INSERT INTO withdraws (user_id, withdraw_amount, withdraw_time)
            VALUES (?, ?, ?)
        """
        parameters = (user_id, withdraw_amount, withdraw_time)
        try:
            cursor = self.connection.execute_query(query, parameters)
            withdraw_id = cursor.lastrowid
            self.connection.commit()

            logging.info(f"Created withdraw: ID {withdraw_id}, User ID {user_id}, Amount {withdraw_amount}.")
            return Withdraw(withdraw_id, user_id, withdraw_amount, withdraw_time)
        
        except Exception as e:
            logging.error(f"An error occurred while creating withdraw: {e}")
            return None

    def get_withdraw_by_id(self, withdraw_id):
        query = "SELECT * FROM withdraws WHERE withdraw_id=?"
        parameters = (withdraw_id,)

        try:
            withdraw_data = self.connection.fetch_one(query, parameters)
            if withdraw_data:
                logging.info(f"Retrieved withdraw by ID: {withdraw_id}.")
                return Withdraw(*withdraw_data)
            else:
                logging.info(f"No withdraw found with ID: {withdraw_id}.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving withdraw by ID {withdraw_id}: {e}")
            return None

    def get_withdraw_by_user_id(self, user_id):
        query = "SELECT * FROM withdraws WHERE user_id=?"
        parameters = (user_id,)

        try:
            withdraw_data = self.connection.fetch_all(query, parameters)
            if withdraw_data:
                logging.info(f"Retrieved {len(withdraw_data)} withdraws for user ID: {user_id}.")
                return [Withdraw(*withdraw) for withdraw in withdraw_data]
            else:
                logging.info(f"No withdraws found for user ID: {user_id}.")
                return []
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving withdraws for user ID {user_id}: {e}")
            return []

    def update_withdraw(self, withdraw_id, new_withdraw_amount, new_withdraw_time):
        query = """
            UPDATE withdraws
            SET withdraw_amount=?, withdraw_time=?
            WHERE withdraw_id=?
        """
        parameters = (new_withdraw_amount, new_withdraw_time, withdraw_id)
        try:
            self.connection.execute_query(query, parameters)
            self.connection.commit()

            updated_withdraw_data = self.connection.fetch_one("SELECT * FROM withdraws WHERE withdraw_id=?", (withdraw_id,))
            if updated_withdraw_data:
                logging.info(f"Updated withdraw ID {withdraw_id} to amount {new_withdraw_amount}.")
                return Withdraw(*updated_withdraw_data)
            else:
                logging.warning(f"No withdraw found with ID: {withdraw_id} for update.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while updating withdraw ID {withdraw_id}: {e}")
            return None

    def delete_withdraw(self, withdraw_id):
        query = "DELETE FROM withdraws WHERE withdraw_id=?"
        parameters = (withdraw_id,)

        try:
            withdraw_data = self.connection.fetch_one("SELECT * FROM withdraws WHERE withdraw_id=?", parameters)

            if withdraw_data:
                self.connection.execute_query(query, parameters)
                self.connection.commit()
                logging.info(f"Deleted withdraw ID: {withdraw_id}.")
                return Withdraw(*withdraw_data)
            else:
                logging.warning(f"No withdraw found with ID: {withdraw_id} for deletion.")
                return None

        except Exception as e:
            logging.error(f"An error occurred while deleting withdraw ID {withdraw_id}: {e}")
            return None
