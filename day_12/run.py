import numpy as np
from copy import deepcopy
import re

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines

def read_input_matrix(filename):
	lines = read_input_lines(filename)
	lines = [list(l) for l in lines]
	print(f"h: {len(lines)}, w: {len(lines[0])}")
	
	i_s, j_s = np.where(np.array(lines) == "S")
	i_s = i_s[0]
	j_s = j_s[0]

	i_e, j_e = np.where(np.array(lines) == "E")
	i_e = i_e[0]
	j_e = j_e[0]

	lines = [[int(c, 36) - int("a", 36) for c in l] for l in lines]
	m = np.array(lines, int)

	return m, (i_s, j_s), (i_e, j_e)


steps = [(0,-1),(1,0),(0,1),(-1,0)]
names_steps = ["<","v",">","^"]

def rounte(m, starts, ij_e):
	distances = np.zeros_like(m) - 1

	h, w = m.shape

	for ij_s in starts:
		distances[ij_s] = 0

	currently_new = deepcopy(starts)

	done = False

	while not done and not len(currently_new) == 0:
		next_new = []
		for i_0, j_0 in currently_new:
			for d_i, d_j in steps:
				i_1, j_1 = (i_0 + d_i, j_0 + d_j)
				if i_1 >= h or j_1 >= w or i_1 < 0 or j_1 < 0:
					continue

				if distances[i_1, j_1] >= 0:
					continue
				

				if m[i_1, j_1] - m[i_0, j_0] <= 1:
					distances[i_1, j_1] = distances[i_0, j_0] + 1
					next_new.append((i_1, j_1))

				if distances[ij_e] > 0:
					done = True

		currently_new = deepcopy(next_new)

	return distances

def part_1(filename):
	m, ij_s, ij_e = read_input_matrix(filename)
	lines = read_input_lines(filename)

	distances = np.zeros_like(m) - 1
	distances[ij_s] = 0
	m[ij_s] = 0
	m[ij_e] = int("Z", 36) - int("A", 36)

	starts = [ij_s]

	distances = rounte(m, starts, ij_e)

	print("1 >> ", distances[ij_e])


def part_2(filename):
	m, ij_s, ij_e = read_input_matrix(filename)
	lines = read_input_lines(filename)

	distances = np.zeros_like(m) - 1
	distances[ij_s] = 0
	m[ij_s] = 0
	m[ij_e] = int("Z", 36) - int("A", 36)

	starts = []


	for i, j in zip(*np.where(m == 0)):
		starts.append((i,j))
		distances[i,j] = 0

	distances = rounte(m, starts, ij_e)

	print("2 >> ", distances[ij_e])


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")