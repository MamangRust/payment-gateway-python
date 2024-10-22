import logging
from typing import List
from models.topup import Topup
from .abstract_class.topup import TopupAbstractRepository


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TopupRepository(TopupAbstractRepository):
    def __init__(self, connection):
        self.connection = connection

    
    def get_all_topups(self) -> List[Topup]:
        query = "SELECT * FROM topups"

        try:
            topups_data = self.connection.fetch_all(query)
        
            if topups_data:
                logging.info(f"Retrieved {len(topups_data)} topups.")
                return [Topup(*topup_data) for topup_data in topups_data]
            else:
                logging.info("No topups found.")
                return []
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving all topups: {e}")
            return []


    def create_topup(self, user_id, topup_no, topup_amount, topup_method, topup_time) -> Topup:
        query = """
            INSERT INTO topups (user_id, topup_no, topup_amount, topup_method, topup_time)
            VALUES (?, ?, ?, ?, ?)
        """
        parameters = (user_id, topup_no, topup_amount, topup_method, topup_time)

        try:
            cursor = self.connection.execute_query(query, parameters)
            topup_id = cursor.lastrowid
            self.connection.commit()

            logging.info(f"Created topup: ID {topup_id}, User ID {user_id}, Topup No {topup_no}, Topup Amount {topup_amount}, Topup Method {topup_method}, Topup Time {topup_time}.")
            return Topup(topup_id, user_id, topup_no, topup_amount, topup_method, topup_time)
        
        except Exception as e:
            logging.error(f"An error occurred while creating topup: {e}")
            return None


        return Topup(topup_id, user_id, topup_no, topup_amount, topup_method, topup_time)

    def get_topup_by_user_id(self, user_id) -> List[Topup]:
        query = "SELECT * FROM topups WHERE user_id=?"
        parameters = (user_id,)

        try:
            topups_data = self.connection.fetch_all(query, parameters)
        
            if topups_data:
                logging.info(f"Retrieved {len(topups_data)} topups for user ID {user_id}.")
                return [Topup(*topup_data) for topup_data in topups_data]
            else:
                logging.info(f"No topups found for user ID {user_id}.")
                return []
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving topups for user ID {user_id}: {e}")
            return []


    def get_topup_id(self, topup_id):
        query = "SELECT * FROM topups WHERE topup_id=?"
        parameters = (topup_id,)

        try:
            topup_data = self.connection.fetch_one(query, parameters)
        
            if topup_data:
                logging.info(f"Retrieved topup by ID: {topup_id}.")
                return Topup(*topup_data)
            else:
                logging.info(f"No topup found with ID: {topup_id}.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving topup by ID {topup_id}: {e}")
            return None

    def update_topup(self, topup_id, new_topup_amount, new_topup_method, new_topup_time) -> Topup:
        query = """
            UPDATE topups
            SET topup_amount=?, topup_method=?, topup_time=?
            WHERE topup_id=?
        """
        parameters = (new_topup_amount, new_topup_method, new_topup_time, topup_id)

        try:
            cursor = self.connection.execute_query(query, parameters)
            self.connection.commit()

            updated_topup_data = self.connection.fetch_one("SELECT * FROM topups WHERE topup_id=?", (topup_id,))

            if updated_topup_data:
                logging.info(f"Updated topup ID {topup_id} to topup_amount {new_topup_amount}, topup_method {new_topup_method}, topup_time {new_topup_time}.")
                return Topup(*updated_topup_data)
            else:
                logging.warning(f"No topup found with ID: {topup_id} for update.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while updating topup ID {topup_id}: {e}")
            return None

    def delete_topup(self, topup_id) -> Topup:
        query = "DELETE FROM topups WHERE topup_id=?"
        parameters = (topup_id,)


        try:
            cursor = self.connection.execute_query(query, parameters)
            self.connection.commit()

            deleted_topup_data = self.connection.fetch_one("SELECT * FROM topups WHERE topup_id=?", (topup_id,))

            if deleted_topup_data:
                logging.info(f"Deleted topup ID {topup_id}.")
                return Topup(*deleted_topup_data)
            else:
                logging.warning(f"No topup found with ID: {topup_id} for deletion.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while deleting topup ID {topup_id}: {e}")
            return None


