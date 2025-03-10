import random

def coin():
    val = random.random()
    if val > 0.5:
        return "heads!"
    else:
        return "tails!"