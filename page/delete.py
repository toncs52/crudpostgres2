import sys
import streamlit as st
sys.path.insert(1, 'controller')
import client as client

def delete():
    st.title("Delete")
    
    delete_id = st.number_input("Input ID", format="%d" , step=1)
    if st.button("Delete"):
        client.delete(delete_id)
        st.success("delete person")