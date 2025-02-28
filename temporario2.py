import datetime
import streamlit as st

st.title("Aluno")

RA = st.text_input("Escreva seu RA", " ", key= "i_1")
cpf = st.text_input("Escreva seu CPF", " ", key= "i_2")
nome = st.text_input("Escreva seu nome", " ", key= "i_3")

d = st.date_input("Data de nascimento", value=None)

uploaded_files = st.file_uploader(
    "Escolha uma foto", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
                                        
    
