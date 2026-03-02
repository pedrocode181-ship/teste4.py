import streamlit as st

st.set_page_config(page_title="Teste", page_icon="🚀")

st.title("🚀 Teste Streamlit")

st.write("Se o botão funcionar, o deploy deu certo 😎")

if st.button("Clique aqui"):
    st.success("Funcionou!!! 🎉")