import math
import os
import string
from itertools import groupby
# DBSCAN
# n : 83845
# tp : 1094
# fp : 589
# tn : 81411
# fn : 751
# rand index = 0.9840181286898444 %

# Kmeans
# n : 83845
# tp : 1072
# fp : 1535
# tn : 80490
# fn : 748
# rand index = 0.9727711849245632 %

# Agglomerative complete-link
# n : 83845
# tp : 1220
# fp : 1640
# tn : 80371
# fn : 614
# rand index = 0.973117061243962 %

# Agglomerative single_link
# n : 83845
# tp : 1285
# fp : 30625
# tn : 51580
# fn : 355
# rand index = 0.6305086767249091 %

# Agglomerative group link
# n : 83845
# tp : 1355
# fp : 3312
# tn : 78745
# fn : 433
# rand index = 0.9553342477190053 %


# Implemented Kmeans
# n : 83845
# tp : 1260
# fp : 941
# tn : 81065
# fn : 579
# rand index = 0.9818713101556443 %


n = math.comb(410 , 2)
km = "Kmeans/"
kmpp = "Kmeanspp/"
dbs = "DBSCAN/"
com_agl = "Complete_Agglomerative/"
sin_agl =  "Single_Agglomerative/"
gro_agl = "Group_Agglomerative/"
#algorihtm slection

algorihtm = kmpp

tp_fp =0
for i in range(len(os.listdir(algorihtm))):
    test_list = os.listdir(algorihtm+str(i)) # dir is your directory path
    number_files = len(test_list)
    tp_fp+= math.comb(number_files,2)



tp =0

for k in range(len(os.listdir(algorihtm))):
    test_list = os.listdir(algorihtm+str(k)) # dir is your directory path

    test_list.sort()

    # using lambda + itertools.groupby() + split()
    # group similar substrings
    res = [list(i) for j, i in groupby(test_list,
                                       lambda a: a.split('_')[1])]
    for p in res:
        count = len(p)
        if count > 1:
            tp+=math.comb(count,2)




fp = tp_fp - tp


fn =0

for i in range(41):
    sum =0
    for j in range(len(os.listdir(algorihtm))):
        test_list = os.listdir(algorihtm+str(j)) # dir is your directory path
        find=0
        for k in range(len(test_list)):
            # print("_"+str(i+1)+"jpg")
            # print(test_list[k])
            if test_list[k].endswith("_"+str(i+1)+".jpg"):
                find+=1
        if find > 1:
            sum+=math.comb(find,2)
    fn += math.comb(10,2) - (sum)




tn = n - (tp+fp+fn)

print("n : "+str(n))
print("tp : "+ str(tp))
print("fp : "+ str(fp))
print("tn : "+str(tn))
print("fn : "+ str(fn))


rand_ind = (tp+tn)/(tp+fp+fn+tn)
print("rand index = "+ str(rand_ind) + " %")






