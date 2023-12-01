import numpy as np
from copy import deepcopy
import re
import json

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines

def read_input(filename):
	lines = read_input_lines(filename)
	commands = []
	temp_payload = []
	temp_command = None
	for line in lines:
		if line.startswith("$ "):
			if temp_command is not None:
				commands.append((temp_command, temp_payload))
				temp_command = []
				temp_payload = None

			if line[2:4] == "cd":
				commands.append(tuple(line[2:].split(" ")))
			if line[2:4] == "ls":
				temp_command = "ls"
				temp_payload = []
		else:
			temp_payload.append(tuple(line.split(" ")))

	if temp_command is not None:
		commands.append((temp_command, temp_payload))
		temp_command = []
		temp_payload = None

	return commands

def sum_dict(d, total_sum, sum_list):
	if type(d) == int:
		val = d
	elif type(d) == dict:
		val = 0
		total_sum_dict = {}
		for n, sd in d.items():
			sval, total_sum, sum_list = sum_dict(sd, total_sum, sum_list)
			val += sval

		if val <= 100000:
			total_sum += val

		sum_list.append(val)

	return val, total_sum, sum_list

def run(filename):
	data = read_input(filename)
	tree = {}
	current = tree
	path_steps = [tree]

	for cmd, arg in data:
		if cmd == "cd":
			if arg == "/":
				current = tree
				path_steps = [tree]
			elif arg == "..":
				if len(path_steps) > 0:
					current = path_steps[-1]
					path_steps = path_steps[:-1]
				else:
					print(path_steps)
			else:
				current.setdefault(arg, {})
				current[arg]
				path_steps.append(current)
				current = current[arg]

		elif cmd == "ls":
			for t, n in arg:
				if t == "dir":
					current[n] = {}
				else:
					current[n] = int(t)

	return sum_dict(tree, 0, [])

def part_1(filename):
	v, total_sum, sum_list = run(filename)

	print("1 >> ", total_sum)


def part_2(filename):
	v, total_sum, sum_list = run(filename)

	req = 30000000 - (70000000 - v)
	print("  r > ", req)
	print("2 >> ", min([k for k in sum_list if k >= req]))


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")