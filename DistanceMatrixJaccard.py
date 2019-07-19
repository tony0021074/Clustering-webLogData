import numpy as np
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import squareform

data = []

with open("../input/anonymous-msweb.data", "r") as f:
    for line in f:
        if line[0] == "C":
            key = int(line[-6:-1])
            data.append([key,[]])
        if line[0] == "V" and key > 0:
            read_value = int(line[2:6])
            data[-1][1].append(read_value)

X = np.arange(len(data)).reshape(-1, 1)

def  myJaccard(x, y):
    x,y = int(x), int(y)
    intersect = len(set(data[x][1]).intersection(set(data[y][1])))
    union = len(set(data[x][1]).union(set(data[x][1])))
    return 1-intersect/union

jaccard_distance_matrix = pairwise_distances(X, metric=myJaccard)
jaccard_distance_matrix=squareform(jaccard_distance_matrix)
np.save('condensed_distance_matrix_jaccard', jaccard_distance_matrix)