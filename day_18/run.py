import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	data = [tuple(np.array(l.split(","), int)) for l in lines]
	return data

def neighbors_for(cube, w = None):
	neighbors = []
	i, j, k = cube
	neighbors.append((i+1, j, k))
	neighbors.append((i-1, j, k))
	neighbors.append((i, j+1, k))
	neighbors.append((i, j-1, k))
	neighbors.append((i, j, k+1))
	neighbors.append((i, j, k-1))

	# optional range limit
	if w is not None:
		candidates = neighbors
		neighbors = []
		w = int(w)
		for i, j, k in candidates:
			if i < 0 or i >= w or  j < 0 or j >= w or  k < 0 or k >= w:
				continue
			neighbors.append((i, j, k))

	return neighbors

def part_1(filename):
	data = read_input(filename)

	sides = 6 * len(data)
	print("    >", sides)

	for i, cube in enumerate(data):
		neighbors = neighbors_for(cube)
		for other in neighbors:
			if other in data[:i]:
				sides -= 2

	print("1 >> ", sides)


def part_2(filename):
	data = read_input(filename)

	w = np.max(np.array(data)) + 1
	m = np.zeros((w, w, w), int)

	for ijk in data:
		m[ijk] = 1

	seeds = [(0, 0, 0)]
	surface_count = 0

	# swamping algo
	for _ in range(w*w):
		if _ % 10 == 0:
			print(f"i: {_:4}  seeds: {len(seeds):6}  srfc: {surface_count}")
		if len(seeds) == 0:
			break

		next_seeds = []
		for seed in seeds:
			if m[seed] == 2: # already checked
				continue
			if m[seed] == 1: # is droplet
				surface_count += 1
				continue

			m[seed] = 2 # mark checked
			next_seeds += neighbors_for(seed, w)
		seeds = deepcopy(next_seeds)


	# edge correction
	print("    >", surface_count)
	surface_count += np.sum(np.array(data) == 0)
	surface_count += np.sum(np.array(data) == w - 1)


	print("2 >> ", surface_count)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")