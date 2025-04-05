import numpy as np
from scipy.spatial import distance


def manhattan(v1,v2):
    v1=np.array(v1).astype("float")
    v2=np.array(v2).astype("float")
    dist = np.sum(np.abs(v1-v2))
    return dist

def euclidean(v1,v2):
    v1=np.array(v1).astype("float")
    v2=np.array(v2).astype("float")
    dist = np.sqrt(np.sum((v1-v2)**2))
    return dist

def chebyshev(v1,v2):
    v1=np.array(v1).astype("float")
    v2=np.array(v2).astype("float")
    dist = np.max(np.abs(v1-v2))
    return dist

def canberra(v1,v2):
    v1=np.array(v1).astype("float")
    v2=np.array(v2).astype("float")
    dist = np.sum(np.abs(v1-v2)/(np.abs(v1)+np.abs(v2)))
    return dist


def rechercheImage(signaturebase,carac_img_requests,distances,k):
    list_similaires=[]
    for instance in signaturebase:
        carac,label,img_chemin = instance[0:-2],instance[-2],instance[-1] #la case -2 constient la classe et -1 contient le chemin vers le fichier
        if distances =='canberra':
            dist = canberra(carac,carac_img_requests)
        if distances =="euclidean":
            dist = euclidean(carac,carac_img_requests)
        if distances =="chebyshev":
            dist = chebyshev(carac,carac_img_requests)
        if distances =="manhattan":
            dist = manhattan(carac,carac_img_requests)
        list_similaires.append((dist,img_chemin,label))
    list_similaires.sort(key=lambda x:x[0])
    return list_similaires[:k]

#deux images sont similaires si la distance tend vers 0