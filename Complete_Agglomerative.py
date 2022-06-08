
import os
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
# load the image
import numpy as np
from sklearn.decomposition import PCA
import glob
import shutil
import os
import math

img2 =[]


for file_name in os.listdir("ORL/"):
    matrix = np.array((cv2.imread("ORL/" + file_name))).reshape((cv2.imread("ORL/" + file_name)).size)
    img2.append(matrix)


pca = PCA(2)
#Transform the data
df = pca.fit_transform(img2)

aggloclust=AgglomerativeClustering(linkage="complete" ,n_clusters=41)
agl = aggloclust.fit(img2)
print(agl)
labels = aggloclust.labels_
print(labels)
#Getting unique labels

u_labels = np.unique(labels)
print(u_labels)
#plotting the results:




counter=0
for file_name in os.listdir("ORL/"):
    src_dir = "ORL/"+file_name
    dst_dir = "Complete_Agglomerative/"+str(labels[counter])
    if not os.path.exists("Complete_Agglomerative/"+str(labels[counter])):
        os.mkdir("Complete_Agglomerative/"+str(labels[counter]))
    shutil.copy(src_dir,dst_dir)
    counter+=1


