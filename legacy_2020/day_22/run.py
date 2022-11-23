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

	current = []

	for line in lines[1:]:
		if line == "":
			deck_1 = deepcopy(current)
			current = []
			continue
		if line.startswith("Player"):
			continue

		current.append(int(line))

	deck_2 = deepcopy(current)

	return deck_1, deck_2


def combat(deck_1, deck_2):
	top_1 = deck_1[0]
	top_2 = deck_2[0]
	deck_1 = deepcopy(deck_1[1:])
	deck_2 = deepcopy(deck_2[1:])

	if top_1 > top_2:
		deck_1 += [top_1, top_2]
	else:
		deck_2 += [top_2, top_1]
	
	return deck_1, deck_2


def part_1(filename):
	deck_1, deck_2 = read_input(filename)

	while len(deck_1) > 0 and len(deck_2) > 0:
		deck_1, deck_2 = combat(deck_1, deck_2)

		print(deck_1)
		print(deck_2)
		print("")

	c = 0
	for f, n in enumerate((deck_1 + deck_2)[::-1]):
		c += (f+1) * n

	print(">> ", c)

game = 1


def combat_rec(deck_1, deck_2):
	global game
	this_game = game
	game += 1

	states_1 = []
	states_2 = []

	for i in range(1, 100000):
		if False:
			print("")
			print("game ", this_game, "  round ", i)
			print(deck_1)
			print(deck_2)

		if len(deck_1 + deck_2) == 0:
			raise Exception("WTF")

		elif len(deck_1) == 0:
			return "Player 2", deck_1, deck_2
		elif len(deck_2) == 0:
			return "Player 1", deck_1, deck_2
		
		top_1 = deck_1[0]
		top_2 = deck_2[0]
		
		if str(deck_1) in states_1 or str(deck_2) in states_2:
			#print(stringify(deck_1, deck_2))
			return "Player 1", deck_1, deck_2
		
		elif len(deck_1) > top_1 and len(deck_2) > top_2:
			winner, _1, _2 = combat_rec(deepcopy(deck_1[1:top_1+1]), deepcopy(deck_2[1:top_2+1]))
		
		elif top_1 > top_2:
			winner = "Player 1"
		elif top_2 > top_1:
			winner = "Player 2"


		states_1.append(str(deck_1))
		states_2.append(str(deck_2))

		deck_1 = deepcopy(deck_1[1:])
		deck_2 = deepcopy(deck_2[1:])
		if winner == "Player 1":
			deck_1 += [top_1, top_2]
		else:
			deck_2 += [top_2, top_1]

	raise Exception("Should not reach this")



def part_2(filename):
	deck_1, deck_2 = read_input(filename)

	winner, deck_1, deck_2 = combat_rec(deck_1, deck_2)

	print(deck_1)
	print(deck_2)
	print("")

	c = 0
	for f, n in enumerate((deck_1 + deck_2)[::-1]):
		c += (f+1) * n

	print(">> ", c)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	part_2("data_test")
	part_2("data")