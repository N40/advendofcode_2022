import numpy as np
from copy import deepcopy

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
		lines = [l.replace("\n","") for l in lines]

	rules = {}
	for i, line in enumerate(lines):
		if line == "":
			lines = lines[i+1:]
			break
		key, rule = line.split(": ")
		r1, r2 = rule.split(" or ")
		rules[key] = (
			[int(r1.split("-")[0]), int(r1.split("-")[1])],
			[int(r2.split("-")[0]), int(r2.split("-")[1])])


	your_ticket = None
	for i, line in enumerate(lines):
		if line == "":
			lines = lines[i+1:]
			break
		if line.startswith("your"):
			continue
		your_ticket = [int(k) for k in line.split(",")]


	nearby_tickets = []
	for i, line in enumerate(lines):
		if line.startswith("nearby"):
			continue
		nearby_tickets.append([int(k) for k in line.split(",")])
	
	return rules, your_ticket, nearby_tickets

def valid_by_rule(val, r1, r2):
	return (val >= r1[0] and val <= r1[1]) or (val >= r2[0] and val <= r2[1])

def part_1(filename):
	rules, your_ticket, nearby_tickets = read_input(filename)

	invalid_numbers = []
	for ticket in nearby_tickets:
		for n in ticket:
			valid = False
			for r in rules.values():
				valid = valid or valid_by_rule(n, *r)
			if not valid:
				invalid_numbers.append(n)

	print(invalid_numbers)

	print(">> ", np.sum(invalid_numbers))


def part_2(filename):
	rules, your_ticket, nearby_tickets = read_input(filename)

	invalid_numbers = []
	valid_tickets = []
	rules_order_possibilities = {}

	for ticket in nearby_tickets:
		valid = True
		for n in ticket:
			valid_number = False
			for r in rules.values():
				rule_applies = valid_by_rule(n, *r)
				if rule_applies:
					valid_number = True
			if not valid_number:
				valid = False
		if valid:
			valid_tickets.append(ticket)

	#print(valid_tickets)

	for r_name, rs in rules.items():
		rules_order_possibilities[r_name] = {}
		for i_n,n in enumerate(your_ticket):
			rules_order_possibilities[r_name][i_n] = []

		for i_t,ticket in enumerate(valid_tickets):
			for i_n,n in enumerate(ticket):
				rule_applies = valid_by_rule(n, *rs)
				if rule_applies:
					rules_order_possibilities[r_name][i_n].append(i_t)

		options = set()
		for i_n,n in enumerate(your_ticket):
			if len(rules_order_possibilities[r_name][i_n]) == len(valid_tickets):
				options.add(i_n)
		rules_order_possibilities[r_name] = options

	rules_final = {}

	#print(rules_order_possibilities)

	for _ in range(100):
		for r_name, options in rules_order_possibilities.items():
			if len(options) == 1:
				r_name_fix = r_name
				i_fix = list(options)[0]
				break

		for r_name in rules:
			if r_name != r_name_fix:
				rules_order_possibilities[r_name].discard(i_fix)

		rules_final[r_name_fix] = i_fix
		rules_order_possibilities[r_name_fix] = set()

	print(rules_final)

	v = 1
	for r_name in rules_final:
		if r_name.startswith("departure"):
			v *= your_ticket[rules_final[r_name]]

	print(">> ", v)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	#part_2("data_test_2")
	part_2("data")