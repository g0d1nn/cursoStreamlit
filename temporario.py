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
st.color_picker("Escolha uma cor", "#00f900")

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
