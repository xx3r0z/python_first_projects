import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a todo")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add")
edit_button = fsg.Button("Edit")
complete = fsg.Button("Complete")
close = fsg.Button("Close App")

window = fsg.Window('My To-do App',
                    layout=[[label], [input_box], [add_button], [edit_button, complete], [close]],
                    font=('Helvetica', 20))
# window.read() returns a tuple containing the event(e.g btn click) and a dictionary containing a key
# and the value of the key is what is submitted in the input box. The default key starts from 0...
# but it can be renamed by giving it an explicit value in the input_box
#('Add', {'todo': 'content submitted'})
#event, values represents the 2 content in the tuple so they can be worked on separately

while True:
    event, values = window.read()

    match event:
        case 'Add':
            todos = functions.open_todos()

            todos.append(values['todo'] + '\n')

            functions.write_todos(todos)
        case fsg.WIN_CLOSED:
            break


window.close()