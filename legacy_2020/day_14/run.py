import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]

	return lines

def mask_from_line(line):
	mask = line[7:]
	assert(len(mask) == 36)
	return mask

def mem_from_line(line):
	m = re.findall(r"mem\[(\d+)\] = (\d+)", line)
	return int(m[0][0]), int(m[0][1])

def apply_bit_with_mask(bit, mask):
	assert(len(bit) == len(mask))
	r = ""
	for b, m in zip(bit, mask):
		if m != "X":
			r += m
		else:
			r += b
	return r

def apply_value_with_mask(value, mask):
	bit = "{0:036b}".format(value)
	bit = apply_bit_with_mask(bit, mask)
	return int(bit, 2)

def part_1(filename):
	lines = read_input(filename)
	mem = {}
	mask = ""

	for line in lines:
		if line[:4] == "mem[":
			addr, val = mem_from_line(line)
			mem[addr] = apply_value_with_mask(val, mask)
		elif line[:4] == "mask":
			mask = mask_from_line(line)
		else:
			raise Exception("Invalid Line: ", line)


	print(">> ", np.sum(list(mem.values())))

def calc_addrs(addr, mask):
	addr_bit = "{0:036b}".format(addr)
	addr_masks = [""]
	for a, m in zip(addr_bit, mask):
		next_gen = []
		for am in addr_masks:
			if m == "0":
				next_gen.append(am + a)
			elif m == "1":
				next_gen.append(am + "1")
			else: # floating X
				next_gen.append(am + "0")
				next_gen.append(am + "1")
		addr_masks = deepcopy(next_gen)

	addrs = [int(am, 2) for am in addr_masks]
	return addrs

def part_2(filename):
	lines = read_input(filename)
	mem = {}
	mask = ""

	for line in lines:
		if line[:4] == "mem[":
			a0, val = re.findall(r"mem\[(\d+)\] = (\d+)", line)[0]
			addr = calc_addrs(int(a0), mask)
			for a in addr:
				mem[a] = int(val)
		elif line[:4] == "mask":
			mask = mask_from_line(line)
		else:
			raise Exception("Invalid Line: ", line)


	print(">> ", np.sum(list(mem.values())))



if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test_2")
	part_2("data")