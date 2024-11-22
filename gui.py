import functions
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# fsg.theme('Default1')
fsg.theme('DarkBlack')

label_date = fsg.Text("Date:", key="date")
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo:", key="todo")
add_button = fsg.Button("Add")
list_box1 = fsg.Listbox(values=functions.get_todos(), size=(45, 10),
                        key="edit_todo", enable_events=True)
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

window = fsg.Window("My To-Do App",
                    layout=[
                        [label_date],
                        [label],
                        [input_box, add_button],
                        [list_box1,edit_button,complete_button],
                        [exit_button]],
                   font=("Helvetica", 20)
                    )

while True:
    event, values = window.read(timeout=500)
    window["date"].update(value=time.strftime("%b %d, %Y  %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["edit_todo"].update(values=todos)
            window["todo"].update(value="")

        case "Edit":
            try:
                todo_to_edit = values["edit_todo"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                num = todos.index(todo_to_edit)
                todos[num] = new_todo
                functions.write_todos(todos)
                window["edit_todo"].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item first!!", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["edit_todo"][0]

                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["edit_todo"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                fsg.popup("Please select an item first!!", font=("Helvetica", 20))

        case "Exit":
            break

        case "edit_todo":
            window["todo"].update(value=values["edit_todo"][0])


        case fsg.WIN_CLOSED:
            break



window.close()