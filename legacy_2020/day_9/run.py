import numpy as np

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	data = [int(x) for x in lines]

	return data

def is_sum_of_two_in(n, backs):
	for x in backs:
		for y in backs:
			if x != y and n == x + y:
				return True

	return False

def part_1(filename, n_back):
	data = read_input(filename)

	for i, x in enumerate(data):
		if i < n_back: continue

		if not is_sum_of_two_in(x, data[i-n_back:i]):
			print(">> ", x)
			return i, x


def part_2(filename, n_back):
	data = read_input(filename)
	i, x = part_1(filename, n_back)

	for j in range(i):
		for l in range(j+1, i):
			ns = data[j:l]
			s = sum(ns)
			if s == x:
				ns = sorted(ns)
				print(f">> [{j},{l}]", ns, ns[0] + ns[-1])
			if s > x:
				continue


if __name__ == '__main__':
	part_1("data_test", 5)
	part_1("data", 25)
	part_2("data_test", 5)
	part_2("data", 25)