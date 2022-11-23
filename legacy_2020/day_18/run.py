import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	
	return lines

def calc_1(line):
	# resolve braces
	while True:
		m = re.search(r"\(([^\(\)]+)\)", line)
		if m is not None:
			value = calc_1(m.groups()[0])
			line = line.replace(m.group(), str(value))
		else:
			break

	c = int(line.split(" ")[0])

	vals = [int(v) for v in line.split(" ")[2::2]]
	ops = line.split(" ")[1::2]

	for o, v in zip(ops, vals):
		if o == "*":
			c *= v
		elif o == "+":
			c += v

	return c

def part_1(filename):
	data = read_input(filename)

	r = 0
	for line in data:
		r_l = calc_1(line)
		print(line, "=", r_l)
		r += r_l

	print(">> ", r)




def calc_2(line):
	# resolve braces
	while True:
		m = re.search(r"\(([^\(\)]+)\)", line)
		if m is not None:
			value = calc_2(m.groups()[0])
			line = line.replace(m.group(), str(value))
		else:
			break

	# resolve plus
	while True:
		m = re.search(r"(\d+ \+ \d+)", line)
		if m is not None and m.groups()[0] != line:
			value = calc_2(m.groups()[0])
			line = line.replace(m.group(), str(value))
		else:
			break


	c = int(line.split(" ")[0])

	vals = [int(v) for v in line.split(" ")[2::2]]
	ops = line.split(" ")[1::2]

	for o, v in zip(ops, vals):
		if o == "*":
			c *= v
		elif o == "+":
			c += v

	return c

def part_2(filename):
	data = read_input(filename)

	r = 0
	for line in data:
		r_l = calc_2(line)
		print(line, "=", r_l)
		r += r_l

	print(">> ", r)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	part_2("data_test")
	part_2("data")