import automat
import dice
import ruleta

def Automat(user, bet):
    return automat.automat(user, bet)

def Dice(user, bet, nOfDice):
    return dice.dice(user,bet,nOfDice)

def Ruleta(user, bet, choice):
    return ruleta.ruleta(user, bet, choice)
