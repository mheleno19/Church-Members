import streamlit as st
import pandas as pd
import Pages.Clientes.Create as PageCreate
import Pages.Clientes.Query as PageQuery

st.title("Church Members")
st.sidebar.title("Menu")

Page_membros = st.sidebar.selectbox("Church Members", ["Incluir", "Consultar"])

if Page_membros == "Consultar":
    PageQuery.query()

elif Page_membros == "Incluir":
    PageCreate.create()
