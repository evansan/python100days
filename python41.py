user = {'name': None, 'age': None, 'gender': None, 'country': None}

def user_info():
    for key, value in user.items():
       user[key] = input(f"{key}: ")
    for key, value in user.items():
        print(f"{key}: {value}")

user_info()