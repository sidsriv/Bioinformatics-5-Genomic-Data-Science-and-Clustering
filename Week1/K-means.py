__author__ = 'Siddhant'

import os
from math import sqrt
from operator import itemgetter
import sys


def point_dist(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i]-b[i])**2
    return sqrt(d)


def dist_set(a, s):
    l = [point_dist(a, b) for b in s]
    return min(l)


def cent_grav(s):
    center = [0.0 for _ in range(m)]
    for item in s:
        for i in range(m):
            center[i] += item[i]
    weighted_center = [t/len(s) for t in center]
    return weighted_center


def closest_center(a):
    distances = [point_dist(a, point) for point in centers]
    index = min(enumerate(distances), key=itemgetter(1))[0]
    return index


def interpreter(conn):
    first = conn.readline().strip().split(' ')
    kk = int(first[0])
    mm = int(first[1])
    point_sett = list()
    for raw_line in conn:
        point = raw_line.strip().split(' ')
        float_point = [float(i) for i in point]
        point_sett.append(float_point)
    return kk, mm, point_sett


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        k, m, point_set = interpreter(f)
    n = len(point_set)
    centers = point_set[0:k]
    no_improv = False
    while not no_improv:
        # Assigns each point to its closest center
        grouping = {i: [] for i in range(k)}
        for point in point_set:
            grouping[closest_center(point)].append(point)
        # Measures new centers from groupings
        new_centers = list()
        for i in range(k):
            new_centers.append(cent_grav(grouping[i]))
        # Checks for improvement, exits loop in the absence of improvement
        old_to_new = sum(dist_set(point, centers) for point in new_centers)
        no_improv = (old_to_new == 0.0)
        centers = new_centers
    with open('lloyd_alg.txt', 'w') as g:
        for point in centers:
            ss = ['{0:.3f}'.format(val) for val in point]
            g.write(' '.join(ss)+'\n')