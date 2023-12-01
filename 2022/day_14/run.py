import numpy as np
from copy import deepcopy
import re

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]

	data = []
	for line in lines:
		nodes = []
		for node in line.split(" -> "):
			x, y = (int(node.split(",")[0]), int(node.split(",")[1]))
			nodes.append((x,y))
		data.append(nodes)
	return data

def read_input(filename):
	data = read_input_lines(filename)

	cave = np.zeros((1001,1001), int)
	for nodes in data:
		for (j_0, i_0), (j_1, i_1) in zip(nodes[1:], nodes[:-1]):
			if i_0 > i_1 or j_0 > j_1:
				(j_0, i_0), (j_1, i_1) = (j_1, i_1), (j_0, i_0)

			cave[i_0:i_1+1, j_0:j_1+1] = 1

	return cave

def drop_sand_at(cave, i, j):

	if j < 0 or j > 1000:
		return None

	if cave[i, j] != 0:
		return None

	below = np.where(cave[i:, j] > 0)[0]

	# fall through
	if len(below) == 0:
		return None

	i_b = min(below) + i

	# check left/right
	if cave[i_b, j-1] == 0:
		return drop_sand_at(cave, i_b, j-1)
	if cave[i_b, j+1] == 0:
		return drop_sand_at(cave, i_b, j+1)

	# insert
	cave[i_b - 1, j] = 2
	return cave

def part_1(filename):
	cave = read_input(filename)

	while True:
		r = drop_sand_at(cave, 0, 500)
		if r is None:
			break

		cave = r
	
	print("1 >> ", np.sum(cave == 2))


def part_2(filename):
	cave = read_input(filename)

	i_floor = max([i for i in range(len(cave)) if np.sum(cave[i,:]) > 0]) + 2
	cave[i_floor, :] = 1

	while True:
		r = drop_sand_at(cave, 0, 500)
		if r is None:
			break

		cave = r

	print("2 >> ", np.sum(cave == 2))


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")