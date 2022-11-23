import numpy as np
from copy import deepcopy
import re
from itertools import permutations, combinations_with_replacement

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines

def read_tile(lines):
	tile_id = int(lines[0].split(" ")[1].strip(":"))
	w = len(lines[1])
	matrix = [list(l.replace(".", "0").replace("#", "1")) for l in lines[1:1 + w]]
	matrix = np.array(matrix, int)
	return tile_id, matrix

def read_input(filename):
	lines = read_input_lines(filename)
	w = len(lines[1])
	print(f"tile: {w} x {w}")

	lines_per_tile = w + 2
	n_tiles = (len(lines) + 3) // lines_per_tile

	data = {}
	for i in range(n_tiles):
		tile_id, matrix = read_tile(lines[i * lines_per_tile:(i + 1) * lines_per_tile])
		data[tile_id] = matrix

	return data

def edges_from_matrix(matrix):
	w, h = matrix.shape
	edges = [
		# rotations
		list(matrix[0,:]),
		list(matrix[:,w-1]),
		list(matrix[h-1,::-1]),
		list(matrix[::-1,0]),

		# rotations + flipped
		list(matrix[0,::-1]),
		list(matrix[::-1,w-1]),
		list(matrix[h-1,:]),
		list(matrix[:,0]),
	]
	return edges

def matrix_variants(matrix):
	matrix_f = matrix[::-1,:]
	variants = [
		matrix,
		np.rot90(matrix, -1),
		np.rot90(matrix, -2),
		np.rot90(matrix, -3),
		matrix_f,
		np.rot90(matrix_f, -1),
		np.rot90(matrix_f, -2),
		np.rot90(matrix_f, -3),
	]
	return variants

def top(matrix):
	return list(matrix[0, :])
def right(matrix):
	return list(matrix[:, -1])
def bottom(matrix):
	return list(matrix[-1, :])
def left(matrix):
	return list(matrix[:, 0])

def print_layout(layout):
	w = len(layout)
	for i in range(w):
		for j in range(w):
			v = layout[i][j]
			if v is None:
				print(f"  -  ", end = " ")
			else:
				print(f"{v[0]:5}", end = " ")
		print("")
	print("")

def complete_layout(connections_left, connections_top, layout, used, i, j):
	w = len(layout)

	if np.sum(list(used.values())) == w * w:
		return layout

	n_tv_options = []
	if j > 0 and i == 0:
		n_tv_options = connections_left[layout[i][j-1]]
	elif i > 0 and j == 0:
		n_tv_options = connections_top[layout[i-1][j]]
	elif i > 0 and j > 0:
		n_tv_options = set(connections_top[layout[i-1][j]]).intersection(set(connections_left[layout[i][j-1]]))
	elif i == 0 and j == 0:
		n_tv_options = set(list(connections_top.keys()) + list(connections_left.keys()))

	if j < w-1:
		i_next = i
		j_next = j+1
	else:
		i_next = i+1
		j_next = 0

	for n_tv in n_tv_options:
		if used[n_tv[0]]:
			continue

		n_layout = deepcopy(layout)
		n_used = deepcopy(used)
		n_layout[i][j] = n_tv
		n_used[n_tv[0]] = True

		final_layout = complete_layout(connections_left, connections_top, n_layout, n_used, i_next, j_next)
		if final_layout is not None:
			return final_layout

	return None


def part_1(filename):
	data = read_input(filename)
	data_variants_raw = {tid: matrix_variants(data[tid]) for tid in data}
	
	tvs = [(tid, vid) for tid in data for vid in range(8)]
	data_variants = {(tid, vid): data_variants_raw[tid][vid] for (tid, vid) in tvs}

	c_w = int(np.sqrt(len(data)))
	print(f"canvas: {c_w} x {c_w}")
	ticks = 0

	# init helper struct
	connections_left = {tv: [] for tv in tvs}
	connections_top = {tv: [] for tv in tvs}
	valid_starts = set()

	for a in tvs:
		for b in tvs:

			if right(data_variants[a]) == left(data_variants[b]):
				#print(tid_a, tid_b, vid_a, vid_b, matches)
				connections_left[a].append(b)
				valid_starts.add(a)

			if bottom(data_variants[a]) == top(data_variants[b]):
				#print(tid_a, tid_b, vid_a, vid_b, matches)
				connections_top[a].append(b)
				valid_starts.add(a)


	# build solution
	layout = [[None for i in range(c_w)] for i in range(c_w)]
	used = {tid: False for tid in data}
	
	final = complete_layout(connections_left, connections_top, layout, used, 0, 0)


	c = 1

	if final is not None:
		print_layout(final)
		c *= final[0][0][0]
		c *= final[0][-1][0]
		c *= final[-1][0][0]
		c *= final[-1][-1][0]

	print(">> ", c)

	return final, data_variants

	
def get_sea_monster():
	lines = [
		"                  # ",
		"#    ##    ##    ###",
		" #  #  #  #  #  #   "]
	matrix = [list(l.replace(" ", "0").replace("#", "1")) for l in lines]
	matrix = np.array(matrix, int)
	return matrix


def part_2(filename):
	layout, data_variants = part_1(filename)

	c_w = len(layout)
	t_w = len(list(data_variants.items())[0][1]) - 2
	s_w = c_w * t_w


	total = np.zeros((s_w, s_w), int) * np.NaN
	total = np.array(total, int)
	for i in range(c_w):
		for j in range(c_w):
			total[i*t_w:(i+1)*t_w, j*t_w:(j+1)*t_w] = \
				data_variants[layout[i][j]][1:-1,1:-1]

	print(total)
	print("\n")

	monster = get_sea_monster()
	m_count = np.sum(monster)
	m_w = len(monster[0])
	m_h = len(monster)

	sea = None
	monster_envs = []
	for _sea in matrix_variants(total):
		count = 0
		_monster_envs = []
		for i in range(s_w-m_h+1):
			for j in range(s_w-m_w+1):
				env = _sea[i:i+m_h, j:j+m_w]
				if np.sum(env * monster) == m_count:
					count += 1
					_monster_envs.append(env)
		if count > 0:
			sea = _sea
			monster_envs = _monster_envs
			break

	print(sea.sum() - len(monster_envs) * m_count)


	print(">> ", 0)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test")
	part_2("data")