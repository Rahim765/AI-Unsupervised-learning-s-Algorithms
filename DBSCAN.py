
from sklearn.neighbors import NearestNeighbors
import os
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
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


neighb = NearestNeighbors(n_neighbors=2) # creating an object of the NearestNeighbors class
nbrs=neighb.fit(img2) # fitting the data to the object
distances,indices=nbrs.kneighbors(img2)
distances = np.sort(distances, axis = 0) # sorting the distances
distances = distances[:, 1] # taking the second column of the sorted distances
plt.rcParams['figure.figsize'] = (5,3) # setting the figure size
plt.plot(distances) # plotting the distances
plt.show()

# pca = PCA(2)
# #Transform the data
# df = pca.fit_transform(img2)


#4000 , 3  , 3500 , 3
dbscan = DBSCAN(eps = 4000, min_samples =3)
db = dbscan.fit(img2)
labels = db.labels_
print(db)
print(labels)
#Getting unique labels

u_labels = np.unique(labels)
print(u_labels)


counter=0
for file_name in os.listdir("ORL/"):
    src_dir = "ORL/"+file_name
    if labels[counter] != -1:
        dst_dir = "DBSCAN/"+str(labels[counter])
        if not os.path.exists("DBSCAN/"+str(labels[counter])):
            os.mkdir("DBSCAN/"+str(labels[counter]))
        shutil.copy(src_dir,dst_dir)
    counter+=1






