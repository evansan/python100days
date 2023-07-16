print ("One milion to one")

counter = 0
answer = 654321

while True:
    counter += 1
    guess = int(input("what is your guess: "))
    if guess == answer:
        print("correct")
        break
    elif guess < answer:
        print("too low")
        continue
    else:
        print("too high")

print("It took you", counter, "times to guess")


