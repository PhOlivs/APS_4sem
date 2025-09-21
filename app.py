import streamlit as st
from src.controller.controle import controle

st.title("Análise de Desmatamento")

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
if uploaded_file:
    controller = controle(uploaded_file)
    df = controller.analisar_dados()
    
    if df is not None:
        st.write("Dados Carregados com Sucesso!")
        st.dataframe(df.head())
    else:
        st.write("Falha ao carregar os dados.")