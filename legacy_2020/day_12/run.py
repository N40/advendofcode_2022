import numpy as np
from copy import deepcopy

# x = est
# y = south

dir_key = {
	"N": (0, -1),
	"E": (1, 0),
	"S": (0, 1),
	"W": (-1, 0),
}

dir_cycle = list("ESWN")

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	
	data = [(l[0], int(l[1:])) for l in lines]

	return data

def step_1(state, cmd):
	key, val = cmd
	d, x, y = deepcopy(state)

	if key == "R":
		n = val // 90
		d = dir_cycle[(dir_cycle.index(d) + n) % 4]
	elif key == "L":
		n = val // 90
		d = dir_cycle[(dir_cycle.index(d) - n) % 4]
	elif key in "NSEWF":
		if key == "F":
			d_used = d
		else:
			d_used = key
		dx, dy = dir_key[d_used]
		x += dx * val
		y += dy * val
	else:
		raise Exception("Wrong command", key)

	return (d, x, y)


def step_2(state, cmd):
	key, val = cmd
	wx, wy, x, y = deepcopy(state)

	if key in "LR":
		n = (val // 90)
		if key == "L":
			n = -n
		n = n % 4

		if n == 0:
			pass
		elif n == 1:
			wx, wy = [-wy, wx]
		elif n == 2:
			wx, wy = [-wx, -wy]
		elif n == 3:
			wx, wy = [wy, -wx]

	elif key == "F":
		x += wx * val
		y += wy * val
		
	elif key in "NSEW":
		dx, dy = dir_key[key]
		wx += dx * val
		wy += dy * val
	else:
		raise Exception("Wrong command", key)

	return (wx, wy, x, y)


def part_1(filename):
	data = read_input(filename)

	state = ("E", 0, 0)

	for d in data:
		state = step_1(state, d)
		print(">>>>  ", state)

	print(">> ", abs(state[1]) + abs(state[2]))


def part_2(filename):
	data = read_input(filename)

	state = (10, -1, 0, 0)

	for d in data:
		state = step_2(state, d)
		print(">>>>  ", state)

	print(">> ", abs(state[2]) + abs(state[3]))



if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test")
	part_2("data")