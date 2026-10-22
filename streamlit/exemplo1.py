import streamlit as st

nome = st.text_input("Digite o seu nome: ")
idade = st.number_input("Idade: ")

curso = st.selectbox("Qual curso vc faz?", ["", "ADS", "SI", "CCP", "Jogos", "ADM"])

if curso:
    st.write(f"Olá {nome}, {idade} anos")
    st.write(f"Curso: {curso}")