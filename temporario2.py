import datetime
import streamlit as st

ra = st.number_input(
    "Escreva o seu RA", value=None, placeholder="Escreva um numero..."
)
nome = st.text_input("Escreva seu nome", " ", key= "i_1")

cpf = st.number_input(
    "Escreva o seu CPF", value=None, placeholder="Escreva um numero..."
)


d = st.date_input("Data de nascimento", value=None)
                                        
    
