import numpy as np
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	
	data = {}
	for line in lines:
		head, content = line.split(" bags contain ")
		data[head] = re.findall(r"(\d+) (\w+ \w+)", content)
		
	print(data)

	return data

def find_parents(data, color):
	result = []
	for parent, children in data.items():
		colors = [c for n,c in children]
		if color in colors:
			result.append(parent)
			result += find_parents(data, parent)
	print(result)
	return result

def count_children(data, root):
	result = 1

	for count, color in data[root]:
		print(root, " -> ", count, color)
		result += int(count) * count_children(data, color)

	return result

def part_1(filename):
	data = read_input(filename)

	r = set(find_parents(data, "shiny gold"))
	r = len(r)

	print(">> ", r)


def part_2(filename):
	data = read_input(filename)

	r = count_children(data, "shiny gold") - 1

	print(">> ", r)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test_2")
	part_2("data")