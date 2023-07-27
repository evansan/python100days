import os, time
listOfEmail = []

def prettyprint():
    os.system("clear")
    print("listOfEmail")
    print()
    for index in range(len(listOfEmail)):
        print(f"{index}:{listOfEmail[index]}")

while True:
    print( "SPAMMER Inc.")
    menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")

    if menu == "1":
        email = input ("Email > ")
        listOfEmail.append(email)
    elif menu== "2":
        email = input ( "Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyprint()
    elif menu == "4":
        for i in range(0,10):
            print(f"Email {i+1}\n")
            print(f"dear {listOfEmail[i]}")
            print("""
                  this is a spam email
                  click link to get 1 million
                  total legit
                  trust me bro
                  """)
            time.sleep(2)
 
    time.sleep(1)
    os.system("clear")