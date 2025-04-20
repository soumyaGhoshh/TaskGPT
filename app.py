import streamlit as st
from agent import break_down_task

st.set_page_config(page_title="TaskGPT", layout="centered")
st.title("TaskGPT: Smart Task Breakdown Agent")

task = st.text_input("Enter a task or goal ", "")

if st.button("Break it Down"):
    if task.strip():
        with st.spinner("Thinking..."):
            result = break_down_task(task)
        st.success("Here's your action plan!")
        st.markdown(result)
