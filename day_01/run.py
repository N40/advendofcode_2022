import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		content = f.read()
		content = content.replace("\n",",")
		content = content.strip(",")
		content = content.split(",,")
	data = [np.array(line.split(","), int) for line in content]
	
	count = [np.sum(cals) for cals in data]
	
	return count

def part_1(filename):
	count = read_input(filename)
	print(">> ", np.max(count))


def part_2(filename):
	count = read_input(filename)
	count = sorted(count, reverse=True)
	print(">> ", np.sum(count[:3]))


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")