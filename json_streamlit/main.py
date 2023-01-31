import json
import pandas as pd
import streamlit as st

st.title("Title")


df = pd.read_json('data.json')

st.dataframe(df)

print(df)

# searchbar
to_search = st.text_input("Find:")

# inputs
name_input = st.text_input("Nome:")
surname_input = st.text_input("Cognome:")

if st.button("Add"):
    df.append({"Nome": name_input}, ignore_index=True)
    st.success("Aggiunto!")
    st.dataframe()


if to_search:
    i = df[df["Nome"] == to_search]
    st.dataframe(i)
else:
    st.write(f"No {to_search} in the table")

