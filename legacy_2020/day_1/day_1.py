import numpy as np

def read_input(filename):
	with open(filename) as f:
		l = f.readlines()

	l = [_.replace("\n","") for _ in l]
	l = [int(_) for _ in l]
	return l

def part_1(filename):
	numbers = read_input(filename)

	target = 2020
	for n in numbers:
		for m in numbers:
			if n + m == target:
				print(">> ", n*m)
				return

def part_2(filename):
	numbers = read_input(filename)

	target = 2020
	for n in numbers:
		for m in numbers:
			for k in numbers:
				if n + m + k == target:
					print(">> ", n*m*k)
					return


if __name__ == '__main__':
	#part_1("data")
	part_2("data")