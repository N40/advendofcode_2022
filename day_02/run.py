import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
	data = [(l[0], l[2] )for l in lines]
	return data



def part_1(filename):
	data = read_input(filename)
	score = 0

	for s_a, s_b in data:
		k_a = int(s_a, 36) - int("A", 36)
		k_b = int(s_b, 36) - int("X", 36)
		diff = (k_b - k_a) % 3
		score += (diff + 1) % 3 * 3
		score += k_b + 1


	print("1 >> ", score)


def part_2(filename):
	data = read_input(filename)
	score = 0

	for s_a, s_b in data:
		k_a = int(s_a, 36) - int("A", 36)
		ins = int(s_b, 36) - int("X", 36)
		score += 3 * ins
		diff = (ins + 2) % 3
		k_b = (k_a + diff) % 3
		score += k_b + 1

	print("2 >> ", score)

if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")