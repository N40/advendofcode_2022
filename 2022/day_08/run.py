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
	print(f"h: {len(lines)}, w: {len(lines[0])}")
	matrix = np.array(lines, int)
	return matrix

def read_input(filename):
	return read_input_matrix(filename)


def part_1(filename):
	matrix = read_input(filename)
	h, w = matrix.shape

	visible = np.zeros_like(matrix) + 1

	for i in range(1, h-1):
		for j in range(1, w-1):
			t_hide = np.max(matrix[:i, j]) >= matrix[i,j]
			b_hide = np.max(matrix[i+1:, j]) >= matrix[i,j]
			l_hide = np.max(matrix[i, :j]) >= matrix[i,j]
			r_hide = np.max(matrix[i, j+1:]) >= matrix[i,j]
			visible[i,j] = int(not (t_hide and b_hide and l_hide and r_hide))

	print("1 >>", visible.sum())



def part_2(filename):
	matrix = read_input(filename)
	h, w = matrix.shape

	visible = np.zeros_like(matrix) + 1
	score = np.zeros_like(matrix)

	dirs = [(-1,0),(1,0),(0,-1),(0,1)]

	for i in range(1, h-1):
		for j in range(1, w-1):
			scid = [1,1,1,1]
			for i_d, d in enumerate(dirs):
				d_i, d_j = d
				i_1, j_1 = i + d_i, j + d_j
				c = 0
				prev = 0
				while (i_1 >= 0 and j_1 >= 0 and i_1 < h and j_1 < w):
					c += 1
					if matrix[i_1, j_1] >= matrix[i, j]:
						break
					prev = matrix[i_1, j_1]
					i_1, j_1 = i_1 + d_i, j_1 + d_j

				scid[i_d] = c
			score[i,j] = np.array(scid).prod()
			print(scid)

	print(score)
	print("2 >>", score.max())


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")