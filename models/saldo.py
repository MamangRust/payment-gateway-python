class Saldo:
    def __init__(self, saldo_id, user_id, total_balance, withdraw_amount, withdraw_time):
        self.saldo_id = saldo_id
        self.user_id = user_id
        self.total_balance = total_balance
        self.withdraw_amount = withdraw_amount
        self.withdraw_time = withdraw_time

    def __str__(self):
        return f"Saldo ID: {self.saldo_id}, User ID: {self.user_id}, Total Balance: {self.total_balance}, Withdraw Amount: {self.withdraw_amount}, Withdraw Time: {self.withdraw_time}"
    

class SaldoList(list):
    def __str__(self):
        return '[' + ', '.join(map(str, self)) + ']'