import numpy as np

def read_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","").strip() for l in lines]
	return lines

def read_input_union(filename):
	lines = read_lines(filename)

	groups = []
	_group = set()
	for line in lines:
		if line == "":
			groups.append(_group)
			_group = set()
		else:
			for c in line:
				_group.add(c)

	groups.append(_group)

	return groups


def read_input_intersection(filename):
	lines = read_lines(filename)

	groups = []
	_group = None
	for line in lines:
		# add group to results and reset
		if line == "" and _group is not None:
			groups.append(_group)
			_group = None

		# initialize group
		elif _group is None:
			_group = set(list(line))

		# intersect with group
		else:
			_addition = set(list(line))
			_group = _group.intersection(_addition)

	if _group is not None:
		groups.append(_group)

	return groups

def part_1(filename):
	data = read_input_union(filename)

	num = 0
	for g in data:
		print(g, len(g))
		num += len(g)

	print(">> ", num)


def part_2(filename):
	data = read_input_intersection(filename)

	num = 0
	for g in data:
		print(g, len(g))
		num += len(g)

	print(">> ", num)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test")
	part_2("data")