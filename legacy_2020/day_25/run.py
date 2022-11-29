import numpy as np
from copy import deepcopy
import re

divider = 20201227
subject = 7

def part_1(pub_key_1, pub_key_2):
	r = 1
	c = 0
	s = 1
	while r != pub_key_1:
		r = (r * subject) % divider
		c += 1

		s = (s * pub_key_2) % divider

	print(">> ", s)


if __name__ == '__main__':
	part_1(17807724, 5764801)
	part_1(11161639, 15628416)