class Transfer:
    def __init__(self, transfer_id,transfer_from, transfer_to, transfer_amount, transfer_time) -> None:
        self.transfer_id = transfer_id
        self.transfer_from = transfer_from
        self.transfer_to = transfer_to
        self.transfer_amount = transfer_amount
        self.transfer_time = transfer_time

    def __str__(self):
        return f'Transfer ID: {self.transfer_id}, Transfer From: {self.transfer_from}, Transfer To: {self.transfer_to}, Transfer Amount: {self.transfer_amount}, Transfer Time: {self.transfer_time}'


class TransferList(list):
    def __str__(self):
        return '[' + ', '.join(map(str, self)) + ']'