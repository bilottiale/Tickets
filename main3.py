import sqlite3
import streamlit as st
import pandas as pd

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS table_name (
                    column1_name TEXT,
                    column2_name TEXT,
                    column3_name TEXT,
                    column4_name text
                    )
               """)
conn.commit()

def insert_data(column1, column2, column3, column4):
    cursor.execute("""INSERT INTO table_name (column1_name, column2_name, column3_name, column4_name) VALUES (?, ?, ?, ?)""", (column1, column2, column3, column4))
    conn.commit()

def clear_data():
    cursor.execute("DELETE FROM table_name")
    conn.commit()

st.title("Database App")
column1_input = st.text_input("Enter Column 1 Data")
column2_input = st.text_input("Enter Column 2 Data")
column3_input = st.text_input("Enter Column 3 Data")

column4_input = st.selectbox("Tipo di biglietto", ["Online", "Promo prevendita", "Prevendita", "Promo Tavolo", "Tavolo", "Omaggio"])

if st.button("Submit"):
    insert_data(column1_input, column2_input, column3_input, column4_input)
    st.success("Data Added")

if st.button("Clear"):
    clear_data()
    st.success("Data cleared")

cursor.execute("SELECT * FROM table_name")
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=["Column 1", "Column 2", "Column 3", "Column 4"])

st.dataframe(df)
