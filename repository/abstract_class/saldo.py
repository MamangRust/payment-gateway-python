from models.saldo import Saldo
from typing import List, Optional
from abc import ABC, abstractmethod

class SaldoAbstractRepository(ABC):
    @abstractmethod
    def create_saldo(self, user_id, total_balance, withdraw_amount=0, withdraw_time=None) -> Saldo:
        """
        Create a new saldo entry for a user.

        Parameters:
        - user_id: int, unique identifier of the user.
        - total_balance: int, the total balance of the user.
        - withdraw_amount: int, the amount of money withdrawn (default is 0).
        - withdraw_time: datetime, timestamp of the last withdrawal (default is None).

        Returns:
        - None
        """
        pass

    
    @abstractmethod
    def get_all_saldos(self) -> List[Saldo]:
        """
        Retrieve all saldo information.

        Returns:
        - list: List of dictionaries, each containing saldo information.
        """
        pass

    @abstractmethod
    def get_saldo_by_user_id(self, user_id) -> Saldo:
        """
        Retrieve saldo information for a user by their unique identifier.

        Parameters:
        - user_id: int, unique identifier of the user.

        Returns:
        - dict: Saldo information as a dictionary.
        """
        pass

    @abstractmethod
    def update_saldo(self, user_id, total_balance, withdraw_amount=0, withdraw_time=None) -> Saldo:
        """
        Update saldo information for a user.

        Parameters:
        - user_id: int, unique identifier of the user.
        - total_balance: int, the updated total balance of the user.
        - withdraw_amount: int, the updated amount of money withdrawn.
        - withdraw_time: datetime, the updated timestamp of the last withdrawal.

        Returns:
        - None
        """
        pass

    @abstractmethod
    def delete_saldo(self, user_id) -> Saldo:
        """
        Delete saldo information for a user.

        Parameters:
        - user_id: int, unique identifier of the user.

        Returns:
        - None
        """
        pass
