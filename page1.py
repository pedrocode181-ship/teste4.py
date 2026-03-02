import streamlit as st

st.set_page_config(page_title="Página 1")

st.title("🏠 Página 1")

if st.button("Ir para Página 2"):
    st.switch_page("pages/page2.py")
