import numpy as np
from copy import deepcopy
import re

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines

def read_input_matrix(filename):
	lines = read_input_lines(filename)
	lines = [list(l) for l in lines]
	# print(f"h: {len(lines)}, w: {len(lines[0])}")

	chars = {".":0, "#":1}
	lines = [[chars[c] for c in l] for l in lines]
	m = np.array(lines, int)
	return m


def padd_matrix(m, border):
	h, w = m.shape
	m_new = np.zeros((h + 2 * border, w + 2 * border), int)
	m_new[border:border+h, border:border+w] += m
	return m_new

check_offsets = {
	0: np.array([[-1,-1], [-1, 0], [-1,+1]]), # N
	1: np.array([[+1,-1], [+1, 0], [+1,+1]]), # S
	2: np.array([[-1,-1], [ 0,-1], [+1,-1]]), # W
	3: np.array([[-1,+1], [ 0,+1], [+1,+1]]), # E
}

def print_m(m, pad):
	copy = m[pad:-pad, pad:-pad]
	for l in copy:
		for c in l:
			print(".#"[c], end = "")
		print("")
	print("")

def process(m, k_limit):
	m = padd_matrix(m, 2*len(m))

	print_m(m, 2*len(m) - 1)

	for k in range(k_limit):
		next_occ = np.zeros_like(m)
		elves = np.array(np.where(m)).T
		elves_next = []
		changes = 0

		for p_old in elves:
			p_first_free = None
			dof = 0
			for i_d in range(4):
				check_positions = p_old + check_offsets[(i_d + k)%4]
				p_try = check_positions[1]
				i, j = check_positions.T

				if np.sum(m[i, j]) == 0:
					dof += 1

					if p_first_free is None:
						p_first_free = p_try

			if dof in [0, 4]:
				p_next = p_old
			else:
				changes += 1
				p_next = p_first_free

			next_occ[tuple(p_next)] += 1
			elves_next.append(p_next)

		assert(len(elves_next) == len(elves))

		m *= 0
		for p_old, p_next in zip(elves, elves_next):
			if next_occ[tuple(p_next)] == 1:
				m[tuple(p_next)] = 1
			else:
				m[tuple(p_old)] = 1
	
		#print_m(m, 4)

		if changes == 0:
			break

	return m, k


def part_1(filename):
	m = read_input_matrix(filename)

	m, k = process(m, 10)

	h = max(np.where(m)[0]) - min(np.where(m)[0]) + 1
	w = max(np.where(m)[1]) - min(np.where(m)[1]) + 1
	print("    ", w, "*", h, "-", np.sum(m))

	print("1 >> ", h * w - np.sum(m))


def part_2(filename):
	m = read_input_matrix(filename)

	m, k = process(m, 100000)

	print("2 >> ", k + 1)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")