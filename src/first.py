import random

from second import PI


def returnNumber():
    if random.randint(0, 10) > 5:
        x = 5
    return x


print(returnNumber())
print(PI)
