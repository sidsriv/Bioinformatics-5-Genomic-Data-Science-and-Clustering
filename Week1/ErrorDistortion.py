__author__ = 'Siddhant Srivastava'


import math
import sys

filename = sys.argv[1]

with open(filename) as file:
	temp = []
	for line in file:
		temp.append(line)

k,d = map(int,temp[0].split(' '))

points = []
centers = []
for i in range(1,k+1):
	centers.append(map(float,temp[i].split(' ')))

for i in range(k+3,len(temp)):
	points.append(map(float,temp[i].split(' ')))

def distance(X,Y):
	d = len(X)
	dis = 0
	for i in range(d):
		dis += (X[i] - Y[i])**2
	return math.sqrt(dis)


def distortion_error(k,d,centers,points):
	error_sum = 0
	for point in points:
		min_dis = min(distance(point,center) for center in centers)
		error_sum += min_dis**2
	return error_sum/len(points)

print distortion_error(k,d,centers,points)
