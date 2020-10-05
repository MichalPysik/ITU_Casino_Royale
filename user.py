import time

#define user which has all needed data saved internally
class user:
    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.kostka = 1
        self.automat = 1
        self.ruleta = 1
        self.created = time.time()
        return

    #add balance to user
    #return new balance
    def add_balance(self, add):
        self.balance += add
        return self.balance

    #get users balance
    #ret actual balance
    def get_balance(self):
        return self.balance

    #subtract from balance
    #ret actual balance
    def sub_balance(self, sub):
        self.balance -= sub
        return self.balance

    #get users name
    #return name of user
    def get_name(self):
        return self.name