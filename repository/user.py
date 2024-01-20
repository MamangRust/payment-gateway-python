from models.user import User
from typing import List

class UserRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all_users(self) -> List[User]:
        query = "SELECT * FROM users"
        cursor = self.connection.execute_query(query)
        users = [User(user_id, email, password, noc_transfer) for user_id, email, password, noc_transfer in cursor.fetchall()]
        return users

    def create_user(self, email, password, noc_transfer=0) -> User:
        query = "INSERT INTO users (email, password, noc_transfer) VALUES (?, ?, ?)"
        parameters = (email, password, noc_transfer)
        cursor = self.connection.execute_query(query, parameters)
        user_id = cursor.lastrowid  
        
        self.connection.commit()
        return User(user_id, email, password, noc_transfer)

    def get_user_by_email(self, email) -> User:
        query = "SELECT * FROM users WHERE email=?"
        parameters = (email,)
        user_data = self.connection.fetch_one(query, parameters)
        return User(*user_data) if user_data else None

    def get_user_by_id(self, user_id) -> User:
        query = "SELECT * FROM users WHERE user_id=?"
        parameters = (user_id,)
        user_data = self.connection.fetch_one(query, parameters)
        return User(*user_data) if user_data else None

    def update_user(self, user):
        query = "UPDATE users SET noc_transfer=? WHERE user_id=?"
        parameters = (user.noc_transfer, user.user_id)
        self.connection.execute_query(query, parameters)
        self.connection.commit()
        return User(user.user_id, user.email, user.password, user.noc_transfer)

    def delete_user(self, user_id)-> User:
        query_select = "SELECT * FROM users WHERE user_id=?"
        parameters_select = (user_id,)
        user_data = self.connection.fetch_one(query_select, parameters_select)

        if user_data:
            query_delete = "DELETE FROM users WHERE user_id=?"
            parameters_delete = (user_id,)
            self.connection.execute_query(query_delete, parameters_delete)
            self.connection.commit()

        return User(*user_data) if user_data else None
    
    def __str__(self):
        return f"All Users: {', '.join(str(user) for user in self.get_all_users())}"