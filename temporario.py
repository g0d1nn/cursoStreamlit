import streamlit as st

st.header("Cabeçalho")
st.toggle("Toggle")
st.button("Botão salvar")
st.text_area("Digite o texto")
st.text_input("")
st.selectbox(
  "Qual a sua cor favorita?",
  ("azul", "vermelho", "verde")
)
st.checkbox("Check")
