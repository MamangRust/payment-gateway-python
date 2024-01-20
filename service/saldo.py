from models.saldo import SaldoList
from repository.abstract_class.saldo import SaldoAbstractRepository

class SaldoService:
    def __init__(self, saldo_repo: SaldoAbstractRepository):
        self.saldo_repo = saldo_repo

    def create_saldo(self, user_id, total_balance, withdraw_amount=0, withdraw_time=None):
        return self.saldo_repo.create_saldo(user_id, total_balance, withdraw_amount, withdraw_time)

    def get_saldo_by_user_id(self, user_id):
        return self.saldo_repo.get_saldo_by_user_id(user_id)

    def get_all_saldos(self):
        saldo = self.saldo_repo.get_all_saldo()

        return SaldoList(saldo)

    def update_saldo(self, user_id, new_total_balance, withdraw_amount=0, withdraw_time=None):
        saldo = self.saldo_repo.get_saldo_by_user_id(user_id)
        if saldo:
            saldo.total_balance += new_total_balance
            updated_saldo = self.saldo_repo.update_saldo(user_id=user_id,total_balance=saldo.total_balance, withdraw_amount=withdraw_amount, withdraw_time=withdraw_time)
            return updated_saldo
        return None

    def delete_saldo(self, user_id):
        return self.saldo_repo.delete_saldo(user_id)