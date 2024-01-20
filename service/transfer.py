from models.transfer import TransferList
from datetime import datetime
from repository.abstract_class.transfer import TransferAbstractRepository
from repository.abstract_class.saldo import SaldoAbstractRepository

class TransferService:
    def __init__(self, transfer_repo: TransferAbstractRepository, saldo_repo: SaldoAbstractRepository):
        self.transfer_repo = transfer_repo
        self.saldo_repo = saldo_repo

    def create_transfer(self, transfer_from, transfer_to, transfer_amount):
        if transfer_amount > 50000:
            raise ValueError("Transfer amount exceeds the specified limit (50000)")

        transfer = self.transfer_repo.create_transfer(transfer_from, transfer_to, transfer_amount, datetime.now())
        if transfer:
            sender_saldo = self.saldo_repo.get_saldo_by_user_id(transfer_from)
            receiver_saldo = self.saldo_repo.get_saldo_by_user_id(transfer_to)

            sender_saldo.total_balance -= transfer_amount
            receiver_saldo.total_balance += transfer_amount

            self.saldo_repo.update_saldo(transfer_from, sender_saldo.total_balance)
            self.saldo_repo.update_saldo(transfer_to, receiver_saldo.total_balance)

        return transfer

    def get_all_transfers(self):
        transfer = self.transfer_repo.get_all_transfers()

        return TransferList(transfer)
    def get_transfer_by_user_id(self, user_id):
        transfer = self.transfer_repo.get_transfer_by_user_id(user_id)
        
        return TransferList(transfer)
    
    def update_transfer(self, transfer_id, new_transfer_amount):
        if new_transfer_amount > 50000:
            raise ValueError("New transfer amount exceeds the specified limit (50000)")

        transfer = self.transfer_repo.get_transfer_by_id(transfer_id)

        if transfer:
            # Store the old transfer amount and time for saldo adjustment
            old_transfer_amount = transfer.transfer_amount
            old_transfer_time = transfer.transfer_time

            # Update the transfer in the repository
            updated_transfer = self.transfer_repo.update_transfer(transfer_id, new_transfer_amount, datetime.now())

            if updated_transfer:
                # Adjust sender and receiver saldos
                sender_saldo = self.saldo_repo.get_saldo_by_user_id(updated_transfer.transfer_from)
                receiver_saldo = self.saldo_repo.get_saldo_by_user_id(updated_transfer.transfer_to)

                # Subtract old transfer amount and add new transfer amount to sender
                sender_saldo.total_balance += old_transfer_amount - new_transfer_amount

                # Subtract old transfer amount and add new transfer amount to receiver
                receiver_saldo.total_balance -= old_transfer_amount + new_transfer_amount

                # Update sender and receiver saldos in the repository
                self.saldo_repo.update_saldo(updated_transfer.transfer_from, sender_saldo.total_balance)
                self.saldo_repo.update_saldo(updated_transfer.transfer_to, receiver_saldo.total_balance)

            return updated_transfer

        return None
    
    def delete_transfer(self, transfer_id):
        return self.transfer_repo.delete_transfer(transfer_id)