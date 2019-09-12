import random


def roll(arg:str):
    params = arg.lower().split('d')
    times = int(params[0])
    sides = int(params[1])

    response = 'Rolled '
    sum = 0

    for i in range(0, times):
        rolled = random.randrange(1, int(sides))
        sum += rolled
        response += str(rolled) + (' = ' if i == times - 1 else ' + ')

    response += str(sum)
    return response