import random


def generovani():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    probability = [0.3,0.2,0.15,0.15,0.05,0.05,0.03,0.03,0.02,0.02]
    return random.choices(numbers, probability)[0]

def automat(user,bet):

    if user.get_balance() < bet:
        return False
    z_1 = generovani()
    z_2 = generovani()
    z_3 = generovani()


    #three same numbs
    if z_1 == z_2 and z_1 == z_3:
        # 0.3^3 = 3%
        if z_1 == 1:
            user.add_balance(20*bet)
        # 0.2^3 = 0.8%
        elif z_1 == 2:
            user.add_balance(40*bet)
        # 0.15^3 = 0.3375%
        elif z_1 == 3:
            user.add_balance(80*bet)
        # 0.15^3 = 0.3375%
        elif z_1 == 4:
            user.add_balance(80*bet)
        # 0.05^3 = 0,0125%
        elif z_1 == 5:
            user.add_balance(80*bet)
        # 0.05^3 = 0,0125%
        elif z_1 == 6:
            user.add_balance(150*bet)
        # 0.03^3 = 0,0027%
        elif z_1 == 7:
            user.add_balance(300*bet)
        # 0.03^3 = 0,0027%
        elif z_1 == 8:
            user.add_balance(300*bet)
        # 0.02^3 = 0,0008%
        elif z_1 == 9:
            user.add_balance(800*bet)
        # 0.02^3 = 0,0008%
        elif z_1 == 10:
            user.add_balance(800*bet)
    else:
        user.sub_balance(bet)
    return [z_1,z_2,z_3]