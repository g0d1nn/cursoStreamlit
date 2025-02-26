import streamlit as st
import pandas as pd
from io import StringIO
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
  
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
