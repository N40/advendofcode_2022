import numpy as np
from copy import deepcopy
import re

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines

s2d_mapping = {"2":2, "1":1, "0":0, "-":-1, "=":-2 }
d2s_mapping = {v: k for k, v in s2d_mapping.items()}

def SNAFU_to_DEC(snafu):
	dec = 0
	for i, c in enumerate(snafu[::-1]):
		dec += s2d_mapping[c] * 5 ** i
	return dec

def DEC_to_SNAFU(dec):
	snafu = ""
	while dec > 0:
		f = (dec + 2) % 5 - 2
		snafu = d2s_mapping[f] + snafu
		dec -= f
		dec //= 5
	return snafu

def part_1(filename):
	lines = read_input_lines(filename)
	total = 0
	for snafu in lines:
		dec = SNAFU_to_DEC(snafu)
		snafu_rev = DEC_to_SNAFU(dec)
		print(f"{snafu:>10}", f"{dec:>10}", f"{snafu_rev:>10}")
		total += dec

	print("")
	print(">> sum dec  ", total)
	print(">> sum snafu", DEC_to_SNAFU(total))


def part_2(filename):
	data = read_input(filename)

	print(">> ", 0)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")