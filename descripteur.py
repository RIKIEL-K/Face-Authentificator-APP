from skimage.feature import graycomatrix, graycoprops
from mahotas.features import haralick
from BiT import bio_taxo
import cv2
import numpy as np


def glcm(chemin):
    data = cv2.imread(chemin,0)
    co_matrice = graycomatrix(data, [1], [np.pi/2], None, symmetric=True, normed=True)
    contrast = float(graycoprops(co_matrice, 'contrast')[0,0])
    dissimilarity = float(graycoprops(co_matrice, 'dissimilarity')[0,0])
    homogeneity = float(graycoprops(co_matrice, 'homogeneity')[0,0])
    energy = float(graycoprops(co_matrice, 'energy')[0,0])
    correlation = float(graycoprops(co_matrice, 'correlation')[0,0])
    ASM = float(graycoprops(co_matrice, 'ASM')[0,0])
    return [contrast, dissimilarity, homogeneity, energy, correlation,ASM]

def haralick_features(chemin):
    data = cv2.imread(chemin,0)
    features = haralick(data).mean(0).tolist()
    features = [float(i) for i in features]
    return features

def bitdesc(chemin):
    data = cv2.imread(chemin,0)
    features = bio_taxo(data)
    features = [float(i) for i in features]
    return features

def concatenation(chemin):
    return glcm(chemin) + haralick_features(chemin) + bitdesc(chemin)