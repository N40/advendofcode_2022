import numpy as np
from copy import deepcopy as dc
import re

def read_input(filename):
	with open(filename) as f:
		lines = f.readlines()
	lines = [l.replace("\n","").strip() for l in lines]


	data = []
	pp = dict()
	for line in lines:
		if line == "":
			data.append(dc(pp))
			pp = dict()
			continue

		for field in line.split(" "):
			key = field.split(":")[0]
			pp[key] = field.split(":")[1]

	for s in data:
		print(s)

	return data

def validate(key, value):
	if key == "byr":
		if re.match("[0-9]{4}", value) is None: return False
		value = int(value)
		return value <= 2002 and value >= 1920

	elif key == "iyr":
		if re.match("[0-9]{4}", value) is None: return False
		value = int(value)
		return value <= 2020 and value >= 2010

	elif key == "eyr":
		if re.match("[0-9]{4}", value) is None: return False
		value = int(value)
		return value <= 2030 and value >= 2020

	elif key == "hgt":
		if len(value) < 4:
			return False

		unit = value[-2:]
		value = int(value[:-2])
		if unit == "cm":
			return 150 <= value and value <= 193
		elif unit == "in":
			return 59 <= value and value <= 76
		else:
			return False

	elif key == "hcl":
		return (re.match("#[0-9a-f]{6}", value) is not None) and len(value) == 7

	elif key == "ecl":
		return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

	elif key == "pid":
		return (re.match("[0-9]{9}", value) is not None) and len(value) == 9

	elif key == "cid":
		return True

	print("INVALID KEY: ", key)
	return False

def part_1(filename):
	data = read_input(filename)

	required = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid",
		])

	num_good = 0
	for d in data:
		s = set(d.keys())
		num_good += (len(required.difference(s)) == 0)
		print(">>    ", required.difference(s))
	print(">> ", num_good)


def part_2(filename):
	data = read_input(filename)

	required = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid",
		])

	num_good = 0

	for d in data:
		s = set(d.keys())
		valid = (len(required.difference(s)) == 0)

		for key in d:
			#print(key, d[key], validate(key, d[key]))
			valid = valid and validate(key, d[key])

		num_good += valid

	print(">> ", num_good)


if __name__ == '__main__':
	#part_1("data_test")
	#part_1("data")
	part_2("data_test_invalid")
	part_2("data_test_valid")
	part_2("data")