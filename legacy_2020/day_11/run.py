import numpy as np
from copy import deepcopy

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	lines = [list(l) for l in lines]
	print(f"h: {len(lines)}, w: {len(lines[0])}")
	return lines

def occ_in_dir(data, w, h, i, j, d_i, d_j):
	while i+d_i >= 0 and j+d_j >= 0 and j+d_j < w and i+d_i < h:
		i += d_i
		j += d_j
		if data[i, j] == "#":
			return True
		elif data[i, j] == "L":
			return False

	return False

def step_2(data):
	data = np.array(deepcopy(data))
	occ = np.array(data == "#", int)
	ns = np.zeros_like(occ)
	h, w = data.shape

	for i in range(len(data)):
		for j in range(len(data[0])):
			ns[i, j] += occ_in_dir(data, w, h, i, j,  1,  1)
			ns[i, j] += occ_in_dir(data, w, h, i, j,  0,  1)
			ns[i, j] += occ_in_dir(data, w, h, i, j, -1,  1)
			ns[i, j] += occ_in_dir(data, w, h, i, j, -1,  0)
			ns[i, j] += occ_in_dir(data, w, h, i, j, -1, -1)
			ns[i, j] += occ_in_dir(data, w, h, i, j,  0, -1)
			ns[i, j] += occ_in_dir(data, w, h, i, j,  1, -1)
			ns[i, j] += occ_in_dir(data, w, h, i, j,  1,  0)


	#print(ns)

	for i in range(len(data)):
		for j in range(len(data[0])):
			if ns[i, j] == 0 and data[i, j] == "L":
				data[i, j] = "#"
			elif ns[i, j] >= 5 and data[i, j] == "#":
				data[i, j] = "L"
	return data

	#print(ns)

def step_1(data):
	data = np.array(deepcopy(data))
	occ = np.array(data == "#", int)
	ns = np.zeros_like(occ)

	ns[:-1] += occ[1:]
	ns[1:] += occ[:-1]
	ns[:,:-1] += occ[:,1:]
	ns[:,1:] += occ[:,:-1]

	ns[:-1,:-1] += occ[1:,1:]
	ns[:-1,1:] += occ[1:,:-1]
	ns[1:,:-1] += occ[:-1,1:]
	ns[1:,1:] += occ[:-1,:-1]

	for i in range(len(data)):
		for j in range(len(data[0])):
			if ns[i, j] == 0 and data[i, j] == "L":
				data[i, j] = "#"
			elif ns[i, j] >= 4 and data[i, j] == "#":
				data[i, j] = "L"
	return data

def is_identical(a, b):
	return np.sum(a == b) == a.size

def part_1(filename):
	data_0 = np.array(read_input(filename))
	

	c = 1
	data = step_1(data_0)
	while not is_identical(data, data_0):
		c += 1
		data_0 = deepcopy(data)	
		data = step_1(data_0)		


	n = np.sum(data == "#")

	print(">> ", c, n)


def part_2(filename):
	data_0 = np.array(read_input(filename))
	
	c = 1
	data = step_2(data_0)
	while not is_identical(data, data_0):
		c += 1
		data_0 = deepcopy(data)	
		data = step_2(data_0)		


	n = np.sum(data == "#")

	print(">> ", c, n)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test")
	part_2("data")

