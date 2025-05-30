import streamlit as st

st.balloons()
st.title("Hello world!")
x=st.text_input("Enter your Name")
y=st.text_input("Enter your email")

st.write(f"hi {x}, your email id {y} is correct know!")
st.balloons()
