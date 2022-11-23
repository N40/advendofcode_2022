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

		key, r_in = line.split(": ")

		r = None
		if "\"" in r_in:
			r = [r_in.replace("\"", "")]
		else:
			r = []
			for part in r_in.split(" | "):
				r.append([int(k) for k in part.split(" ")])

		rules[int(key)] = r

	return rules, lines

def build_strings(rules, number):

	result = []
	for part in rules[number]:
		sub_results = [""]
		for p in part:
			new_sub_reqults = []
			if type(p) == str:
				to_add = [p]
			else:
				to_add = build_strings(rules, p)


			for a in to_add:
				for s in sub_results:
					new_sub_reqults.append(s + a)

			sub_results = deepcopy(new_sub_reqults)

		result += sub_results

	rules[number] = result

	return result


def part_1(filename, try_kill_8_11 = False):
	rules, lines = read_input(filename)


	options = build_strings(rules, 0)
	options = rules[0]
	print("options: ", len(options))
	target_len = len(options[0])


	count_good = 0

	for line in lines:
		good = line in options

		if good:
			print(line, line in options)
			pass
		count_good += int(good)

	print(">> ", count_good)


def part_2(filename):
	rules, lines = read_input(filename)

	"""
	0: 8 11
	8: 42
	11: 42 31 | 42 11 31

	-> 
	0: 42 42 (42) (31) 31 

	"""

	_42_options = build_strings(rules, 42)
	_31_options = build_strings(rules, 31)
	print("options 42: ", len(_42_options))
	print("options 31: ", len(_31_options))


	count_good = 0

	for line in lines:
		line_backup = line
		good = False
		_42_head_count = 0
		_31_tail_count = 0
		_excess_count = 0

		# securly check end
		for _31 in _31_options:
			if line.endswith(_31):
				_31_tail_count += 1
				line = line[:-len(_31)]

		# trim front
		line_prev = "_"
		while line_prev != line:
			line_prev = line
			for _42 in _42_options:
				if line.startswith(_42):
					_42_head_count += 1
					line = line[len(_42):]

		# trim back
		line_prev = "_"
		while line_prev != line:
			line_prev = line
			for _31 in _31_options:
				if line.endswith(_31):
					_31_tail_count += 1
					line = line[:-len(_31)]

		_excess_count = len(line)

		good = True and \
			_excess_count == 0 and \
		    _31_tail_count >= 1 and \
		    _42_head_count >= 1 + _31_tail_count

		if good:
			print(line_backup, _42_head_count, _31_tail_count, _excess_count)
		count_good += int(good)

	print(">> ", count_good)



if __name__ == '__main__':
	part_1("data_test")
	#part_1("data")
	#part_2("data_test_2")
	part_2("data")