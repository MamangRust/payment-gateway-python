class User:
    def __init__(self, user_id, email, password, noc_transfer):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.noc_transfer = noc_transfer

    def __str__(self):
        return f"User(user_id={self.user_id}, email={self.email}, password={self.password}, noc_transfer={self.noc_transfer})"
    


class UserList(list):
    def __str__(self):
        return '[' + ', '.join(map(str, self)) + ']'