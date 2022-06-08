
#kmeans

import os
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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

kmeans=KMeans(n_clusters=41,init='k-means++' ,random_state=0)
y_means=kmeans.fit_predict(img2)
centers=np.array(kmeans.cluster_centers_)

#Getting unique labels

u_labels = np.unique(y_means)

#plotting the results:

for i in u_labels:
    plt.scatter(df[y_means == i , 0] , df[y_means == i , 1] , i)

plt.scatter(centers[:,0] , centers[:,1] , 41, color = 'k')
plt.show()


counter=0
for file_name in os.listdir("ORL/"):
    src_dir = "ORL/"+file_name
    dst_dir = "Kmeanspp/"+str(y_means[counter])
    if not os.path.exists("Kmeanspp/"+str(y_means[counter])):
        os.mkdir("Kmeanspp/"+str(y_means[counter]))
    shutil.copy(src_dir,dst_dir)
    counter+=1


