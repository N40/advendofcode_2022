import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		l = f.readline()
	return l


def part(filename, m):
	line = read_input(filename)

	for k in range(m, len(line)):
		if len(set(line[k-m:k])) == m:
			print(m, ">> ", k)
			return



if __name__ == '__main__':
	part("data_test", 4)
	part("data", 4)
	part("data_test", 14)
	part("data", 14)	