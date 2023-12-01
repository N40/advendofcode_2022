import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
	lines = [l.replace("\n","").split(": ") for l in lines]
	data = {key: val for key, val in lines}
	for key, val in data.items():
		if not " " in val:
			val = int(val)
		data[key] = val

	return data


def eval_data(data, key_of_interest):
	c = 0
	while not type(data[key_of_interest]) == int:
		for key, val in data.items():
			if type(val) == int:
				continue

			l, r = (val[:4], val[7:])
			if type(data[l]) == int and type(data[r]) == int:
				val = val.replace(l, str(data[l])).replace(r, str(data[r]))
				val = int(eval(val))
				data[key] = val

		c += 1
		if c > len(data) + 10:
			break

	return data

def part_1(filename):
	data = read_input(filename)
	
	data = eval_data(data, "root")

	print(">> ", data["root"])


inv_op = {
	"+": "-",
	"-": "+",
	"*": "/",
	"/": "*",
}

def part_2(filename):
	data = read_input(filename)

	data["root"] = data["root"].replace("+", "=")

	target = "humn"
	changed = []

	while target != "root":
		for key, val in data.items():
			if key in changed:
				continue

			if str(val).startswith(target):
				left = target
				right = val[7:]
				other = right
				break
			if str(val).endswith(target):
				right = target
				left = val[:4]
				other = left
				break
		op = val[5]

		if op == "=":
			data["null"] = 0
			t_val = other + " + null"
		elif op in "+*" or left == target:
			t_val = key + " " + inv_op[op] + " " + other
		else: # e.g. key = left / target or key = left - target
			t_val = left + " " + op + " " + key

		print(key, val, " -> ", target, t_val)
		print("")

		#swap
		data[target] = t_val
		changed.append(target)
		data.pop(key)

		target = key

	data = eval_data(data, "humn")

	print(">> ", data["humn"])


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")