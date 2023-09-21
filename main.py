import streamlit as st

import page.insert as insert
import page.select as select
import page.update as update
import page.delete as delete

st.sidebar.title = ("Menu")

page = st.sidebar.selectbox('Menu', ["Home", "Insert","Select" , "Update", "Delete"])

if page == "Insert":
    insert.insert()

if page == "Select":
    select.select_all()

if page == "Update":
    update.update()

if page == "Delete":
    delete.delete()