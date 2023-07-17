import os, time, random

def hp():
    import random
    hp = random.randint(1,6) * random.randint(1,12) / 2 + 10
    return hp
    
def strength():
    import random
    strength = random.randint(1,6) * random.randint(1,8) / 2 + 12
    return strength

while True:
    name = input("What is the name of your character?: ")
    type = input("What is the type of your character?: ")

    os.system("clear")
    print(name)
    time.sleep(1)
    print("HP: " + str(hp()))
    time.sleep(1)
    print("Strength: " + str(strength()))
    
    repeat = input("again?: ")
    if repeat == "yes":
        os.system("clear")
    else:
        break
