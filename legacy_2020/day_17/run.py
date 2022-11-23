import numpy as np
from copy import deepcopy

def read_input(filename, padding = 0):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	lines = [list(l.replace("#", "1").replace(".", "0")) for l in lines]
	dy = len(lines)
	dx = len(lines[0])
	dz = 1
	dw = 1
	print(f"dy: {dy}, dx: {dx}")
	core = np.array([[lines]], int)
	data = np.zeros((dw + 2 * padding, dz + 2 * padding, dy + 2 * padding, dy + 2 * padding), int)
	print(data.shape)
	data[padding, padding, padding:padding+dy, padding:padding+dx] = core
	return data

def sum_neighbors_3(data, i_z, i_y, i_x):
	return data[
		max(0, i_z-1):i_z+2,
		max(0, i_y-1):i_y+2,
		max(0, i_x-1):i_x+2,
		].sum()

def step_3(state):
	new_state = deepcopy(state)

	d_z, d_y, d_x = state.shape

	for i_z in range(d_z):
		for i_y in range(d_y):
			for i_x in range(d_x):
				sn1 = sum_neighbors_3(state, i_z, i_y, i_x)
				act = state[i_z, i_y, i_x]
				sn1 -= act

				if act and sn1 in [2, 3]:
					new = 1
				elif act:
					new = 0
				elif sn1 == 3:
					new = 1
				else:
					new = 0

				new_state[i_z, i_y, i_x] = new

	return new_state


def sum_neighbors_4(data, i_w, i_z, i_y, i_x):
	return data[
		max(0, i_w-1):i_w+2,
		max(0, i_z-1):i_z+2,
		max(0, i_y-1):i_y+2,
		max(0, i_x-1):i_x+2,
		].sum()

def step_4(state):
	new_state = deepcopy(state)

	d_w, d_z, d_y, d_x = state.shape

	for i_w in range(d_w):
		for i_z in range(d_z):
			for i_y in range(d_y):
				for i_x in range(d_x):
					sn1 = sum_neighbors_4(state, i_w, i_z, i_y, i_x)
					act = state[i_w, i_z, i_y, i_x]
					sn1 -= act

					if act and sn1 in [2, 3]:
						new = 1
					elif act:
						new = 0
					elif sn1 == 3:
						new = 1
					else:
						new = 0

					new_state[i_w, i_z, i_y, i_x] = new

	return new_state

def part_1(filename):
	state = read_input(filename, 6)[6]
	
	for k in range(7):
		print(">>>  ", k, state.sum())
		state = step_3(state)

	print(">> ", 0)


def part_2(filename):
	state = read_input(filename, 6)
	
	for k in range(7):
		print(">>>  ", k, state.sum())
		state = step_4(state)

	print(">> ", 0)


if __name__ == '__main__':
	part_1("data_test")
	#part_1("data")
	part_2("data_test")
	part_2("data")