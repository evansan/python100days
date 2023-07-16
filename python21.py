print("Math Game!")

score = 0
number = int(input("name your mutiples: "))

for i in range(1,11):
    answer = int(input(str(i) + " x " + str(number) + " = "))
    if answer == i * number:
        print("you are right")
        score += 1
    else:
        print("you are wrong")

if score == 10:
    print("good fucking work 😎")
else:
    print("you scored" , score , "Out of 10")