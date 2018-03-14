import numpy
import sys

def get_base(num):
	base = int(numpy.sqrt(num))

	if base % 2 == 0:
		return base - 1
	return base

def run(num):
	base = get_base(num)
	min_dist = base/2 + 1

	start = base**2 + min_dist
	print ((num - start) % min_dist + min_dist)

if __name__ == '__main__':
	number = sys.argv[1]
	run(int(number))
