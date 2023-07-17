import os, time, random

def dice(side):
    result = random.randint(1,side)
    return result

def hp():
    hp = (dice(6) * dice(20) + 30)
    return hp
    
def strength():
    strength = (dice(6) * dice(6) / 2)
    return strength

p1_name = input("Player 1, what is the name of your character?: ")
p2_name = input("Player 2, what is the name of your character?: ")

p1_hp = hp()
p1_strength = strength()
p2_hp = hp()
p2_strength = strength()

def print_score(name, hp, strength):
    print(name)
    print("HP: ", hp)
    print("Strength: ", strength)
    print()

time.sleep(1)
os.system("clear")
print("battle time")

round = 0
while True:

    if p1_hp >= 0 and p2_hp >= 0:
        print("it is round ", round)
        p1_dice = dice(6)
        p2_dice = dice(6)

        if p1_dice == p2_dice:
            round += 1
        elif p1_dice > p2_dice:
            p2_hp -= p1_strength
            round += 1
        else:
            p1_hp -= p2_strength
            round += 1
            
        print_score(p1_name, p1_hp, p1_strength)
        print_score(p2_name, p2_hp, p2_strength)
        time.sleep(2)
        os.system("clear")

    elif p1_hp < 0:
        print(p2_name, "defeated", p1_name, "in round", round)
        break
    elif p2_hp < 0:
        print(p1_name, "defeated", p2_name, "in round", round)
        break
