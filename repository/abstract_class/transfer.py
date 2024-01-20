from typing import List
from models.transfer import Transfer
from abc import ABC, abstractmethod

class TransferAbstractRepository(ABC):

    @abstractmethod
    def create_transfer(self, transfer_from, transfer_to, transfer_amount, transfer_time) -> Transfer:
        """
        Create a new transfer entry between users.

        Parameters:
        - transfer_from: int, unique identifier of the user initiating the transfer.
        - transfer_to: int, unique identifier of the user receiving the transfer.
        - transfer_amount: int, the amount of money being transferred.
        - transfer_time: datetime, timestamp of the transfer.

        Returns:
        - None
        """
        pass

    @abstractmethod
    def get_transfer_by_id(self, transfer_id) -> Transfer:
        pass

    @abstractmethod
    def get_transfer_by_user_id(self, user_id) -> List[Transfer]:
        """
        Retrieve transfer information for a user by their unique identifier.

        Parameters:
        - user_id: int, unique identifier of the user.

        Returns:
        - dict: Transfer information as a dictionary.
        """
        pass
    
    @abstractmethod
    def get_all_transfers(self) -> List[Transfer]:
        """
        Retrieve information for all transfers.

        Returns:
        - list: List of dictionaries, each containing transfer information.
        """
        pass

    @abstractmethod
    def update_transfer(self, transfer_id, new_transfer_amount, new_transfer_time) -> Transfer:
        """
        Update transfer information.

        Parameters:
        - transfer_id: int, unique identifier of the transfer entry.
        - new_transfer_amount: int, the updated amount of the transfer.
        - new_transfer_time: datetime, the updated timestamp of the transfer.

        Returns:
        - None
        """
        pass
    
    @abstractmethod
    def delete_transfer(self, transfer_id) -> Transfer:
        """
        Delete transfer information.

        Parameters:
        - transfer_id: int, unique identifier of the transfer entry.

        Returns:
        - None
        """
        pass
