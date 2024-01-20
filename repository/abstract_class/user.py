from typing import List
from models.user import User
from abc import ABC, abstractmethod

class UserAbstractRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id):
        """
        Retrieve a user by their unique identifier.

        Parameters:
        - user_id: int, unique identifier of the user.

        Returns:
        - dict: User information as a dictionary.
        """
        pass

    @abstractmethod
    def get_user_by_email(self, email) -> User: 
        """
        Retrieve a user by their email address.

        Parameters:
        - email: str, email address of the user.

        Returns:
        - dict: User information as a dictionary.
        """
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        """
        Retrieve all users.

        Returns:
        - list: List of dictionaries, each containing user information.
        """
        pass

    @abstractmethod
    def create_user(self, email, password, noc_transfer =0) -> User:
        """
        Create a new user.

        Parameters:
        - username: str, username of the new user.
        - email: str, email address of the new user.

        Returns:
        - dict: User information of the newly created user.
        """
        pass

    @abstractmethod
    def update_user(self, user) -> User:
        """
        Update user information.

        Parameters:
        - user: dict, user information to be updated.

        Returns:
        - dict: Updated user information.
        """
        pass

    @abstractmethod
    def delete_user(self, user_id) -> User:
        """
        Delete a user.

        Parameters:
        - user_id: int, unique identifier of the user to be deleted.

        Returns:
        - dict: User information of the deleted user.
        """
        pass
