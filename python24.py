
import random

print("Infinity Dice")

def dice():
    sides = int(input("how many side"))
    print(random.randint(1,sides))

dice()
while True:
    repeat = input("roll again?")
    if repeat == "yes":
        dice()
    else:
        break