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


class Skin:
    def __init__(self, Id, Type, path, price, name):
        self.id = Id
        self.type = Type
        self.path = path
        self.price = price
        self.name = name
        self.active = False
        return


    # return path to file with skin
    def get_path(self):
        return self.path

    # change price to new price
    def change_price(self, price):
        self.price = price;
        return

    # get price of skin
    def get_price(self):
        return self.price

    # set state of skin
    def set_active(self, state):
        self.active = state

    # return True if skin is active
    def is_active(self):
        return self.active

    # return name of skin
    def get_name(self):
        return self.name


# define user which has all needed data saved internally
class User:
    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.created = time.time()
        self.skins = []
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
        self.save()
        return self.balance

    # get users name
    # return name of user
    def get_name(self):
        return self.name

    # add new skin to user
    def add_skin(self, skin):
        self.skins.append(skin)
        self.save()
        return

    # return users skins
    def get_skins(self):
        return self.skins

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