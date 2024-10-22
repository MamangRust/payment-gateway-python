import logging
from models.user import User
from typing import List
from .abstract_class.user import UserAbstractRepository

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserRepository(UserAbstractRepository):
    def __init__(self, connection):
        self.connection = connection

    def get_all_users(self) -> List[User]:
        query = "SELECT * FROM users"
        try:
            user_data = self.connection.fetch_all(query)

            if user_data:
                logging.info(f"Retrieved {len(user_data)} users.")
                return [User(*user) for user in user_data]
            else:
                logging.info("No users found.")
                return []

        
        except Exception as e:
            logging.error(f"An error occurred while retrieving all users: {e}")
            return []

    def create_user(self, email, password, noc_transfer=0) -> User:
        query = "INSERT INTO users (email, password, noc_transfer) VALUES (?, ?, ?)"
        parameters = (email, password, noc_transfer)
        try:
            cursor = self.connection.execute_query(query, parameters)
            user_id = cursor.lastrowid  

            self.connection.commit()

            logging.info(f"Created user: ID {user_id}, Email {email}, Password {password}, Noc Transfer {noc_transfer}.")

            return User(user_id, email, password, noc_transfer)
        
        except Exception as e:
            logging.error(f"An error occurred while creating user: {e}")
            return None

    def get_user_by_email(self, email) -> User:
        query = "SELECT * FROM users WHERE email=?"
        parameters = (email,)
        try:
            user_data = self.connection.fetch_one(query, parameters)
    
            logging.info(f"Retrieved user by email: {email}.")

            return User(*user_data) if user_data else None
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving user by email: {e}")
            return None

    def get_user_by_id(self, user_id) -> User:
        query = "SELECT * FROM users WHERE user_id=?"
        parameters = (user_id,)
        try:
            user_data = self.connection.fetch_one(query, parameters)

            if user_data:
                logging.info(f"Retrieved user by ID: {user_id}.")

                return User(*user_data)
            else:
                logging.info(f"No user found with ID: {user_id}.")
                return None
        
        except Exception as e:
            logging.error(f"An error occurred while retrieving user by ID: {e}")
            return None

    def update_user(self, user_id, new_noc_transfer):
        query = "UPDATE users SET noc_transfer=? WHERE user_id=?"
        parameters = (user_id, new_noc_transfer)
        try:
            self.connection.execute_query(query, parameters)
            self.connection.commit()

            updated_user_data = self.connection.fetch_one("SELECT * FROM users WHERE user_id=?", (user_id,))
            if updated_user_data:
                logging.info(f"Updated user ID {user_id} to noc_transfer {new_noc_transfer}.")
                return User(*updated_user_data)
            else:
                logging.warning(f"No user found with ID: {user_id} for update.")

                return None
        
        except Exception as e:
            logging.error(f"An error occurred while updating user ID {user_id}: {e}")
            return None



    def delete_user(self, user_id) -> User:
        query_select = "SELECT * FROM users WHERE user_id=?"
        parameters_select = (user_id,)
        try:
            user_data = self.connection.fetch_one(query_select, parameters_select)

            if user_data:
                query_delete = "DELETE FROM users WHERE user_id=?"
                parameters_delete = (user_id,)
                self.connection.execute_query(query_delete, parameters_delete)
                self.connection.commit()
                
                logging.info(f"Deleted user: ID {user_id}, Email {user_data[1]}, Password {user_data[2]}, Noc Transfer {user_data[3]}.")

                return User(*user_data)
            else:
                logging.warning(f"No user found with ID: {user_id} for deletion.")
                return None


        except Exception as e:
            logging.error(f"An error occurred while deleting user ID {user_id}: {e}")
            return None

    def __str__(self):
        try:
            return f"All Users: {', '.join(str(user) for user in self.get_all_users())}"
        except Exception as e:
            return f"An error occurred while getting all users: {e}"
