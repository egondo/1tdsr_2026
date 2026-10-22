import streamlit as st
import pandas as pd


st.header("Pagina que irá mostrar as notas de alguns alunos")

st.markdown("Tabela")
df = pd.DataFrame({"nome": ["Marcia", "Ana", "Fernando"], "CTP": [6, 8, 7.6], "DDD": [7.6, 5.6, 8.9], "Front": [9.6, 4.2, 7.0]})

st.write(df)