import numpy as np
from copy import deepcopy
import re

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
	lines = [l.replace("\n","") for l in lines]
	lines = [l for l in lines if l != ""]

	return lines

dir_diffs = {
	"ne": (-1, -.5),
	"nw": (-1, +.5),
	"e":  ( 0, -1 ),
	"w":  ( 0, +1 ),
	"se": (+1, -.5),
	"sw": (+1, +.5),
}

def split_into_op(line):
	line = deepcopy(line)
	op = []
	while len(line) > 0:
		for d in dir_diffs.keys():
			if line.startswith(d):
				line = line[len(d):]
				op.append(d)
	return op

def read_input(filename):
	lines = read_input_lines(filename)

	data = []
	for line in lines:
		op = split_into_op(line)

		data.append(op)

	return data

def navigate_coord(op, start = (0, 0)):
	i, j = start
	for d in op:
		d_i, d_j = dir_diffs[d]
		i += d_i
		j += d_j
	return i, j

def process(ops, prev = {}):
	tiles = deepcopy(prev)
	for op in ops:
		pos = navigate_coord(op)
		tiles.setdefault(pos, False)
		tiles[pos] = not tiles[pos]
	return tiles

def part_1(filename):
	ops = read_input(filename)

	tiles = process(ops)

	c = 0
	c_r = 0
	for pos, val in tiles.items():
		c += int(val)
		c_r += int(val == False)

	print(">>>  ", c_r)
	print(">> ", c)
	print("")

def black_neighbors(tiles):
	counts = {}
	for pos, val in tiles.items():
		if not val:
			continue

		for d, diff in dir_diffs.items():
			npos = (pos[0] + diff[0], pos[1] + diff[1])
			counts.setdefault(npos, 0)
			counts[npos] += 1
	return counts

def evolve(tiles):
	neighbors = black_neighbors(tiles)
	new_tiles = {}

	positions = (set(neighbors.keys())).union(set(tiles.keys()))

	for pos in positions:
		ncount = neighbors.get(pos, 0)
		val = tiles.get(pos, False)
		
		if val and ncount in [0, 3, 4, 5, 6]:
			new_tiles[pos] = False
		elif not val and ncount == 2:
			new_tiles[pos] = True
		elif val:
			new_tiles[pos] = True

	return new_tiles


def part_2(filename):
	ops = read_input(filename)

	tiles = {}
	tiles = process(ops, tiles)

	for day in range(1, 101):
		tiles = evolve(tiles)
	
		c = 0
		for pos, val in tiles.items():
			c += int(val)

		print(day, ">>>  ", c)

	print(">> ", c)
	print("")


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")