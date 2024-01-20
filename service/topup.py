from datetime import datetime
from models.topup import TopupList
from repository.abstract_class.topup import TopupAbstractRepository
from repository.abstract_class.saldo import SaldoAbstractRepository

class TopupService:
    def __init__(self, topup_repo: TopupAbstractRepository, saldo_repo: SaldoAbstractRepository):
        self.topup_repo = topup_repo
        self.saldo_repo = saldo_repo

    def create_topup(self, user_id, topup_no, topup_amount, topup_method):
        if topup_amount > 50000:
            raise ValueError("Topup amount exceeds the specified limit (50000)")

        topup = self.topup_repo.create_topup(user_id, topup_no, topup_amount, topup_method, datetime.now())
        if topup:
            saldo = self.saldo_repo.get_saldo_by_user_id(user_id)
            saldo.total_balance += topup_amount
            self.saldo_repo.update_saldo(user_id, saldo.total_balance)
        return topup

    def get_all_topups(self):
        topup = self.topup_repo.get_all_topups()

        return TopupList(topup)
    

    def get_topup_id(self, topup_id):
        return self.topup_repo.get_topup_id(topup_id)

    def get_topup_by_user_id(self, user_id):
        topup = self.topup_repo.get_topup_by_user_id(user_id)

        

        return TopupList(topup)
    

    def update_topup(self, topup_id, new_topup_amount, new_topup_method):
        if new_topup_amount > 50000:
            raise ValueError("New topup amount exceeds the specified limit (50000)")

        topup = self.topup_repo.get_topup_by_id(topup_id=topup_id)

        if topup:
            # Store the old topup amount and method for saldo adjustment
            old_topup_amount = topup.topup_amount
            old_topup_method = topup.topup_method

            # Update the topup in the repository
            updated_topup = self.topup_repo.update_topup(topup_id, new_topup_amount, new_topup_method, datetime.now())

            if updated_topup:
                # Adjust saldo based on the difference in topup amounts
                saldo = self.saldo_repo.get_saldo_by_user_id(updated_topup.user_id)
                saldo.total_balance += new_topup_amount - old_topup_amount

                # Update saldo in the repository
                self.saldo_repo.update_saldo(updated_topup.user_id, saldo.total_balance)

            return updated_topup

        return None

    def delete_topup(self, topup_id):
        topup = self.topup_repo.delete_topup(topup_id)
        return topup