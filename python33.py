todo = []

def list():
    for item in todo:
        print(item)

print("To do list manager")

while True:
    menu = input("add, remove, or view?:")

    if menu == "view":
        list()
    elif menu == "add":
        item = input("what is the your agenda?")
        todo.append(item)
    elif menu == "remove":
        item = input("what do you want to remove?:")
        if item in todo:
            todo.remove(item)
        else:
            print(f"{item} is not in the list!")
    