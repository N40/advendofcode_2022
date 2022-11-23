import numpy as np

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]

	data = []
	for l in lines:
		count, char, pw = l.split(" ")
		char = char[0]
		cl, cu = count.split("-")
		cl = int(cl)
		cu = int(cu)
		data.append((cl, cu, char, pw))
	return data

def part_1(filename):
	data = read_input(filename)

	n_good = 0

	for cl, cu, char, pw in data:
		count = list(pw).count(char)
		n_good += (cl <= count and count <= cu)

	print(">> ", n_good)

def part_2(filename):
	data = read_input(filename)

	n_good = 0

	for cl, cu, char, pw in data:
		chars = list(pw)
		a = chars[cl-1] == char
		b = chars[cu-1] == char 
		n_good += (a + b == 1)

	print(">> ", n_good)

if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")