import numpy as np
from copy import deepcopy

def read_input(input):
	numbers = [int(i) for i in input.split(",")]
	return numbers

def part_1(data, turns):
	numbers = read_input(data)

	state = {}

	for i,n in enumerate(numbers):
		state[n] = i

	n_next = 0
	n_last = 6
	
	for i in range(len(numbers), turns):
		last_n_pos = state.get(n_next, None)

		if (i+1 == turns):
			print(i + 1, " > ", n_last, last_n_pos, n_next)
	
		n_last = n_next
		
		state[n_next] = i

		if last_n_pos is None:
			n_next = 0
		else:
			n_next = i - last_n_pos




	print(">> ", 0)


def part_2(data):
	data = read_input(data)

	print(">> ", 0)


if __name__ == '__main__':
	#part_1("3,2,1", 2020)
	#part_1("0,1,5,10,3,12,19", 2020)
	
	# part 2
	part_1("0,1,5,10,3,12,19", 30000000)
	
	#part_2("data_test")
	#part_2("data")