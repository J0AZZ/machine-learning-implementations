# -*- coding: utf-8 -*-
"""
K Nearest Neighbors

Created on Wed Sep  9 19:04:43 2020

@author: Joás de Brito Ferreira Filho
"""

from math import sqrt
import heapq

# For two features (2-dimensional observations)

## EUCLIDIAN DISTANCE (L2 Norm)
def distance_2d(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Measures the euclidian distance from point to all points in plane (for 2-dimensional vectors)
# and returns the k nearest neighbors with respect to a point
def knn_2d(point, plane, k=1):
    distances = list()
    for p in plane:
        distances.append(distance_2d(point.coordinates, p.coordinates))
    return heapq.nsmallest(k, distances)

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
        distances.append(manhattan_distance(point.coordinates, p.coordinates))
    return heapq.nsmallest(k, distances)



