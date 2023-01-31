import sqlite3
import streamlit as st

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS table_name (
                    column1_name TEXT,
                    column2_name TEXT,
                    column3_name TEXT
                )""")
conn.commit()

def insert_data(column1, column2, column3):
    cursor.execute("INSERT INTO table_name (column1_name, column2_name, column3_name) VALUES (?, ?, ?)", (column1, column2, column3))
    conn.commit()

st.title("Database App")
column1_input = st.text_input("Enter Column 1 Data")
column2_input = st.text_input("Enter Column 2 Data")
column3_input = st.text_input("Enter Column 3 Data")

if st.button("Submit"):
    insert_data(column1_input, column2_input, column3_input)
    st.success("Data Added")

