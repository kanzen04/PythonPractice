#QUESTION 8 



# PART I  - DIFFERENCE BETWEEN TWO LIST

def diff(a,b):
	return [i for i in a if i not in b]

def common(a, b):
	return [i for i in a if i in b]
				

x = [1,2,3,4,5,6,7,8]
y = [2,3,4,9,10]

z = diff(x,y)




# PART II - UNION OF TWO SETS 
def union(a,b):
	only_in_a = diff(a, b)
	only_in_b = diff(b, a) 
	common_in_ab = common(a, b)
	return only_in_a + only_in_b + common_in_ab

result = union(x,y)


	


# PART III - SHOW EXAMPLES

print 'this is x ', x
print 'this is y ', y

print 'the difference sample of x-y: ',z
print 'the union sample x+y: ', result


a = [1, 2, 3]
b = [3, 4, 5]
assert [1, 2] == diff(a, b)
assert [4, 5] == diff(b, a)
assert [1, 2, 3, 4, 5] == sorted(union(a, b))

a = [1, 2, 3]
b = [2, 3, 4]
assert [1] == diff(a, b)
assert [4] == diff(b, a)
assert [1, 2, 3, 4] == sorted(union(a, b))
