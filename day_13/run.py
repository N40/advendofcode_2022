import numpy as np
from copy import deepcopy
import re
import functools

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines

def read_input(filename):
	lines = read_input_lines(filename)
	
	count = (len(lines) + 1) // 3
	data = []

	for i in range(count):
		data.append((eval(lines[3*i]), eval(lines[3*i + 1])))

	return data

def check(left, right, level):
	# print("  " * level + "-compare", left, right)

	# int v int
	if type(left) == int and type(right) == int:
		if left == right:
			return None
		else:
			return left < right

	# list v list
	if type(left) == int:
		left = [left]
	if type(right) == int:
		right = [right]

	n = min(len(left), len(right))

	for i in range(n):
		c = check(left[i], right[i], level + 1)
		if c is not None:
			return c

	if len(left) == len(right):
		return None
	else:
		return len(left) < len(right)

def check_top(left, right):
	c = check(left, right, 0)
	if c is None:
		c = True

	return c


def part_1(filename):
	data = read_input(filename)

	indices = []

	for i, (left, right) in enumerate(data):
		if check_top(left, right):
			indices.append(i + 1)

	print(indices)


	print("1 >> ", np.sum(indices))


def part_2(filename):
	data = read_input_lines(filename)
	data = [eval(l) for l in data if l != ""]
	
	a = [[2]]
	b = [[6]]

	count_a_right = 1
	count_b_right = 2
	for i, other in enumerate(data):
		if not check_top(a, other):
			count_a_right += 1
		if not check_top(b, other):
			count_b_right += 1

	print("2 >> ", count_a_right * count_b_right)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")