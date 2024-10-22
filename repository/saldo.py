import logging
from typing import Optional, List
from models.saldo import Saldo
from .abstract_class.saldo import SaldoAbstractRepository

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SaldoRepository:
    def __init__(self, connection):
        self.connection = connection


    def get_all_saldo(self) -> List[Saldo]:
        query = "SELECT * FROM saldo"

        try:
            saldo_data = self.connection.fetch_all(query)

            if saldo_data:
                logging.info(f"Retrieved {len(saldo_data)} saldo.")
                return [Saldo(*data) for data in saldo_data]
            else:
                logging.info("No saldo found.")
                return []
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving all saldo: {e}")
            return []
        

    def create_saldo(self, user_id, total_balance, withdraw_amount=0, withdraw_time=None) -> Saldo:
        query = """
            INSERT INTO saldo (user_id, total_balance, withdraw_amount, withdraw_time)
            VALUES (?, ?, ?, ?)
        """
        parameters = (user_id, total_balance, withdraw_amount, withdraw_time)
        try:
            cursor = self.connection.execute_query(query, parameters)
            saldo_id = cursor.lastrowid
            self.connection.commit()

            logging.info(f"Created saldo: ID {saldo_id}, User ID {user_id}, Total Balance {total_balance}.")
            return Saldo(saldo_id, user_id, total_balance, withdraw_amount, withdraw_time)
        
        except Exception as e:
            logging.error(f"An error occurred while creating saldo: {e}")
            return None

    def get_saldo_by_user_id(self, user_id) -> Optional[Saldo]:
        query = "SELECT * FROM saldo WHERE user_id=?"
        parameters = (user_id,)

        try:

            saldo_data = self.connection.fetch_one(query, parameters)
            if saldo_data:
                logging.info(f"Retrieved saldo by user ID: {user_id}.")
                return Saldo(*saldo_data)
            
            else:
                logging.info(f"No saldo found for user ID {user_id}.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving saldo by user ID: {e}")
            return None


    def update_saldo(self, user_id, total_balance, withdraw_amount=0, withdraw_time=None) -> Optional[Saldo]:
        query = """
            UPDATE saldo
            SET total_balance=?, withdraw_amount=?, withdraw_time=?
            WHERE user_id=?
        """
        parameters = (total_balance, withdraw_amount, withdraw_time, user_id)

        try:
            self.connection.execute_query(query, parameters)
            self.connection.commit()

            updated_saldo_data = self.connection.fetch_one("SELECT * FROM saldo WHERE user_id=?", (user_id,))
            if updated_saldo_data:
                logging.info(f"Updated saldo ID {user_id} to total_balance {total_balance}.")
                return Saldo(*updated_saldo_data)
            else:
                logging.warning(f"No saldo found with ID: {user_id} for update.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while updating saldo ID {user_id}: {e}")
            return None


    def delete_saldo(self, user_id) -> Optional[Saldo]:
        query_select = "SELECT * FROM saldo WHERE user_id=?"
        parameters_select = (user_id,)
        
        try:
            saldo_data = self.connection.fetch_one(query_select, parameters_select)

            if saldo_data:
                query_delete = "DELETE FROM saldo WHERE user_id=?"
                parameters_delete = (user_id,)
                self.connection.execute_query(query_delete, parameters_delete)
                self.connection.commit()
                
                logging.info(f"Deleted saldo: ID {user_id}, User ID {user_data[1]}, Total Balance {user_data[2]}, Withdraw Amount {user_data[3]}, Withdraw Time {user_data[4]}.")

                return Saldo(*user_data)
            else:
                logging.warning(f"No saldo found with ID: {user_id} for deletion.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while deleting saldo ID {user_id}: {e}")
            return None
