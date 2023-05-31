import streamlit as st
import modules.functions as func

todos = func.get_data()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.update_data(todos)


st.title("To-Do App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.update_data(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="New/edit field", placeholder="Enter new to-do...",
              on_change=add_todo, key="new_todo")
