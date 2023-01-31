import sqlite3
import streamlit as st
import pandas as pd

conn = sqlite3.connect("table_test.json")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS table_name (
                    column1_name TEXT,
                    column2_name TEXT,
                    column3_name TEXT,
                    column4_name TEXT
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

column4list = ("Online", "Promo prevendita", "Prevendita", "Promo Tavolo", "Tavolo", "Omaggio")

column4_input = st.selectbox("Tipo di biglietto", column4list)

if st.button("Submit"):
    insert_data(column1_input, column2_input, column3_input, column4_input)
    st.success("Data Added")

if st.button("Clear"):
    clear_data()
    st.success("Data cleared")

cursor.execute("SELECT * FROM table_name")
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=["Nome", "Cognome", "Column 3", "Tipo biglietto"])

searching_name = st.text_input("Searching for: ")

st.dataframe(df)

# search
if searching_name:
    i = df[df["Nome"] == searching_name]
    st.dataframe(i)
    print(i["Nome"])
else:
    st.write(f"No {searching_name} in the table")
