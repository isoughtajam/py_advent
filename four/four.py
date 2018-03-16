import sys

def run(filename):
	valid = 0
	total = 0
  	with open(filename) as f:
		for line in f:
			parsed = line.replace("\n", "")
			tokens = parsed.split(" ")
			if len(tokens) == len(set(tokens)):
				valid += 1
	print (valid)


if __name__ == '__main__':
	filename = sys.argv[1]
	run(filename)