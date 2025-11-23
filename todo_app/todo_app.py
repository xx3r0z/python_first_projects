#from functions import open_todos, write_todos
import functions
import time

# print(__name__)
now =  time.strftime("%b %d, %Y %H:%M")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    # .strip is used to remove the spaces and return just the text in the string

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = functions.open_todos()

        todos.append(todo)

        functions.write_todos(todos)
    elif user_action.startswith('show'):
        todos = functions.open_todos()

        # new_todos = []
        # for todo in todos:
        #     todo = todo.strip('\n')
        #     new_todos.append(todo)

        #Another way to write same thing
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            index = int(index) + 1
            print(f"{index}. {item}")
    elif user_action.startswith('edit'):
        try:
            todos = functions.open_todos()

            number = input("Number of todo to edit: ")
            number = int(number) - 1
            new_todo = input("Enter a todo to replace: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

            print(f"`{new_todo}` has been updated in your todo list")
        except ValueError:
            print('Your command is invalid')
            continue
    elif user_action.startswith('complete'):
        try:
            todos = functions.open_todos()

            number = int(user_action[9:])
            number = int(number) - 1
            completed_todo = todos[number].strip('\n')
            print(f"{completed_todo} marked as complete and will be deleted from your todo list")
            todos.pop(number)

            functions.write_todos(todos)
        except IndexError:
            print('Todo not on your list!')
        except ValueError:
            print('Enter the number of the todo you want to mark as complete!')
    elif user_action.startswith('exit'):
        break
    else:
        print("You input the wrong command! Try again")
print("Bye!")