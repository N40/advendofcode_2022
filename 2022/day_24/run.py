import numpy as np
from copy import deepcopy
import re

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines

def read_input(filename):
	lines = read_input_lines(filename)
	lines = [list(l) for l in lines]
	print(f"h: {len(lines)}, w: {len(lines[0])}")
	mapping = {"#":1, '.':0, '>':2, 'v':3, '<':4, '^':5}
	m = np.array([[mapping[c] for c in l] for l in lines], int)
	S = (0, np.where(m[0] == 0)[0][0])
	E = (len(m)-1, np.where(m[-1] == 0)[0][0])
	return m, S, E


def move_it(filename, pos_ids):
	m, S, E = read_input(filename)
	border = deepcopy(m)
	border[1:-1,1:-1] *= 0
	h_i, w_i = m[2:,2:].shape

	# indices of blizzard directions Richt, Down, Left, Up
	b_r_i, b_r_j = blizz_r = np.where(m == 2)
	b_d_i, b_d_j = blizz_r = np.where(m == 3)
	b_l_i, b_l_j = blizz_r = np.where(m == 4)
	b_u_i, b_u_j = blizz_r = np.where(m == 5)

	# shame on me for using eval
	iternery = [[S, E][i] for i in pos_ids]

	# init 

	steps = 0

	for it_0, it_1 in zip(iternery[:-1], iternery[1:]):
		#reset progress
		progress = np.zeros_like(m, int)
		progress[it_0] = 1

		while progress[it_1] == 0:
			steps += 1
			# step each blizzard direction
			b_r_j = 1 + (b_r_j + 1 - 1) % w_i
			b_d_i = 1 + (b_d_i + 1 - 1) % h_i
			b_l_j = 1 + (b_l_j - 1 - 1) % w_i
			b_u_i = 1 + (b_u_i - 1 - 1) % h_i

			# write occupancy
			occ = deepcopy(border)
			occ[(b_r_i, b_r_j)] += 1
			occ[(b_d_i, b_d_j)] += 1
			occ[(b_l_i, b_l_j)] += 1
			occ[(b_u_i, b_u_j)] += 1

			# spread progress
			old_progress = deepcopy(progress)
			progress[:-1, :] += old_progress[+1:,:] # up
			progress[+1:, :] += old_progress[:-1,:] # down
			progress[:, :-1] += old_progress[:,+1:] # left
			progress[:, +1:] += old_progress[:,:-1] # right
			progress = progress.astype(bool).astype(int)

			# filter progress
			progress *= (occ == 0).astype(int)

		print(steps)
		#print(progress)


	print(pos_ids, ">> ", steps)


def part_1(filename):
	move_it(filename, [0, 1])

def part_2(filename):
	move_it(filename, [0, 1, 0, 1])


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")