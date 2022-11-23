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
	data = []
	for line in lines:
		m = re.search(r"(.+) \(contains (.+)\)", line)
		data.append((m.groups()[0].split(" "), m.groups()[1].split(", ")))

	ingredient_list = []
	allergene_list = []
	for _ings, _algs in data:
		ingredient_list += _ings
		allergene_list += _algs
	ingredient_list = sorted(list(set(ingredient_list)))
	allergene_list = sorted(list(set(allergene_list)))

	return data, ingredient_list, allergene_list


def print_state(m_i_a, ingredient_list, allergene_list):
	for k_a, a in enumerate(allergene_list):
		print(f"{'':10}  ", "  |"* k_a, a)

	for i, l in zip(ingredient_list, list(m_i_a)):
		print(f"{i:10}  [", " ".join([f"{x:2}" for x in l]), "]")

	print("")

def part_1(filename):
	data, ingredient_list, allergene_list = read_input(filename)

	ingredients = {ing: None for ing in ingredient_list}

	ingredient_count = {ing: 0 for ing in ingredient_list}
	allergene_count = {alg: 0 for alg in allergene_list}
	for _ings, _algs in data:
		for ing in _ings:
			ingredient_count[ing] += 1
		for alg in _algs:
			allergene_count[alg] += 1


	n_ings = len(ingredient_list)
	n_algs = len(allergene_list)

	m_i_a = np.zeros((n_ings, n_algs), int)
	m_a = np.array([allergene_count[alg] for alg in allergene_list])

	for ings, algs in data:
		for i in ings:
			for a in algs:
				k_i = ingredient_list.index(i)
				k_a = allergene_list.index(a)
				m_i_a[k_i][k_a] += 1

	print_state(m_i_a, ingredient_list, allergene_list)

	print(f"{'total':10}  [", " ".join([f"{x:2}" for x in m_a]), "]")
	print("\n")


	for n in range(n_algs):

		for k_a, a in enumerate(allergene_list):
			comp = m_i_a[:, k_a] >= m_a[k_a]
			if np.sum(comp) == 1:
				k_i = list(comp).index(1)
				i = ingredient_list[k_i]
				print(a, i)
				ingredients[i] = a
				m_i_a[k_i,:] = 0
				break

		print_state(m_i_a, ingredient_list, allergene_list)


	c = 0
	danglist = []
	for ing in ingredients:
		print(f"{ing:15} ", ingredients[ing], "  ", ingredient_count[ing])
		if ingredients[ing] is None:
			c += ingredient_count[ing]
	
	allergenes = {a: i for i, a in ingredients.items() if a is not None}
	danglist = [allergenes[k_a] for k_a in allergene_list]


	print(" ")
	print(">> ", c)
	print(">> ", ",".join(danglist))


if __name__ == '__main__':
	#part_1("data_test")
	part_1("data")
	#part_2("data_test")
	#part_2("data")