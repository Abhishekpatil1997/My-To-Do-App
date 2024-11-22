import functions
import time

now = time.strftime("%b %d, %Y  %H:%M:%S")
print(f"It is {now}.")


user_prompt = "Type add, show, edit, complete or exit:"


while True:
    user_input1 = input(user_prompt)
    user_action = user_input1.strip().lower()

    if user_action.startswith("add"):

            todo = user_action[4:]  + "\n"

            todos = functions.get_todos()

            todos.append(todo)

            functions.write_todos(todos_arg=todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")

        new_todos = [items.strip("\n") for items in todos]
        for index, item in enumerate(new_todos):
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:


            todos = functions.get_todos()

            number = int(user_action[5:])
            number = (number - 1)
            new_todo = input("Enter the new todo:")


            todos[number] = new_todo + "\n"

            functions.write_todos(todos_arg=todos)

        except ValueError:
            print("You command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:] +"\n")
            number = number - 1
            todos = functions.get_todos()

            todos.pop(number)

            functions.write_todos(todos_arg=todos)

        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, you entered a wrong command!!")
