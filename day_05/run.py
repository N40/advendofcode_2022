import numpy as np
from copy import deepcopy
import re

def read_input_lines(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	return lines


def read_input(filename):
	lines = read_input_lines(filename)
	n_crates = (len(lines[0]) + 1 ) // 4

	crates = [[] for i in range(n_crates)]
	for line in lines:
		if line.startswith(" 1 "):
			break

		for i in range(n_crates):
			c = line[1 + 4 * i]
			if c != " ":
				crates[i].append(c)

	crates = [c[::-1] for c in crates]

	moves = []

	for line in lines:
		m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
		if m is None:
			continue
		cnt, frm, to = m.groups()
		cnt = int(cnt)
		frm = int(frm) - 1
		to = int(to) - 1
		moves.append((cnt, frm, to))

	return crates, moves

def print_crates(crates):
	m = 0
	for crate in crates:
		m = max(m, len(crate))

	for j in range(m-1, -1, -1):
		for i in  range(len(crates)):
			if j < len(crates[i]):
				print(f"[{crates[i][j]}] ", end = "")
			else:
				print("    ", end = "")
		print("")

	for i in range(len(crates)):
		print(f"{i+1:2}  ", end = "")
	print("")
	print(np.sum([len(c) for c in crates]))
	print("")


def operate(crates, move, rev):
	cnt, frm, to = move

	#assert(len(crates[frm]) >= cnt)
	# WTF, why is this bug a feature??
	cnt = min(cnt, len(crates[frm]))

	payload = deepcopy(crates[frm][-cnt:])
	if rev:
		crates[to] += payload[::-1]
	else:
		crates[to] += payload
	crates[frm] = deepcopy(crates[frm][:-cnt])

	return crates

def run(filename, rev):
	crates, moves = read_input(filename)

	for move in moves:
		crates = operate(crates, move, rev)

	s = ""
	for crate in crates:
		if len(crate):
			s += crate[-1]
		else:
			s += " "

	return s


def part_1(filename):
	s = run(filename, True)
	print("1 >> ", s)

def part_2(filename):
	s = run(filename, False)
	print("2 >> ", s)

if __name__ == '__main__':
	part_1("data_test")
	part_1("data")
	part_2("data_test")
	part_2("data")