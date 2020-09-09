# -*- coding: utf-8 -*-
"""
K Nearest Neighbors

Created on Wed Sep  9 19:04:43 2020

@author: Joás de Brito Ferreira Filho
"""

from math import sqrt
import heapq

# For two features (2-dimensional observations)

#returns the distance between p1 and p2
def distance_2d(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

#returns the k nearest neighbors with respect to a point
def knn_2d(point, plane, k=1):
    distances = list()
    for p in plane:
        distances.append(distance_2d(point, p))
    return heapq.nsmallest(k, distances)

    
        



