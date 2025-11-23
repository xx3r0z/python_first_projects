def open_todos():
    """ Read a text file and return a list of todo items"""
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todo_local):
    with open('todos.txt', 'w') as file:
        file.writelines(todo_local)
    return


# print(__name__)