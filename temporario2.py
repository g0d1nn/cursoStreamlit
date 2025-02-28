import datetime
import streamlit as st

st.title("Aluno")

ra = st.number_input(
    "Escreva o seu RA", value=None, placeholder="Escreva um numero..."
)

cpf = st.number_input(
    "Escreva o seu CPF", value=None, placeholder="Escreva um numero..."
)

nome = st.text_input("Escreva seu nome", " ", key= "i_1")


d = st.date_input("Data de nascimento", value=None)

uploaded_files = st.file_uploader(
    "Escolha uma foto", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
                                        
    
