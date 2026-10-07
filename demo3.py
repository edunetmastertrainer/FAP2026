import streamlit as st
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('userdata.db')
cur = conn.cursor()
cur.execute('''
create table if not exists users(id integer primary key autoincrement,name text not null,age integer not null
,city text not null)
''')
conn.commit()

def add_user(name,age,city):
    cur.execute('INSERT INTO users(name,age,city) VALUES(?,?,?)',(name,age,city))
    conn.commit()

def get_users():
    cur.execute('SELECT * FROM users')
    return cur.fetchall()

def getuser_by_name(name):
    cur.execute('SELECT * FROM users WHERE name=?',(name,))
    return cur.fetchall()

st.title("User Data Entry Form")
name = st.text_input("Enter your name", key="name")
age = st.number_input("Enter your age", min_value=18, max_value=100, key="age")
city = st.text_input("Enter your city", key="city")
if st.button("Save"):
    if name and age and city:
        add_user(name, age, city)
        st.success("User data saved successfully!")
    else:
        st.error("Please fill in all fields.")

if st.button("Show All Users"):
    users = get_users()
    if users:
        st.write("All Users:")
        data = pd.DataFrame(users, columns=["ID", "Name", "Age", "City"])
        st.dataframe(data)

st.write("Search User by Name")
search_name = st.text_input("Enter name to search", key="search_name")
if st.button("Search"):
    if search_name:
        user = getuser_by_name(search_name)
        if user:
                st.write("Users Details:")
                data = pd.DataFrame(user, columns=["ID", "Name", "Age", "City"])
                st.dataframe(data)
        else:
            st.warning("No user found with that name.")
        