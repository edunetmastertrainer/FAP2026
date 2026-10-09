import streamlit as st

st.title("Contact Page")
st.write("This is the Contact Page of our multi-page Streamlit app!")
st.text_input("Your Name")
st.text_input("Your Email")
st.text_area("Your Message")
if st.button("submit"):
    st.success("Thank you for your message! We will get back to you soon.")