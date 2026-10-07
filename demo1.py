import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
st.title("Registration")
name = st.text_input("Enter your Name")
password = st.text_input("Eneter your Password",type="password")
if st.button("Sign-In"):
    st.write("Welcome Mr/Ms " + name)

myfile = st.file_uploader("Upload your csv file")
if myfile is not None:
    df = pd.read_csv(myfile)
    st.dataframe(df)




df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.bar_chart(df)