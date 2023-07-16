import random

counter = 0
number = random.randint(1,1000000)
print(number)

while True:
    guess = int(input("What is your guess?: "))
    if guess == number:
        print("you are right")
        break
    elif guess > number:
        print("too high")
        counter += 1
    else:
        print("too low")
        counter += 1

print("it only took you " + str(counter) + " times to get it")

    

