from typing import Optional, List
from models.saldo import Saldo


class SaldoRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_saldo(self, user_id, total_balance, withdraw_amount=0, withdraw_time=None) -> Saldo:
        query = """
            INSERT INTO saldo (user_id, total_balance, withdraw_amount, withdraw_time)
            VALUES (?, ?, ?, ?)
        """
        parameters = (user_id, total_balance, withdraw_amount, withdraw_time)
        self.connection.execute_query(query, parameters)
        self.connection.commit()

        return self.get_saldo_by_user_id(user_id)

    def get_all_saldo(self) -> List[Saldo]:
        query = "SELECT * FROM saldo"
        saldo_data = self.connection.fetch_all(query)
        return [Saldo(*data) for data in saldo_data]

    def get_saldo_by_user_id(self, user_id) -> Optional[Saldo]:
        query = "SELECT * FROM saldo WHERE user_id=?"
        parameters = (user_id,)
        saldo_data = self.connection.fetch_one(query, parameters)

        if saldo_data:
            saldo_id, user_id, total_balance, withdraw_amount, withdraw_time = saldo_data
            return Saldo(saldo_id, user_id, total_balance, withdraw_amount, withdraw_time)
        else:
            return None

    def update_saldo(self, user_id, total_balance, withdraw_amount=0, withdraw_time=None) -> Optional[Saldo]:
        query = """
            UPDATE saldo
            SET total_balance=?, withdraw_amount=?, withdraw_time=?
            WHERE user_id=?
        """
        parameters = (total_balance, withdraw_amount, withdraw_time, user_id)
        self.connection.execute_query(query, parameters)
        self.connection.commit()

        return self.get_saldo_by_user_id(user_id)

    def delete_saldo(self, user_id) -> Optional[Saldo]:
        query_select = "SELECT * FROM saldo WHERE user_id=?"
        parameters_select = (user_id,)
        saldo_data = self.connection.fetch_one(query_select, parameters_select)

        if saldo_data:
            query_delete = "DELETE FROM saldo WHERE user_id=?"
            parameters_delete = (user_id,)
            self.connection.execute_query(query_delete, parameters_delete)
            self.connection.commit()

        return Saldo(*saldo_data) if saldo_data else None
