import streamlit as st

st.title('Authentification via Google')

if st.button('se connecter'):
    st.login("google")