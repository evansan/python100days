print("MokeBeast")

user = {'Name': None, 'Type': None, 'Move': None, 'HP': None, 'MP': None}

def user_info():
    for key, value in user.items():
       user[key] = input(f"{key}: ")


def type_color():
    print()
    if user['Type'].lower() == "fire":
        for key, value in user.items():
            print('\033[33m' + f"{key}: {value}" + '\033[0m')
    elif user['Type'].lower() == "grass":
        for key, value in user.items():
            print('\033[32m' + f"{key}: {value}" + '\033[0m')
    elif user['Type'].lower() == "magic":
        for key, value in user.items():
            print('\033[35m' + f"{key}: {value}" + '\033[0m')   

user_info()
type_color()
