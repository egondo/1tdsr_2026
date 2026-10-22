import requests

import streamlit as st
import pandas as pd


st.header("Cadastro de partida")

time_mandante = st.text_input("Mandante: ")
gols_mandante = st.text_input("Gols Mandante: ")

time_visitante = st.text_input("Visitante: ")
gols_visitante = st.text_input("Gols Visitante: ")

if st.button("Cadastra"):
    st.write("Enviando a partida para o servidor")
    partida = {
        "mandante": time_mandante, "visitante": time_visitante,
        "gols_visitante": int(gols_visitante),
        "gols_mandante": int(gols_visitante)
    }

    resposta = requests.post("http://127.0.0.1:5000/partidas", json=partida)
    if resposta.status_code >= 200 and resposta.status_code < 300:
        #st.write(resposta.json())
        resposta = requests.get("http://127.0.0.1:5000/tabelas")
        lista = resposta.json()
        df = pd.DataFrame(lista)
        df = df[['nome', 'pontos', 'jogos', 'vitorias', 'empates', 'derrotas']]
        st.write(df)
