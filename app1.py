
import streamlit as st

st.title("What is your name?")
name = st.text_input("Enter your name:")

if st.button('save'):
    st.write(f"My names's {name}!")#Install Localtunnel
