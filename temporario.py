import streamlit as st

st.header("Cabeçalho")
st.multiselect(
  "Quais suas cores favoritas",
  ["verde", "amarelo", "vermelho", "azul"],
  ["amarelo", "vermelho"]
)
st.toggle("Toggle")
st.button("Botão salvar")
st.text_area("Digite o texto")
st.text_input("")
st.selectbox(
  "Qual a sua cor favorita?",
  ("azul", "vermelho", "verde")
)

st.checkbox("Check")
