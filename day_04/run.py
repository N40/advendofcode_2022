import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	
	data = []
	for line in lines:
		a, b = line.split(",")
		a = a.split("-")
		b = b.split("-")
		a1, a2 = int(a[0]), int(a[1])
		data.append(([int(a[0]), int(a[1])], [int(b[0]), int(b[1])]))
	return data


def part_1(filename):
	data = read_input(filename)

	count = 0
	for a, b in data:
		b_in_a = a[0] <= b[0] and a[1] >= b[1]
		a_in_b = b[0] <= a[0] and b[1] >= a[1]
		count += int(b_in_a or a_in_b)

	print("1 >> ", count)


def part_2(filename):
	data = read_input(filename)

	count = 0
	for a, b in data:
		if a[0] > b[0]:
			a, b = b, a
		count += int(a[1] >= b[0])

	print("2 >> ", count)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")