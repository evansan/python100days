print("MokeBeast")

user = {'Name': None, 'Type': None, 'Move': None, 'HP': None, 'MP': None}

def user_info():
    for key in user:
        user[key] = input(f"{key}: ")
    for key, value in user.items():
        print(f"{key}: {value}")

def type_color():
    if user['Move'].lower() == "fire":
        print('\033[33m', end='')  # Set color to yellow
        for key, value in user.items():
            print(f"{key}: {str(value)}")
        print('\033[0m', end='')  # Reset color


user_info()
type_color()