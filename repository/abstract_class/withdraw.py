from typing import List
from models.withdraw import Withdraw
from abc import ABC, abstractmethod

class WithdrawAbstractRepository(ABC):
    @abstractmethod
    def create_withdraw(self, user_id, withdraw_amount) -> Withdraw:
        """
        Create a new withdrawal entry for a user.

        Parameters:
        - user_id: int, unique identifier of the user initiating the withdrawal.
        - withdraw_amount: int, the amount of money being withdrawn.

        Returns:
        - None
        """
        pass

    @abstractmethod
    def get_all_withdraws(self) -> List[Withdraw]:
        """
        Retrieve information for all withdrawals.

        Returns:
        - list: List of dictionaries, each containing withdrawal information.
        """
        pass

    @abstractmethod
    def get_withdraw_by_user_id(self, user_id) -> Withdraw:
        """
        Retrieve withdrawal information for a user by their unique identifier.

        Parameters:
        - user_id: int, unique identifier of the user.

        Returns:
        - dict: Withdrawal information as a dictionary.
        """
        pass

    @abstractmethod
    def get_withdraw_by_id(self, withdraw_id) -> Withdraw:
        """
        Retrieve withdrawal information by its unique identifier.

        Parameters:
        - withdraw_id: int, unique identifier of the withdrawal entry.

        Returns:
        - dict: Withdrawal information as a dictionary.
        """
        pass

    @abstractmethod
    def update_withdraw(self, withdraw_id, new_withdraw_amount) -> Withdraw:
        """
        Update withdrawal information.

        Parameters:
        - withdraw_id: int, unique identifier of the withdrawal entry.
        - new_withdraw_amount: int, the updated amount of the withdrawal.

        Returns:
        - None
        """
        pass

    @abstractmethod
    def delete_withdraw(self, withdraw_id) -> Withdraw:
        """
        Delete withdrawal information.

        Parameters:
        - withdraw_id: int, unique identifier of the withdrawal entry.

        Returns:
        - None
        """
        pass
