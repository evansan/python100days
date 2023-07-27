todo = []

def list():
    for item in todo:
        print(item)

print("To do list manager")

while True:
    menu = input("add, remove, view, change, or clear?:\n")

    if menu == "view":
        list()
    elif menu == "add":
        item = input("what do you want to add?")
        if item in todo:
            print("this task is already in the list")
        else:
            todo.append(item)
    elif menu == "remove":
        item = input("what do you want to remove?:")
        confirm = input(f"are you sure you want to remove {item}?")
        if confirm == "yes":
            if item in todo:
                todo.remove(item)
            else:
                print(f"{item} is not in the list!")
        else:
            print(f"{item} not removed")
    elif menu == "change":
        item = input("what do you want to change?")
        new = input("change to what?")
        index = todo.index(item)
        todo[index] = new
    elif menu == "clear":
        todo = []
