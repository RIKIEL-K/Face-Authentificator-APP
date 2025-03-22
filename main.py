import streamlit as st
from config import add_user,login_user
from recognition import capture_photo,extract_face_descriptor,load_face_descriptor,compare_face


st.title('Google Authentification')

if st.button('Authenticate via Google'):
    st.login("google")


st.title('Normal Authentication')

st.subheader("Inscription")
name = st.text_input('Entrez votre nom')
email_signup = st.text_input('Entrez votre courriel (Inscription)')
password_signup = st.text_input('Entrez votre mot de passe (Inscription)', type='password')

if st.button("S'inscrire"):
    if name and email_signup and password_signup:
        add_user(name, email_signup, password_signup)
        st.success("Inscription réussie !")
    else:
        st.error("Veuillez remplir tous les champs.")

# Section de connexion
st.subheader("Connexion")
email_login = st.text_input('Entrez votre courriel (Connexion)')
password_login = st.text_input('Entrez votre mot de passe (Connexion)', type='password')

if st.button("Se connecter"):
    if email_login and password_login:
        if login_user(email=email_login, password=password_login):
            st.success("Connecté avec succès !")
        else:
            st.error(" Connexion échouée. Vérifiez vos identifiants.")
    else:
        st.error("Veuillez remplir tous les champs.")
        
st.title('Face Authentification')
st.subheader("s'inscrire à l'authentification faciale")

face_name = st.text_input('Entrez votre nom de compte')

btn = st.button("S'inscrire à l'authentification faciale")
if btn:
    if face_name:
        photo_path = capture_photo(face_name)
        if photo_path:
            face_descriptor = extract_face_descriptor(photo_path)
            if face_descriptor:
                add_user(face_name, "", "", face_descriptor)
                print("descripteur facial ajouté avec succès !")
            else:
                st.error("L'extraction du descripteur facial a échoué.")
    else:
        st.error("Veuillez entrer un nom de compte avant de continuer.")

st.subheader("se connecter avec l'authentification faciale")

face_name = st.text_input('Re-entrez votre nom de compte')
btn = st.button("Se connecter avec l'authentification faciale")

if btn:
    if face_name:
        stored_descriptor = load_face_descriptor(face_name)

        if stored_descriptor is not None:
            captured_photo = capture_photo()

            if captured_photo is not None:
                if compare_face(captured_photo, stored_descriptor):
                    st.success(f"Bienvenue, {face_name} !")
                    st.markdown("[Accéder à votre espace](https://votre-site.com/espace-prive)")
                else:
                    st.error("Visage non reconnu. Veuillez réessayer.")
            else:
                st.error("Aucune photo capturée.")
        else:
            st.error("Utilisateur non trouvé dans la base de données.")
    else:
        st.error("Veuillez entrer votre nom de compte avant de continuer.")