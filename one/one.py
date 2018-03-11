import sys

def run(num):
  num_string = str(num)

  i = 0
  sum = 0
  for digit in num_string:
    if num_string[i] == num_string[i-(len(num_string)-1)]:
      sum += int(digit)
    i+= 1
  print ("%i" % sum)


if __name__ == '__main__':
  num = sys.argv[1]
  run(num)