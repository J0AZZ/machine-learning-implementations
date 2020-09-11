# -*- coding: utf-8 -*-
"""
K Means Clustering

Created on Fri Sep 11 14:00:31 2020

@author: Joás de Brito Ferreira Filho
"""

import random

# Manhattan Distance (L1 Norm)
def manhattan_distance(p1, p2):
    d = list()
    for i in range(len(p1)):
        d.append(abs(p1[i]-p2[i]))
    return d

def get_centroid(vectors):
    centroid = list()
    for v in vectors:
        for dimensions in v:
            

# Returns k clusters containing the same vectors passed as argument
def kmc(vectors, k):
    # k randomly selected vectors, to be used in the first iteration
    C = random.sample(vectors, k)
    
    clusters = list()
    for n in range(k):
        clusters.append(list())
        
    for v in vectors:
        distance_to_centroid_k = list()
        for c in C:
            distance_to_centroid_k.append(manhattan_distance(c, v))
        c_index = distance_to_centroid_k.argsort()[:1]
        clusters[c_index].append(v)
        
            