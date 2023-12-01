import numpy as np
from copy import deepcopy
import re

def read_input(filename):
	with open(filename) as f:
		raw = f.read()
		
	monkeys = []

	m = re.findall(
		r"Monkey (\d+):\n.+: (.+)\n.+new = (.+)\n.+by (\d+)\n.+monkey (\d+)\n.+monkey (\d+)",
		raw)

	monkeys = []
	actions = []
	state = []
	for match in m:
		i, items, op, mod, i_true, i_false = match
		monkeys.append((
			op,
			int(mod),
			int(i_true), int(i_false)
			))
		actions.append(0)
		state.append([int(k) for k in items.split(",")])

		assert(int(i) != i_false)
		assert(int(i) != i_true)

	return monkeys, actions, state

def print_monkeys(data):
	monkeys, actions, state = data
	for i, (act, items) in enumerate(zip(actions, state)):

		print(f"monkey {i}:  {act:4}  ; {(items)}" )


def print_monkeys_2(data):
	monkeys, actions, state = data
	for i, (act, items) in enumerate(zip(actions, state)):

		print(f"monkey {i}:  {act:4}  ; {len(items)}" )

def toss_round(data, reduction):
	monkeys, actions, state = data

	for i, (monkey, items) in enumerate(zip(monkeys, state)):

		op, mod, i_true, i_false = monkey
		for item in items:
			actions[i] += 1
			val = eval(op.replace("old", str(item)))
			
			val = reduction(val)

			if val % mod == 0:
				state[i_true].append(val)
			else:
				state[i_false].append(val)

		state[i] = []

	return monkeys, actions, state

def part_1(filename):
	data = read_input(filename)

	print_monkeys(data)

	for k in range(1,21):
		data = toss_round(data, lambda x: x // 3)

		print("\nRound", k)
		print_monkeys(data)
	
	m, a, s = data
	a = sorted(a)

	print(">> ", a[-1] * a[-2])


def part_2(filename):
	data = read_input(filename)

	primes_used = [2, 3, 5, 7, 11, 13, 17, 19, 23]
	lcm = np.prod(primes_used)

	for k in range(1,10001):
		data = toss_round(data, lambda x: x % lcm)

		if k % 1000 == 0:
			print("\nRound", k)
			print_monkeys_2(data)
	
	m, a, s = data
	a = sorted(a)

	print(">> ", a[-1] * a[-2])


if __name__ == '__main__':
	#part_1("data_test")
	part_1("data")
	#part_2("data_test")
	part_2("data")