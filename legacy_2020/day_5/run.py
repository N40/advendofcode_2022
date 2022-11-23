import numpy as np

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines

def as_number_FB_7(code):
	code_binary = code.replace("B", "1").replace("F", "0")
	return int(code_binary, 2)

def as_number_LR_3(code):
	code_binary = code.replace("R", "1").replace("L", "0")
	return int(code_binary, 2)

def get_id(line):
	row = as_number_FB_7(line[:7])
	col = as_number_LR_3(line[7:])
	r = row*8 + col
	return r

def part_1(filename):
	data = read_input(filename)

	m = 0

	for line in data:
		r = get_id(line)
		m = max(m, r)

	print("1> ", m)


def part_2(filename):
	data = read_input(filename)

	ids = [get_id(line) for line in data]

	for i_prev in ids:
		if i_prev+2 in ids and i_prev+1 not in ids:

			print("2> ", i_prev+1)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	#part_2("data_test")
	part_2("data")