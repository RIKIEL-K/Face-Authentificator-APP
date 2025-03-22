import streamlit as st
import cv2
import os
import numpy as np
import face_recognition
import sqlite3
import pickle


# Charger les descripteurs depuis la base de données SQLite
DB_NAME = "users_faces.db"

# Créer le dossier 'capture' s'il n'existe pas
CAPTURE_FOLDER = "capture"
os.makedirs(CAPTURE_FOLDER, exist_ok=True)

# Fonction pour capturer une photo avec la webcam
def capture_photo(name):
    capture = cv2.VideoCapture(0)
    st.write("Appuyez sur 'Espace' pour capturer une photo ou 'Q' pour quitter.")

    while True:
        ret, frame = capture.read()
        if not ret:
            st.error("Erreur lors de l'ouverture de la caméra.")
            break

        cv2.imshow("Capture d'image", frame)

        # Appuyer sur 'Espace' pour capturer la photo
        if cv2.waitKey(1) & 0xFF == ord(' '):
            photo_path = os.path.join(CAPTURE_FOLDER, f"{name}.jpg")
            cv2.imwrite(photo_path, frame)
            print(f"Photo capturée et enregistrée")
            break

        # Appuyer sur 'Q' pour quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

    return photo_path


# Fonction pour extraire les descripteurs faciaux
def extract_face_descriptor(photo_path):
    image = face_recognition.load_image_file(photo_path)
    encodings = face_recognition.face_encodings(image)
    
    if encodings:
        return pickle.dumps(encodings[0])  # Sérialisation du descripteur facial
    else:
        st.error("Aucun visage détecté sur l'image.")
        return None
    
    


def load_face_descriptor(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT face_descriptor FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return pickle.loads(result[0])  # Désérialisation du descripteur
    return None

# Fonction pour comparer les descripteurs faciaux
def compare_face(photo, stored_descriptor):
    photo = cv2.imread(photo)
    image_reduit = cv2.resize(photo, (0, 0), None, 0.25, 0.25)
    face_locations = face_recognition.face_locations(image_reduit)
    face_encodings = face_recognition.face_encodings(image_reduit, face_locations)

    for encode, loc in zip(face_encodings, face_locations):
        match = face_recognition.compare_faces([stored_descriptor], encode)
        distance = face_recognition.face_distance([stored_descriptor], encode)
        minDist=np.argmin(distance)

        if match[minDist]:
            return True

    return False