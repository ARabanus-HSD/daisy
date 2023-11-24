from random import randint

def dices(n_dices):
    dices_result = []
    for i in range(n_dices):
        dices_result.append(randint(1, 6))
    return dices_result

