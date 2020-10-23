import time
import pickle
import os

def get_users():
    users = []
    try:
        files = os.listdir('./SAVE/')
    except:
        print("Can´t open SAVE dir")
        exit(1)
    for i in files:
        i = './SAVE/' + i
        print(i)
        try:
            load_user = pickle.load(open(i,'rb'))
            users.append(load_user)
        except:
            print("Cant load file:", i)
    return users


# define user which has all needed data saved internally
class User:
    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.created = time.time()
        self.skins = [True, False, False, False, False, False]
        self.activeSkin = 0
        return

    # add balance to user
    # return new balance
    def add_balance(self, add):
        self.balance += add
        self.save()
        return self.balance

    # get users balance
    # ret actual balance
    def get_balance(self):
        return self.balance

    # subtract from balance
    # ret actual balance
    def sub_balance(self, sub):
        self.balance -= sub
        if self.balance < 0:
            self.balance = 0
        self.save()
        return self.balance

    # get users name
    # return name of user
    def get_name(self):
        return self.name

    # add new skin to user
    def add_skin(self, skinNum):
        self.skins[skinNum] = True
        self.save()
        return

    # return users skins
    def get_skins(self):
        return self.skins

    # set active skin
    def set_active_skin(self, skinNum):
        if skinNum < 0 or skinNum > 5:
            return
        self.activeSkin = skinNum
        self.save()
        return

    # get number from 0 to 5 representing user's current active skin
    def get_active_skin(self):
        return self.activeSkin

    def save(self):
        temp = 'SAVE/' + self.get_name() + '.pkl'
        temp_bkp = temp + '.bkp'
        try:
            os.rename(temp, temp_bkp)
        except:
            pass
        try:
            pickle.dump(self, open(temp,'wb'), pickle.HIGHEST_PROTOCOL)
        except:
            os.rename(temp_bkp, temp)
            print("Can´t dump pickle to file:",temp)
            return
        try:
            os.remove(temp_bkp)
        except:
            pass
        return

    def delete(self):
        temp = 'SAVE/' + self.get_name() + '.pkl'
        try:
            os.remove(temp)
        except:
            pass
        return
