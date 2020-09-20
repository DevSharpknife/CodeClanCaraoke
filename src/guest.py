class Guest:

    def __init__(self, first_name, surname, age, wallet, fave_song):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.wallet = wallet
        self.fave_song = fave_song

    def get_guest_first_name(self):
        return self.first_name
    
    def get_guest_last_name(self):
        return self.last_name

    def get_guest_age(self):
        return self.age

    def wallet_cash_count(self):
        return self.wallet
    
    def remove_cash_from_wallet(self, cash_taken):
        self.wallet -= cash_taken

    

    
