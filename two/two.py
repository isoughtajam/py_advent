import numpy
import sys

def run(filename):
	checksum = 0
  	with open(filename) as f:
		for line in f:
			parsed = line.replace("\n", "")
			line_list = parsed.split("\t")
			num_list = map(int, line_list)
			cs = max(num_list) - min(num_list)
			checksum += cs
	print (checksum)

if __name__ == '__main__':
	filename = sys.argv[1]
	run(filename)