import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a todo")
input_box = fsg.InputText(tooltip="Enter todo")
add_button = fsg.Button("Add")
edit_button = fsg.Button("Edit")
complete = fsg.Button("Complete")
close = fsg.Button("Close App")

window = fsg.Window('My To-do App', layout=[[label], [input_box], [add_button], [edit_button, complete], [close]])
window.read()
window.close()