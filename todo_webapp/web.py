import streamlit as st
import functions


todos = functions.open_todos()


def add_todo():
    todo= st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")

for todo_items in todos:
     st.checkbox(todo_items)

st.text_input("", placeholder="Enter a todo", on_change=add_todo, key="new_todo")
st.button("Submit")

st.session_state