todos = ["do homework", "eat", "go to sleep"]
while True:
    print("Your current todos are: ")
    print(', '.join(todos))
    # I made a todo list of items and printed the current todos in the list. For the todos to show up without the brakets I used print(', '.join(todos)).

    x = input("Would you like to add or remove a todo? ")

    # I made an input to ask the user if they want to add or remove an item from the list.
    if x == "add":
        y = input("What is the new todo? ")
        print("")
        print("-------------------------------------------------")
        (todos.append(y))
        print("Your current todos are: ")
        print("")
        print(', '.join(todos))
        print("")
    # I made a while loop make x == add and to have to user add any other todo, then the code would add the item to the end of the list and print out the new list.

    if x == "remove":
        z = int(input("Which # todo would you like to remove? "))
        z -= 1
        del todos[z]
        print("-------------------------------------------------")
        print("Your current todos are: ")
        print("")
        print(', '.join(todos))
        print("")
    # I created an if statement for the user if they want to remove an item, then I made the input convert to an interger and for then to start at 1 and not 0 I subtracted 1 from the variable z.