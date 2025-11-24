import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a todo")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.open_todos(), key='todosList',
                       enable_events=True, size=[45, 10])
edit_button = fsg.Button("Edit")
complete = fsg.Button("Complete")
close = fsg.Button("Close App")

layout = [[label], [input_box, add_button], [list_box, edit_button], [complete], [close]]

window = fsg.Window('My To-do App', layout=layout, font=('Helvetica', 20))
# window.read() returns a tuple containing the event(e.g btn click) and a dictionary containing a key
# and the value of the key is what is submitted in the input box. The default key starts from 0...
# but it can be renamed by giving it an explicit value in the input_box
#('Add', {'todo': 'content submitted'})
#event, values represents the 2 content in the tuple so they can be worked on separately

while True:
    event, values = window.read()
    print('Event: ', event)
    print("Values: ", values)

    match event:
        case 'Add':
            todos = functions.open_todos()

            todos.append(values['todo'] + '\n')

            functions.write_todos(todos)

            window['todosList'].update(values=todos)

        case 'Edit':
            edit_todo = values['todosList'][0]
            new_todo = values['todo']

            todos = functions.open_todos()

            index = todos.index(edit_todo)
            print('index: ', index)
            print('todos: ', todos)
            print('edit todo: ', edit_todo)
            todos[index] = new_todo + '\n'

            functions.write_todos(todos)

            window['todosList'].update(values=todos)

        case 'todosList':
            window['todo'].update(values['todosList'][0].strip('\n'))

        case 'Complete':
            complete_todo = values['todosList'][0]
            todos = functions.open_todos()
            index = todos.index(complete_todo)
            todos.pop(index)

            functions.write_todos(todos)

            window['todosList'].update(values=todos)


        case fsg.WIN_CLOSED:
            break


window.close()