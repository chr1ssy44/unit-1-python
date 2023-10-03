todos = ["do homework", "eat", "go to sleep"]
i = 0
print("Your current todos are: ")
print(', '.join(todos))

x = input("Would you like to add or remove a todo? ")

while x == "add":
    y = input("What is the new todo? ")
    (todos.append(y))
    print("Your current todos are: ")
    print(', '.join(todos))
    print("Your current todos are: ")
    break
if x == "remove":
    z = input("Which # todo would you like to remove? ")
for i, todos in enumerate(todos, 1):
    (todos.remove(z))
    print(i, todos)

