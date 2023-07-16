

def login_system():
    while True:
        username = input("what is your username: ")
        password = input("what is your password: ")

        if username == "alex" and password == "passw0rd":
            print("Welcome")
            break
        else:
            print("I do not recognize this combination of username and password")

login_system()