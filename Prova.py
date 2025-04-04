import streamlit as st

st.title("Cadastro de funcionario")

nome = st.text_input("Digite o seu nome")

sobrenome = st.text_input("Digite o seu sobrenome")

dataNasc = st.date_input("Digite sua data de nascimento")

estadoCivil = st.text_input("Digite o seu estado civil")

salario = st.number_input("Digite o seu salario")

st.write(f"Nome completo: {nome} {sobrenome}")
st.write(f"Data de nascimento: {dataNasc}")
st.write(f"Estado civil: {estadoCivil}")
st.write(f"Salário: R${salario}")

if salario < 2500.00:
    st.write("O funcionario deve receber aumento")
    aumento = 0
    while aumento < 500:
        aumento = aumento +100
    st.write(f"O aumento é: {aumento} ")
else:
    st.write("O funcionario não deve receber aumento")

