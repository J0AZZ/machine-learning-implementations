# -*- coding: utf-8 -*-
"""
K Nearest Neighbors

Created on Wed Sep  9 19:04:43 2020

@author: Joás de Brito Ferreira Filho
"""


## MANHATTAN DISTANCE (L1 Norm)
def manhattan_distance(p1, p2):
    distance = 0
    for i in range(len(p1)):
        distance += abs(p1[i] - p2[i])
    return distance

# Measures the Manhattan Distance from point to all points in plane 
# and returns the k smallest distances
def knn(point, plane, k):
    distances = list()
    for p in plane:
        distances.append([p, manhattan_distance(point.coordinates, p.coordinates)])
    index = distances.argsort()[:k]
    knn = list()
    for i in index:
        knn.append(plane[i])



