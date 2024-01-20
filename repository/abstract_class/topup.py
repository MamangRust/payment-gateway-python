from typing import List
from models.topup import Topup
from abc import ABC, abstractmethod

class TopupAbstractRepository(ABC):
    @abstractmethod
    def create_topup(self, user_id, amount) -> Topup:
        """
        Create a new top-up entry for a user.

        Parameters:
        - user_id: int, unique identifier of the user.
        - amount: int, the amount of money to be added to the user's balance.

        Returns:
        - None
        """
        pass

    @abstractmethod
    def get_all_topups() -> List[Topup]:
        """
        Retrieve all top-up information.

        """
        pass

    @abstractmethod
    def get_topup_id(self, topup_id) -> Topup:
        pass

    @abstractmethod
    def get_topup_by_user_id(self, user_id) -> List[Topup]:
        """
        Retrieve top-up information for a user by their unique identifier.

        Parameters:
        - user_id: int, unique identifier of the user.

        Returns:
        - dict: Top-up information as a dictionary.
        """
        pass

    @abstractmethod
    def update_topup(self, topup_id, new_topup_amount) ->Topup:
        """
        Update top-up information.

        Parameters:
        - topup_id: int, unique identifier of the top-up entry.
        - new_topup_amount: int, the updated amount of the top-up.

        Returns:
        - None
        """
        pass

    @abstractmethod
    def delete_topup(self, topup_id) -> Topup:
        """
        Delete top-up information.

        Parameters:
        - topup_id: int, unique identifier of the top-up entry.

        Returns:
        - None
        """
        pass
