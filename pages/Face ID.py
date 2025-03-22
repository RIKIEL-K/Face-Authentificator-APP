import streamlit as st
from config import add_user
from recognition import capture_photo,extract_face_descriptor,load_face_descriptor,compare_face
 
        
st.title('Face ID')
on = st.toggle("Je n'ai pas encore inscris mon visage")
st.warning("Garder votre visage en face de la caméra et appuyer sur la touche 'Espace' pour vous authentifier.")
if on:
    st.subheader("s'inscrire à Face ID")

    face_name = st.text_input('Entrez votre nom de compte')
    face_email = st.text_input('Entrez un courriel')

    btn = st.button("inscrire mon visage")
    if btn:
        if face_name:
            photo_path = capture_photo(face_name)
            if photo_path is not None:
                face_descriptor = extract_face_descriptor(photo_path)
                if face_descriptor:
                    add_user(face_name, face_email, "00000", face_descriptor)
                    print("descripteur facial ajouté avec succès !")
                else:
                    st.error("L'extraction du descripteur facial a échoué.")
        else:
            st.error("Veuillez entrer un nom de compte avant de continuer.")
    
else: 
    st.subheader("se connecter avec Face ID")

    face_name = st.text_input('Entrez le nom de votre compte')
    print(face_name)
    btn = st.button("Se connecter avec Face ID")

    if btn:
        if face_name:
            stored_descriptor = load_face_descriptor(face_name)

            if stored_descriptor is not None:
                captured_photo = capture_photo(face_name)

                if captured_photo is not None:
                    if compare_face(captured_photo, stored_descriptor):
                        st.success(f"Bienvenue, {face_name} !")
                    else:
                        st.error("Visage non reconnu. Veuillez réessayer.")
                else:
                    st.error("Aucune photo capturée.")
            else:
                st.error("Utilisateur non trouvé dans la base de données.")
        else:
            st.error("Veuillez entrer votre nom de compte avant de continuer.")

