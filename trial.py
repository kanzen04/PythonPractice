
from random import randrange

for n in range(3):
	print n
	r = randrange(0,3)
	print r
	if n==r: continue
	if n>r: break
	print "x"
else:
	print "Wow, you are lucky \n"

if n<2:
	print "Better luck next time \n"

