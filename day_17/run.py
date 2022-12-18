import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		line = f.readline().replace("\n", "")
	directions = [[-1, 1][int(c == ">")] for c in line]
	return directions

def create_blocks():
	A = np.ones((1, 4), int)
	
	B = np.zeros((3, 3), int)
	B[1,:] = 1
	B[:,1] = 1

	C = np.zeros((3, 3), int)
	C[0,:] = 1
	C[:,2] = 1
	
	D = np.ones((4, 1), int)

	E = np.ones((2, 2), int)

	return [A, B, C, D, E]


def print_tower(tower, h):
	for i in range(h, -1, -1):
		line = "".join([".#"[n] for n in tower[i]])
		print("|{}|".format(line))
	print("+-------+")


def place_n_blocks(blocks, directions, n, tower, h, l):
	for k in range(n):
		block = blocks[k%len(blocks)]
		b_h, b_w = block.shape
		i = h + 3
		j = 2

		# move
		while True:
			# gas push
			d = directions[l]
			l = (l+1)%len(directions)
			valid_side_movement = True
			if j + d >= 0 and j + b_w + d <= 7:
				collision = (tower[i:i+b_h, j+d:j+d + b_w] * block).any()
				if not collision:
					j += d

			# ground check
			if i == 0:
				break

			# bottom collision
			collision = (tower[i-1:i-1+b_h, j:j+b_w] * block).any()
			if collision:
				break
			
			i -= 1

		# apply
		tower[i:i+b_h, j:j+b_w] += block
		h = max(h, i + b_h)

	return tower, h, l

def build_tower(blocks, directions, n):
	tower = np.zeros((n * 3, 7), int)
	
	h = 0
	l = 0

	return place_n_blocks(blocks, directions, n, tower, h, l)


def part_1(filename):
	directions = read_input(filename)
	blocks = create_blocks()

	tower, h, l = build_tower(blocks, directions, 2022)

	print("1 >> ", h)


def part_2(filename):
	directions = read_input(filename)
	blocks = create_blocks()

	# find cycles of combination of block cycle (n) and push direction cycle (l)
	occs = np.zeros(len(directions), int)
	n_lasts = np.zeros(len(directions), int) - 1
	h_lasts = np.zeros(len(directions), int) - 1

	tower = np.zeros((100000, 7), int)
	
	h = 0
	l = 0
	n = 0
	n_last = 0
	while h < 100000:
		n += 5

		tower, h, l = place_n_blocks(blocks, directions, 5, tower, h, l)
		#print(n, h, l)
		occs[l] += 1

		if occs[l] == 3:
			break
		if occs[l] == 2:
			n_lasts[l] = n
			h_lasts[l] = h


	# cycle found
	n_last = n_lasts[l]
	h_last = h_lasts[l]
	n_per_it = n - n_last
	h_per_it = h - h_last
	# print(n, n_last, l, h, h_last)

	# add height for as many cycles as possible
	n_left = 1000000000000 - n
	k_its = n_left // n_per_it
	h += k_its * h_per_it
	n_left -= k_its * n_per_it

	# build and add the rest starting from a zero height tower with shifted push direction (l)
	tower = np.zeros((10000, 7), int)
	tower, h_add, l = place_n_blocks(blocks, directions, n_left, tower, 0, l)

	h += h_add

	print("2 >> ", h)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")