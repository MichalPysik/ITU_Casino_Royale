import random


# return random number between 0-36
def generovani():

    return random.randint(0,36)

# return number which have been chosen
# @arg1 = bet amount
# @arg2 = number or string red, black, even, odd
def ruleta(user, bet, choice):

    if user.get_balance() < bet:
        return False

    cervena = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    cerna = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

    numb = generovani()
    # sazka na cislo
    if isinstance(choice, int) == True:
        if numb == choice:
            user.add_balance(bet*35)
        else:
            user.sub_balance(bet)
    elif isinstance(choice, str) == True:
        if choice == "red":
            try:
                cervena.index(numb)
                user.add_balance(bet)
            except:
                user.sub_balance(bet)
        elif choice == "black":
            try:
                cerna.index(numb)
                user.add_balance(bet)
            except:
                user.sub_balance(bet)
        elif choice == "odd":
            if numb % 2 == 1:
                user.add_balance(bet)
            else:
                user.sub_balance(bet)
        elif choice == "even":
            if numb % 2 == 0 and numb != 0:
                user.add_balance(bet)
            else:
                user.sub_balance(bet)
    else:
        print("unknown type")
        return -1

    return numb
