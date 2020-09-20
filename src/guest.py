class Guest:

    def __init__(self, first_name, surname, age, wallet):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.wallet = wallet

    def wallet_cash_count(self):
        return self.wallet
    
    def remove_cash_from_wallet(self, cash_taken):
        self.wallet -= cash_taken