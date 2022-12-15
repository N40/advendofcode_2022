import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	data = []
	with open(filename) as f:
		lines = f.readlines()
	for line in lines:
		m = re.search(r"x=(\S+)\, y=(\S+): .+x=(\S+)\, y=(\S+)", line)
		data.append([*m.groups()])
	return np.array(data, int)

def part_1(filename, y):
	data = read_input(filename)

	pos = set()
	beacons = set()
	for d in data:
		d_SB = sum(abs(d[2:] - d[:2]))
		d_x_max = d_SB - abs(d[1] - y)

		# is beacon
		if d[3] == y:
			beacons.add(tuple(d[2:]))

		for x in range(d[0] - d_x_max, d[0] + d_x_max + 1):
			pos.add((x, y))

	print("1 >> ", len(pos) - len(beacons))


def part_2(filename, d_max):
	data = read_input(filename)
	beacon_dists = [sum(abs(d[2:] - d[:2])) for d in data]

	valid = False
	for dist, d in zip(beacon_dists, data):
		border = dist + 1

		if valid:
			break
		for _x in range(max(-border, -d[0]), min(+border+1, d_max-d[0])):
			for _y in [border - abs(_x), - border + abs(_x)]:
				x = _x + d[0]
				y = _y + d[1]
				if x < 0 or x > d_max or y < 0 or y > d_max:
					continue

				valid = True
				for dist2, d2 in zip(beacon_dists, data):
					if abs(x - d2[0]) + abs(y - d2[1]) < dist2:
						valid = False
						break

				if valid:
					r =(x,y)
					break

	print(r)
	x, y = r
	print("2 >> ", x * 4000000 + y)


if __name__ == '__main__':
	part_1("data_test", 10)
	part_1("data", 2000000)
	part_2("data_test", 20)
	part_2("data", 4000000)