from models.user import UserList
from repository.abstract_class.user import UserAbstractRepository
from repository.abstract_class.saldo import SaldoAbstractRepository

class UserService:
    def __init__(self, user_repo: UserAbstractRepository, saldo_repo: SaldoAbstractRepository):
        self.user_repo = user_repo
        self.saldo_repo = saldo_repo

    def create_user(self, email, password, noc_transfer=0):
        user = self.user_repo.create_user(email, password, noc_transfer)
        if user:
            self.saldo_repo.create_saldo(user.user_id, total_balance=0)
        return user

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    def get_user_by_id(self, user_id):
        return self.user_repo.get_user_by_id(user_id)

    def update_user(self, user_id, new_noc_transfer):
        user = self.user_repo.get_user_by_id(user_id)
        if user:
            user.noc_transfer = new_noc_transfer
            updated_user = self.user_repo.update_user(user_id=user_id, new_noc_transfer=new_noc_transfer)
            return updated_user
        return None

    def delete_user(self, user_id):
        deleted_user = self.user_repo.delete_user(user_id)
        if deleted_user:
            self.saldo_repo.delete_saldo(user_id)
        return deleted_user

    def get_all_users(self):
        user = self.user_repo.get_all_users()

        return UserList(user)
