import numpy as np
from distance import rechercheImage
from descripteur import concatenation,glcm,bitdesc,haralick_features
import streamlit as st
from PIL import Image
import tempfile
import os


# Chargement des signatures
signatures = {
    "GLCM": np.load("signaturesGLCM.npy", allow_pickle=True),
    "Haralick": np.load("signaturesHaralick.npy", allow_pickle=True),
    "BiT": np.load("signaturesBitdesk.npy", allow_pickle=True),
    "Concaténation": np.load("signaturesConcatenation.npy", allow_pickle=True)
}

# Choix des descripteurs et distances
descripteurs = ["GLCM", "Haralick", "BiT", "Concaténation"]
distances = ["euclidean", "manhattan", "chebyshev", "canberra"]



st.title('Recherche votre image')

file_image = st.file_uploader("Choisissez une image", type=["jpg", "png","jpeg"])


if file_image is not None:
    # Extraire l'extension du fichier original
    extension = os.path.splitext(file_image.name)[-1]
    image = Image.open(file_image)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=extension)
    image.save(temp_file.name)
    chemin_image = temp_file.name
    
    
    # Sélections utilisateur
    descripteur_choisi = st.selectbox("Choisissez le descripteur à utiliser", descripteurs)
    distance_choisie = st.selectbox("Choisissez la mesure de distance", distances)
    k = st.slider("Nombre d’images similaires à afficher", min_value=1, max_value=20, value=5)
    
    if st.button("Rechercher les images similaires"):
        # Extraction des caractéristiques de l’image requête
        if descripteur_choisi == "GLCM":
            vecteur = glcm(chemin_image)
        elif descripteur_choisi == "Haralick":
            vecteur = haralick_features(chemin_image)
        elif descripteur_choisi == "BiT":
            vecteur = bitdesc(chemin_image)
        elif descripteur_choisi == "Concaténation":
            vecteur = concatenation(chemin_image)

        resultat= rechercheImage(signaturebase=signatures[descripteur_choisi],carac_img_requests=vecteur,distances=distance_choisie,k=k)
        st.success(f"{k} image(s) similaire(s) trouvée(s) avec {descripteur_choisi} et la distance {distance_choisie} :")


        for i,(score,chemin,label) in enumerate(resultat):
            full_path = f'./dataset/{chemin}'
            image = Image.open(full_path)
            st.image(image, caption=f"Résultat {i+1} - Classe : {label} | Distance : {round(score, 3)}", use_container_width=True)