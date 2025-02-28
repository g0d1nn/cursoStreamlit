import datetime
import streamlit as st

nome = st.text_input("Escreva seu nome", " ", key= "i_1")
number = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)


d = st.date_input("Data de nascimento", value=None)
                                        
    
