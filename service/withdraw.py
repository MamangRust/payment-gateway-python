from datetime import datetime
from models.withdraw import Withdraw, WithdrawList
from repository.abstract_class.withdraw import WithdrawAbstractRepository
from repository.abstract_class.saldo import SaldoAbstractRepository

class WithdrawService:
    def __init__(self, withdraw_repo: WithdrawAbstractRepository, saldo_repo: SaldoAbstractRepository):
        self.withdraw_repo = withdraw_repo
        self.saldo_repo = saldo_repo

    def create_withdraw(self, user_id, withdraw_amount) -> Withdraw:
        withdraw = self.withdraw_repo.create_withdraw(user_id, withdraw_amount, datetime.now())
        if withdraw:
            saldo = self.saldo_repo.get_saldo_by_user_id(user_id)
            saldo.withdraw_amount += withdraw_amount
            self.saldo_repo.update_saldo(user_id, saldo.total_balance, saldo.withdraw_amount)
        return withdraw

    def get_withdraw_by_id(self, withdraw_id) -> Withdraw:
        return self.withdraw_repo.get_withdraw_by_id(withdraw_id=withdraw_id)

    def get_all_withdraws(self):
        withdraw = self.withdraw_repo.get_all_withdraws()

        return WithdrawList(withdraw)
    
    def get_withdraw_by_user_id(self, user_id):
        withdraw = self.withdraw_repo.get_withdraw_by_user_id(user_id)

        return WithdrawList(withdraw)
    
    def update_withdraw(self, withdraw_id, new_withdraw_amount) -> Withdraw:
        withdraw = self.withdraw_repo.update_withdraw(withdraw_id, new_withdraw_amount, datetime.now())
        
        if withdraw:
            user_id = withdraw.user_id
            saldo = self.saldo_repo.get_saldo_by_user_id(user_id)
            saldo.withdraw_amount -= (withdraw.withdraw_amount - new_withdraw_amount)
            self.saldo_repo.update_saldo(user_id, saldo.total_balance, saldo.withdraw_amount)
        
        return withdraw

    
    def delete_withdraw(self, withdraw_id) -> Withdraw:
        return self.withdraw_repo.delete_withdraw(withdraw_id)