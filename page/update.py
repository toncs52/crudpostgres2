import sys
import streamlit as st
sys.path.insert(1, 'controller')
import client as client

def update():
    st.title("Update")
    
    update_id = st.number_input("Input ID", format="%d" , step=1)
    input_fullname = st.text_input(label="Fullname")
    input_email = st.text_input(label="Email")
    input_age = st.text_input(label="Age")
    if st.button("Update"):


        client.update(input_fullname, input_email,input_age,update_id)
        st.success("Updated person")