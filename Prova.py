import streamlit as st

st.title("Cadastro de funcionario")

nome = st.text_input("Digite o seu nome")
print(nome)
sobrenome = st.text_input("Digite o seu sobrenome")
print(sobrenome)
dataNasc = st.date_input("Digite sua data de nascimento")
print(dataNasc)
estadoCivil = st.text_input("Digite o seu estado civil")
print(estadoCivil)
salario = st.number_input("Digite o seu salario")
print(salario)
