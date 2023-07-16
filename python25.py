

print("CHARACTER STAT GENERATOR")

def dice():
    import random
    hp = " "
    hp = random.randint(1,6) * random.randint(1,8)
    return hp


print(" you character has " + str(dice()) + " HP ")

