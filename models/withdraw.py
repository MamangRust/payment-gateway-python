class Withdraw:
    def __init__(self, withdraw_id, user_id, withdraw_amount, withdraw_time):
        self.withdraw_id = withdraw_id
        self.user_id = user_id
        self.withdraw_amount = withdraw_amount
        self.withdraw_time = withdraw_time

    def __str__(self):
        return f"Withdraw ID: {self.withdraw_id}, User ID: {self.user_id}, Withdraw Amount: {self.withdraw_amount}, Withdraw Time: {self.withdraw_time}"
    

class WithdrawList(list):
    def __str__(self):
        return '[' + ', '.join(map(str, self)) + ']'