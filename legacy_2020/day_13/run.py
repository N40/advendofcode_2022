import numpy as np
from copy import deepcopy

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]
	
	r_dep = int(lines[0])
	ids = lines[1].split(",")
	pos = [k for k, i in enumerate(ids) if i != "x"]
	ids = [int(i) for i in ids if i != "x"]

	return r_dep, ids, pos

def part_1(filename):
	r_dep, ids, _ = read_input(filename)

	print(ids)
	print(r_dep)

	best_id = None
	best_dep = 0

	for i in ids:
		dep = int(np.ceil(r_dep / i) * i)
		if (dep < best_dep) or (best_id is None):
			best_dep = dep
			best_id = i

	diff = best_dep - r_dep

	print(">>> ", best_id, best_dep, diff)

	print(">> ", best_id * diff)


def part_2_old(filename):
	r_dep, ids, pos = read_input(filename)

	print(ids)
	print(r_dep)
	print(pos)

	m_id = max(ids)
	k = ids.index(m_id)
	m_d = pos[k]


	for _probe in range(1000000000):
		t = m_id * _probe - m_d
		valid = True
		for d, i in zip(pos, ids):
			if (t + d) % i != 0:
				valid = False
				break

		if not valid:
			continue
		else:
			print(">>> ", t)
			break


	print(">> ", 0)

def compute_lcm(x, y):
   greater = max(x, y)
   fac = max(x, y)

   while(True):
       if (greater % x == 0) and (greater % y == 0):
           return greater
       greater += fac

   return lcm

def compute_padding(i_a, o_a, i_b, o_b, t_0 = 0):
	i_s = min(i_a, i_b)

	for m in range(10000):
		t = t_0 + i_s * m
		if ((t + o_a) % i_a == 0) and ((t + o_b) % i_b == 0):
			return t, (t + o_a) // i_a, (t + o_b) // i_b

	raise ValueError(f"Cannot find common padding for {i_a} and {i_b}")

def find_min(step, add, i_new, o_new):
	for m in range(10000):
		t = step * m + add
		if (t + o_new) % i_new == 0:
			return t

	raise ValueError(f"Cannot find common min for lcm {left_lcm}, i_new {i_new} and o_new {o_new}")


def part_2(filename):
	_, ids, pos = read_input(filename)
	print(ids)

	lcm = ids[0]
	t_0 = pos[0]

	for i, o in list(zip(ids, pos))[1:]:
		t_0 = find_min(lcm, t_0, i, o)
		lcm = compute_lcm(lcm, i)
		print(t_0, lcm)

	print(">> ", t_0)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test")
	part_2("data")