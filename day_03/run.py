import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	
	return lines


def part_1(filename):
	lines = read_input(filename)
	prio = 0

	data = []
	for line in lines:
		if len(lines) > 0:
			n = len(line) // 2
			assert(len(line) == 2 * n)
			data.append((line[:n], line[n:]))

	for left, right in data:
		common = set(left).intersection(set(right)).pop()
		if common.islower():
			val = int(common, 36) - 9
		else:
			val = int(common, 36) - 9 + 26
		prio += val

	print(">> ", prio)


def part_2(filename):
	lines = read_input(filename)
	prio = 0

	assert(len(lines) % 3 == 0)

	for i in range(0, len(lines), 3):
		a = set(lines[i])
		b = set(lines[i+1])
		c = set(lines[i+2])

		common = c.intersection(a.intersection(b)).pop()

		if common.islower():
			val = int(common, 36) - 9
		else:
			val = int(common, 36) - 9 + 26
		prio += val

	print(">> ", prio)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")