import numpy as np
from copy import deepcopy
import re


def read_input(raw):
	numbers = list(raw)
	numbers = [int(c) for c in numbers]
	return numbers


def print_state(numbers, current):
	for i, n in enumerate(numbers):
		if i == current:
			print(f"({n})", end = "")
		else:
			print(f" {n} ", end = "")

	print("")


def proceed_1(numbers, current):
	m = len(numbers)	

	#print_state(numbers, current)

	pick_ids = [(current + x) % m for x in [1, 2, 3]]
	#print([numbers[i] for i in pick_ids])
	#print((m + numbers[current] - 1 - 1) % m + 1)

	n_current = numbers[current]

	for k in range(1, m):
		n_target_probe = (m + numbers[current] - k - 1) % m + 1
		k_target = numbers.index(n_target_probe)
		if k_target not in pick_ids:
			break

	#print(numbers[k_target])

	current_0 = current

	new_numbers = []
	for i in range(m):
		if i in pick_ids:
			continue
		elif i == k_target:
			new_numbers.append(numbers[i])

			for j in pick_ids:
				new_numbers.append(numbers[j])
		else:
			new_numbers.append(numbers[i])

	numbers = deepcopy(new_numbers)

	current_1 = numbers.index(n_current)

	shift = current_0 - current_1
	numbers = [numbers[(i - shift)%m] for i in range(m)]
	return numbers


def part_1(raw):
	numbers = read_input(raw)
	m = len(numbers)


	for l in range(100):
		current = l % m

		numbers = proceed_1(numbers, current)


	i_start = numbers.index(1)
	numbers = numbers[i_start+1:] + numbers[:i_start]


	print(">> ", "".join(str(n) for n in numbers))


def build_linked_lists(numbers):
	l = len(numbers)
	next_number = [-1 for i in range(l)]
	prev_number = [-1 for i in range(l)]
	curr_number = [-1 for i in range(l)]

	for i, n in enumerate(numbers):
		n_p = numbers[(i-1)%l]
		n_n = numbers[(i+1)%l]
		next_number[n-1] = n_n - 1
		prev_number[n-1] = n_p - 1
		curr_number[n-1] = i

	#print(curr_number)
	#print(next_number)
	#print(prev_number)

	return next_number


def print_2(next_number, c, ticks = None):
	if ticks is None:
		ticks = len(next_number)


	print(f"({c+1}) ", end = "")
	c = next_number[c]

	for i in range(ticks):
		print(f" {c+1}  ", end = "")
		c = next_number[c]
	
	print("")


def proceed_nn(next_number, c):
	n_1 = next_number[c]
	n_2 = next_number[n_1]
	n_3 = next_number[n_2]
	
	# zip gap
	next_number[c] = next_number[n_3] # old end of block

	p = c
	while p in [c, n_1, n_2, n_3]:
		p = (p - 1)%len(next_number)

	next_number[n_3] = next_number[p] # insert
	next_number[p] = n_1

	return next_number


def part_2(raw):
	numbers = read_input(raw)
	for n in range(10, 10**6+1):
		numbers.append(n)
	m = len(numbers)

	x_turns = 10**7

	nn = build_linked_lists(numbers)
	c = numbers[0] - 1

	print("    .    |" * 10)

	for l in range(x_turns):
		if l % (x_turns / 100) == 0:
			print("#", end = "")

		#print_2(nn, c)
		nn = proceed_nn(nn, c)
		c = nn[c]

	while c != 0:
		c = nn[c]

	print("")

	print_2(nn, c, 5)

	x_1 = nn[c]
	x_2 = nn[nn[c]]
	print(">> ", float(x_1) * float(x_2))


if __name__ == '__main__':
	#part_1("389125467")
	#part_1("418976235")
	#part_2("389125467")
	part_2("418976235")