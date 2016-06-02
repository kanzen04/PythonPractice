#QUESTION 5

import sys

num_input = 4
data = []
while num_input:
	print ('Enter a name to sort')
	data.append(sys.stdin.readline().lower())
	num_input = num_input - 1

data.sort()
for n in range(4):
	sys.stdout.write(data[n])



