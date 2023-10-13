import random


def shuffle(items):
    for i in range(len(items) - 1, 0, -1):
        pick = random.randint(0, i)
        items[pick], items[i] = items[i], items[pick]
    return items
