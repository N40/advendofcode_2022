import numpy as np

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	lines = [list(l) for l in lines]
	print(f"h: {len(lines)}, w: {len(lines[0])}")
	return lines

def find_trees(data, d_i, d_j):
	w = len(data[0])

	i = d_i
	j = d_j

	num_trees = 0

	while i < len(data):
		num_trees += (data[i][j % w] == "#")
		i += d_i
		j += d_j

	return num_trees

def part_1(filename):
	data = read_input(filename)
	w = len(data[0])

	num_trees = find_trees(data, 1, 3)

	print(">> ", num_trees)


def part_2(filename):
	data = read_input(filename)

	n_1_1 = find_trees(data, 1, 1)
	n_1_3 = find_trees(data, 1, 3)
	n_1_5 = find_trees(data, 1, 5)
	n_1_7 = find_trees(data, 1, 7)
	n_2_1 = find_trees(data, 2, 1)

	prod = n_1_1 * n_1_3 * n_1_5 * n_1_7 * n_2_1

	print(">>     ", n_1_1)
	print(">>     ", n_1_3)
	print(">>     ", n_1_5)
	print(">>     ", n_1_7)
	print(">>     ", n_2_1)

	print(">> ", prod)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")