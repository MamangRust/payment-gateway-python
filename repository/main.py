from .user import UserRepository

from .topup import TopupRepository
from .withdraw import WithdrawRepository
from .transfer import TransferRepository
from .saldo import SaldoRepository

class Repository:
    def __init__(self, db_connection):
        self.user_repository = UserRepository(db_connection)
        self.topup_repository = TopupRepository(db_connection)
        self.withdraw_repository = WithdrawRepository(db_connection)
        self.transfer_repository = TransferRepository(db_connection)
        self.saldo_repository =SaldoRepository(db_connection)