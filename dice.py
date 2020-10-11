import random

#hrac a pocitac hazi "nOfDice" poctem kostek, kdo hodi vice tak vyhral


def dice(user, bet, nOfDice):
    playerSum = enemySum = 0
    gameStatus = -1 # 0=won game, 1=lost game, 2=draw
    playerThrows = [] # list cisel 1 - 6 hozenych hracem
    enemyThrows = [] # to stejne hozene pocitacem
    for i in range (0, nOfDice):
        pThrow = random.randrange(6) + 1
        playerThrows.append(pThrow)
        eThrow = random.randrange(6) + 1
        enemyThrows.append(eThrow)
        playerSum += pThrow
        enemySum += eThrow

    if playerSum > enemySum:
        user.add_balance(bet)
        gameStatus = 0
    elif playerSum < enemySum:
        user.sub_balance(bet)
        gameStatus = 1
    else:
        gameStatus = 2
    return [gameStatus, playerSum, enemySum, playerThrows, enemyThrows]
