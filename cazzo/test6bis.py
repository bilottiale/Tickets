import streamlit as st
import sqlite3
import pandas as pd

def save_ticket():
    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_type text,
            first_name text,
            last_name text,
            confirmed text,
            sold text,
            public_relations_person text,
            collector text,
            money text,
            collected text
        )
    """)
    c.execute("""
        INSERT INTO tickets (ticket_type, first_name, last_name, confirmed, sold, public_relations_person, collector, money, collected)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (ticket_type, first_name, last_name, confirmed, sold, public_relations_person, collector, money, collected))
    conn.commit()

    st.write("Tabelle dei biglietti:")
    tickets = c.execute("SELECT * FROM tickets").fetchall()
    st.table(tickets)

    conn.close()
    # Code to save the ticket information to the database
    pass

st.title("Form per biglietti")

ticket_type = st.selectbox("Tipo di biglietto", ["Online", "Promo prevendita", "Prevendita", "Promo Tavolo", "Tavolo", "Omaggio"])

first_name = st.text_input("Nome")
last_name = st.text_input("Cognome")

confirmed = st.selectbox("Confermato", ["SI", "NO"])
sold = st.selectbox("Venduto", ["SI", "NO"])
public_relations_person = st.text_input("PR")

collector = st.selectbox("Chi raccoglie?", ["Maca", "Dichi", "Nick", "Greco"])

money = st.selectbox("Prezzo", ["0€", "16€", "22€", "25€", "30€"])

collected = st.selectbox("Raccolti?", ["SI", "NO"])

st.write("")

if st.button("SALVA"):
    save_ticket()
    st.success("Biglietto salvato")
