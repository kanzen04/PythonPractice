#QUESTION 3

import copy

# Part iii of Question 3

a = [1,2]
b = [a,3]
c = b[:]

print 'This is the values of c', c

d = copy.deepcopy(c)

a[0] = 7
b[1]=8

print '\nThis is the answer for part iii'
print '\nThis is the values of d (deep copied from c): ', d

print 'Changing the value of c[0][1] to 5. And also c[0][0]=7 is assigned. Does this change the value in d as well or not is what we want to see. If value changes, deep copy wasn\'t successful but if value does not change, then deep copy was successful'
c[0][1]=5
print 'Here is the value of c: ', c
print 'Here is the value of d again: ', d
print 'Since d hasn\'t changed, deep copy was successful'

# Part iv of Question 3


c[0][1] = [4,6]

e = copy.deepcopy(c)

print '\nThis is the answer for part iv'
print '\nThis is the output of c (which is a three-level): ', c
print 'This is the output of e (which is a copy of c): ', e

print 'We will change the value of c[0][1][1]=9. Does this change the value in e. If value changes, deep copy not successful otherwise successful'
c[0][1][1]=9
print 'Here is the value of c which has been altered: ',c 
print 'Here is the value of d now: ', e
print 'Since e hasn\'t changed, deep copy was successful'
