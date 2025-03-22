import streamlit as st
from config import add_user,login_user


st.title('Authentication')

on = st.toggle("J'ai déjà un compte")

if on:
    
    st.subheader("Connexion")
    email_login = st.text_input('Entrez votre courriel')
    password_login = st.text_input('Entrez votre mot de passe', type='password')

    if st.button("Se connecter"):
        if email_login and password_login:
            if login_user(email=email_login, password=password_login):
                st.success("Connecté avec succès !")
            else:
                st.error(" Connexion échouée. Vérifiez vos identifiants.")
        else:
            st.error("Veuillez remplir tous les champs.")
else:
    st.subheader("Inscription")
    name = st.text_input('Entrez votre nom')
    email_signup = st.text_input('Entrez votre courriel')
    password_signup = st.text_input('Entrez votre mot de passe', type='password')

    if st.button("S'inscrire"):
        if name and email_signup and password_signup:
            add_user(name, email_signup, password_signup)
            st.success("Inscription réussie !")
        else:
            st.error("Veuillez remplir tous les champs.")


