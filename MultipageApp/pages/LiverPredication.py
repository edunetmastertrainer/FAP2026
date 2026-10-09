import streamlit as st
import pickle

liver_model = pickle.load(open("Liver.pkl", 'rb'))

st.title("Liver Disease Prediction")
age = st.number_input("Enter Age", min_value=5, max_value=100)
gender = st.selectbox("Select Gender", ["Male", "Female"])
Total_bilirubin_level = st.number_input("Enter Total Bilirubin Level")
Direct_bilirubin_level = st.number_input("Enter Direct Bilirubin Level")
Liver_enzyme_level = st.number_input("Enter Liver Enzyme Level")
sgpt_level = st.number_input("Enter SGPT Level")
sgot_level = st.number_input("Enter SGOT Level")
Total_protein_level = st.number_input("Enter Total Protein Level")
Albumin_level = st.number_input("Enter Albumin Level")
agratio = st.number_input("Enter A/G Ratio")
if st.button("Predict"):
    new_data = [[age,{"Male":0,"Female":1}[gender],float(Total_bilirubin_level),float(Direct_bilirubin_level),Liver_enzyme_level,sgpt_level,sgot_level,float(Total_protein_level),float(Albumin_level),float(agratio)]]
    liver_prediction = liver_model.predict(new_data)
    if liver_prediction[0] == 1:
        st.warning("The patient is at low risk of having liver disease.")
    elif liver_prediction[0] == 2:
        st.success("The patient is at moderate risk of having liver disease.")
    else:
        st.error("The patient is at high risk of having liver disease. Please consult a doctor immediately.")