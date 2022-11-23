import numpy as np


def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	data = [int(x) for x in lines]

	return data


def part_1(filename):
	data = read_input(filename)
	ns = np.array([0] + sorted(data))
	diffs = ns[1:] - ns[:-1]
	c1 = np.sum(diffs == 1)
	c3 = np.sum(diffs == 3) + 1

	print(">> ", c1, c3, c1 *c3)


def part_2(filename):
	data = read_input(filename)
	ns = np.array([0] + sorted(data))
	rng = np.arange(ns[-1] + 4)
	parents = [list() for x in range(len(rng))]
	#parents[1] = [0]
	path_count = [0 for p in parents]
	path_count[0] = 1

	for n in ns:
		parents[n+1] += [n]
		parents[n+2] += [n]
		parents[n+3] += [n]

	for n in rng[1:]:
		for p in parents[n]:
			path_count[n] += path_count[p]


	for n, c, p in zip(rng, path_count, parents):
		if n in ns:
			print(f"{n:3}, {c:3},  {p}")

	print(">> ", 0)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test")
	part_2("data")