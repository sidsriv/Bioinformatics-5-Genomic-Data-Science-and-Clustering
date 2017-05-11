__author__ = 'Siddhant Srivastava'


import random
import math
import sys

filename = sys.argv[1]

with open(filename) as file:
	temp = []
	for line in file:
		temp.append(line)

k,d = map(int,temp[0].split(' '))

points = []
for i in range(1,len(temp)):
	points.append(map(float,temp[i].split(' ')))

def distance(X,Y):
	d = len(X)
	dis = 0
	for i in range(d):
		dis += (X[i] - Y[i])**2
	return math.sqrt(dis)

def incremental_farthest_search(points, k):
    remaining_points = points[:]
    solution_set = []
    #solution_set.append(remaining_points.pop(random.randint(0, len(remaining_points) - 1)))
    solution_set.append(points[0])
    for _ in range(k-1):
        distances = [distance(p, solution_set[0]) for p in remaining_points]
        for i, p in enumerate(remaining_points):
            for j, s in enumerate(solution_set):
                distances[i] = min(distances[i], distance(p, s))
        solution_set.append(remaining_points.pop(distances.index(max(distances))))
    return solution_set

solution = incremental_farthest_search(points,3)

for i in range(len(solution)):
	for d in range(len(solution[0])):
		print solution[i][d],
	print '\n'