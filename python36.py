
myList = []

def printList():
    for i in myList:
        print(i)
    print()

while True:
    firstname = input("what's your first name > ").title().strip()
    lastname = input("what's your last name > ").title().strip()
    fullname = firstname + " " + lastname

    if fullname not in myList:
        myList.append(fullname)
    else:
        print("ERROR: Duplicate name")
    printList()
