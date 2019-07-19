import numpy as np
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import squareform
from difflib import SequenceMatcher

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

def ratcliffObershelp(x, y):
    return 1-SequenceMatcher(None, data[int(x)][1], data[int(y)][1]).ratio()

ratcliffobershelp_distance_matrix = pairwise_distances(X, metric=ratcliffObershelp)
ratcliffobershelp_distance_matrix=squareform(ratcliffobershelp_distance_matrix)
np.save('condensed_distance_matrix_ratcliffobershelp', ratcliffobershelp_distance_matrix)