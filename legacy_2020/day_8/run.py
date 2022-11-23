import numpy as np
from copy import deepcopy

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	
	data = []
	for line in lines:
		if line == "":
			break

		cmd, num = line.split(" ")
		data.append((cmd, int(num)))


	return data

def run(data):
	vst = [0 for d in data]

	acc = 0
	i = 0
	while vst[i%len(data)] == 0 and i < len(vst) and i >= 0:
		vst[i] += 1
		cmd, num = data[i]
		if cmd == "nop":
			i += 1
		elif cmd == "acc":
			acc += num
			i += 1
		elif cmd == "jmp":
			i += num
		else:
			raise Exception("Illegal cmd:", cmd)

	if i == len(vst):
		return True, acc
	else:
		return False, acc

	return termin

def part_1(filename):
	data = read_input(filename)
	
	_, acc = run(data)

	print(">> ", acc)


def part_2(filename):
	data = read_input(filename)

	for p in range(len(data)):
		if data[p][0] != "jmp":
			continue

		data_modded = deepcopy(data)
		data_modded[p] = "nop", 0
		terminates, acc = run(data_modded)
		print(p, terminates, acc)

		if terminates:
			print(">> ", p, acc)
			return


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test")
	part_2("data")