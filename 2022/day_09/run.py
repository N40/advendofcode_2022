import numpy as np
from copy import deepcopy
import re


def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	data = [l.split(" ") for l in lines]
	return [(d, int(n)) for d, n in data]

dirs = {
	"R": np.array([0, 1]),
	"U": np.array([-1, 0]),
	"L": np.array([0, -1]),
	"D": np.array([+1, 0])
}


def M_from_H_T(H, T):
	D = H - T
	M = np.array([0, 0])

	# adjacent
	if max(abs(D)) <= 1:
		return M

	# vertical / horizontal
	if D[1] != 0:
		M[1] = [-1, 1][int(D[1]) > 0]
	if D[0] != 0:
		M[0] = [-1, 1][int(D[0]) > 0]

	return M


def part_1(filename):
	data = read_input(filename)
	
	H = np.array([0, 0])
	T = np.array([0, 0])
	visits = set([tuple(H)])

	for d, n in data:
		for k in range(n):
			H += dirs[d]
			T += M_from_H_T(H, T)
			visits.add(tuple(T))


	print("1 >> ", len(visits))


def part_2(filename):
	data = read_input(filename)
	
	Chain = [np.array([0, 0]) for k in range(10)]
	visits = set([(0, 0)])

	for d, n in data:
		for k in range(n):
			Chain[0] += dirs[d]
			for i in range(1, 10):
				Chain[i] += M_from_H_T(Chain[i-1], Chain[i])
			visits.add(tuple(Chain[-1]))


	print("2 >> ", len(visits))


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")