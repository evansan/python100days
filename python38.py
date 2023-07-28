myString = input("Type something > ")

for letter in myString:

    if letter.lower() == "y":
        print('\033[33m', end='')  # yellow
    elif letter.lower() == "g":
        print('\033[32m', end='')  # green
    elif letter.lower() == "p":
        print('\033[35m', end='')  # purple
    elif letter == " ":
        print('\033[0m', end='')  # default

    print(letter, end="")

print('\033[0m')
