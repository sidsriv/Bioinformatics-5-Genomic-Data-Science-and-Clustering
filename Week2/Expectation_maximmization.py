__author__ = 'Siddhant'

import sys
from math import sqrt, exp


def point_dist(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i]-b[i])**2
    return sqrt(d)


def new_centers(points, matrix):
    new_cents = list()
    for j in range(k):
        new_cent = [0.0 for _ in range(m)]
        total_prob = 0.0
        for i, p in enumerate(points):
            local_prob = matrix[i][j]
            total_prob += local_prob
            for kk in range(m):
                new_cent[kk] += local_prob * p[kk]
        new_cent_div = [flo/total_prob for flo in new_cent]
        new_cents.append(new_cent_div)
    return new_cents


def expectation_matrix(points, cent):
    """From the original point_set and current centers, builds expectation matrix
    Matrix is made so that expect[i][j] is the assignment of point i to center j"""
    expect = list()
    for p in points:
        prob = list()
        for c in cent:
            val = exp(-1*stiff*point_dist(p, c))
            prob.append(val)
        tot = sum(prob)
        true_prob = [i/tot for i in prob]
        expect.append(true_prob)
    return expect


def interpreter(conn):
    first = conn.readline().strip().split(' ')
    kk = int(first[0])
    mm = int(first[1])
    stifff = float(conn.readline().strip())
    point_sett = list()
    for raw_line in conn:
        poi = raw_line.strip().split(' ')
        float_point = [float(i) for i in poi]
        point_sett.append(float_point)
    return kk, mm, stifff, point_sett


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        k, m, stiff, point_set = interpreter(f)
    n = len(point_set)
    centers = point_set[0:k]
    steps = 100
    for _ in range(steps):
        expectation = expectation_matrix(point_set, centers)
        centers = new_centers(point_set, expectation)
    with open('soft_k_means.txt', 'w') as g:
        for point in centers:
            ss = ['{0:.3f}'.format(val) for val in point]
            g.write(' '.join(ss)+'\n')