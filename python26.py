import os, time

def music():
    print("playing some music")
    time.sleep(10)


def menu():
    print("MyPOD Music Player")
    time.sleep(3)
    print("enter 1 to play music")
    time.sleep(1)
    print("enter 2 to exit")
    time.sleep(1)
    print("enter anythng else to reload")

while True:
    menu()

    option = input("please select an option: ")

    if option == "1":
        music()
    elif option == "2":
        exit()
    else:
        os.system("clear")
        

