myString = input("Type something > ")

for letter in myString:
    if letter.lower() == "b":
        print('\033[33m', end='')  # yellow
    elif letter.lower() == "g":
        print('\033[32m', end='')  # green
    elif letter.lower() == "p":
        print('\033[35m', end='')  # purple

    print(letter, end="")
    print('\033[0m', end='')  # back to default

# Reset color at end of string
print('\033[0m')