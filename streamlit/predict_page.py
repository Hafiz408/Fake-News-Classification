import streamlit as st
import pickle
import pandas as pd




# def load_model():
#     with open('disease_predictor.pkl', 'rb') as file:
#          data = pickle.load(file)
#     return data

# data = load_model()

def show_predict_page():

    cols=st.columns([2,4,2])
    cols[1].image("icon.png",width=250)
    cols=st.columns([2,8,2])
    cols[1].title("|....... Bogus Text  ......|")
    st.write("")

    st.subheader("Enter the news :")
    text=st.text_area("",placeholder="Type or paste the news to be verified...")

    st.write("")
    cols = st.columns([2,1,2])
    ok = cols[1].button("Detect")

    if ok:
        if len(text) !=0:
            pass
        else:
            st.warning("No text found !!")
    