import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines


def part_1(filename):
	data = read_input(filename)

	ss = []

	X = 1
	k = 1
	i = 0
	while k < 221:
		d = data[i % len(data)]
		#print(f"{k:3} {X:3}  {k*X:10}")
		if (k + 20)%40 == 0:
			ss.append(k*X)

		if d[0] == "n":
			k += 1
		else:
			k += 1
			#print(f"{k:3} {X:3}  {k*X:10}")
			if (k + 20)%40 == 0:
				ss.append(k*X)

			k += 1
			X += int(d.split(" ")[1])

		i += 1

	print("1 >> ", np.sum(ss))


def get_pixel(k, X):
	c = k % 40
	if c-X in [0, 1, 2]:
		return "#"
	else:
		return "."

def part_2(filename):
	data = read_input(filename)

	result = ["" for k in range(7)]

	X = 1
	k = 1
	i = 0
	while k < 241:
		d = data[i % len(data)]
		result[(k-1) // 40] += get_pixel(k, X)

		if d[0] == "n":
			k += 1
		else:
			k += 1
			result[(k-1) // 40] += get_pixel(k, X)

			k += 1
			X += int(d.split(" ")[1])

		i += 1

	for l in result:
		print(l)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")