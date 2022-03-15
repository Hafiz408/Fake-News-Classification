import streamlit as st
from predict_page import show_predict_page
from doc_page import doc


col1,col2 = st.sidebar.columns([1,5])
col2.image("icon.png",width=180)
col2.write("")

col1,col2 = st.sidebar.columns([2,5])
col2.title(""" Bogus Text""")      

col1,col2 = st.sidebar.columns([1,8])
col2.title("Menu")

col1,col2 = st.sidebar.columns([2,8])
choice = col2.radio("",['Detect','Brief'])

if choice == 'Detect':
    show_predict_page()
else:
    doc()