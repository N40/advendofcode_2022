import numpy as np
from copy import deepcopy
import re

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines

def read_input_matrix(filename):
	lines = read_input_lines
	lines = [list(l) for l in lines]
	print(f"h: {len(lines)}, w: {len(lines[0])}")
	return lines

def read_input(filename):
	return read_input_lines(filename)


def part_1(filename):
	data = read_input(filename)

	print(">> ", 0)


def part_2(filename):
	data = read_input(filename)

	print(">> ", 0)


if __name__ == '__main__':
	part_1("data_test")
	#part_1("data")
	#part_2("data_test")
	#part_2("data")