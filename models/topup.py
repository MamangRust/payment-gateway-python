class Topup:
    def __init__(self, topup_id, user_id, topup_no, topup_amount, topup_method, topup_time):
        self.topup_id = topup_id
        self.user_id = user_id
        self.topup_no = topup_no
        self.topup_amount = topup_amount
        self.topup_method = topup_method
        self.topup_time = topup_time

    def __str__(self):
        return f"Topup ID: {self.topup_id}, User ID: {self.user_id}, Topup No: {self.topup_no}, Topup Amount: {self.topup_amount}, Topup Method: {self.topup_method}, Topup Time: {self.topup_time}"
    

class TopupList(list):
    def __str__(self):
        return '[' + ', '.join(map(str, self)) + ']'