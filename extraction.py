import os
import cv2
import numpy as np
from descripteur import concatenation,glcm,haralick_features,bitdesc



def extraction_signatures_concatenation(chemin_repertoire):
    list_caracteristiques=[]
    for root,_,files in os.walk(chemin_repertoire):
        for file in files:
            if file.lower().endswith(('.png','.jpg', '.jpeg')):
                # Lire l'image
                chemin_image = os.path.relpath(os.path.join(root, file),chemin_repertoire)
                path = os.path.join(root, file)
                caracteristiques = concatenation(path)
                # print(caracteristiques)
                class_name=os.path.dirname(chemin_image)
                list_caracteristiques.append(caracteristiques+[class_name,chemin_image])
                # la classe c'est le nom du contient qui contient l'image
    
    signatures=np.array(list_caracteristiques)
    np.save("signaturesConcatenation.npy",signatures)
    
def extraction_signatures_GLCM(chemin_repertoire):
    list_caracteristiques=[]
    for root,_,files in os.walk(chemin_repertoire):
        for file in files:
            if file.lower().endswith(('.png','.jpg', '.jpeg')):
                # Lire l'image
                chemin_image = os.path.relpath(os.path.join(root, file),chemin_repertoire)
                path = os.path.join(root, file)
                caracteristiques = glcm(path)
                # print(caracteristiques)
                class_name=os.path.dirname(chemin_image)
                list_caracteristiques.append(caracteristiques+[class_name,chemin_image])
                # la classe c'est le nom du contient qui contient l'image
    
    signatures=np.array(list_caracteristiques)
    np.save("signaturesGLCM.npy",signatures)


def extraction_signatures_haralick(chemin_repertoire):
    list_caracteristiques=[]
    for root,_,files in os.walk(chemin_repertoire):
        for file in files:
            if file.lower().endswith(('.png','.jpg', '.jpeg')):
                # Lire l'image
                chemin_image = os.path.relpath(os.path.join(root, file),chemin_repertoire)
                path = os.path.join(root, file)
                caracteristiques = haralick_features(path)
                # print(caracteristiques)
                class_name=os.path.dirname(chemin_image)
                list_caracteristiques.append(caracteristiques+[class_name,chemin_image])
                # la classe c'est le nom du contient qui contient l'image
    
    signatures=np.array(list_caracteristiques)
    np.save("signaturesHaralick.npy",signatures)
    
def extraction_signatures_bitdesk(chemin_repertoire):
    list_caracteristiques=[]
    for root,_,files in os.walk(chemin_repertoire):
        for file in files:
            if file.lower().endswith(('.png','.jpg', '.jpeg')):
                # Lire l'image
                chemin_image = os.path.relpath(os.path.join(root, file),chemin_repertoire)
                path = os.path.join(root, file)
                caracteristiques = bitdesc(path)
                # print(caracteristiques)
                class_name=os.path.dirname(chemin_image)
                list_caracteristiques.append(caracteristiques+[class_name,chemin_image])
                # la classe c'est le nom du contient qui contient l'image
    
    signatures=np.array(list_caracteristiques)
    np.save("signaturesBitdesk.npy",signatures)

    
    
def main():
    # extraction_signatures_concatenation("./dataset/")
    # extraction_signatures_GLCM("./dataset/")
    # extraction_signatures_haralick("./dataset/")
    # extraction_signatures_bitdesk("./dataset/")
    print("Début extraction Concatenation")
    extraction_signatures_concatenation("./dataset/")
    print("Fin extraction Concatenation")
    
    print("Début extraction GLCM")
    extraction_signatures_GLCM("./dataset/")
    print("Fin extraction GLCM")

    print("Début extraction Haralick")
    extraction_signatures_haralick("./dataset/")
    print("Fin extraction Haralick")

    print("Début extraction Bitdesk")
    extraction_signatures_bitdesk("./dataset/")
    print("Fin extraction Bitdesk")
    
if __name__ == "__main__":
    main()
    
    
