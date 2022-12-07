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


def sum_dict(d, total_sum):
	if type(d) == int:
		val = d
	elif type(d) == dict:
		val = 0
		for _, sd in d.items():
			sval, total_sum = sum_dict(sd, total_sum)
			val += sval

		if val <= 100000:
			total_sum += val

	return val, total_sum




def part_1(filename):
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
					path_steps = path_steps[:-2]
				else:
					print(path_steps)
			else:
				#current.setdefault(arg, {})
				try:
					current[arg]
					path_steps.append(current)
					current = current[arg]
				except:
					pass

		elif cmd == "ls":
			for t, n in arg:
				if t == "dir":
					current[n] = {}
				else:
					current[n] = int(t)


	print(json.dumps(tree, indent=2))

	v, total_sum = sum_dict(tree, 0)

	print(">> ", total_sum)


def part_2(filename):
	data = read_input(filename)

	print(">> ", 0)


if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	#part_2("data_test")
	#part_2("data")