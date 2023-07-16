print("fill the blank in lyrics!")

counter = 0
while True:
    answer = (input("never gonna __ you up \n"))
    if answer == "give":
        break
    print("keep trying")
    counter += 1

print("You guessed", counter, "times!")