#QUESTION 6

import sys
import pickle

input1 = sys.argv[1]
input2 = sys.argv[2]

a = open(input1)
b = open(input2)

#creating a dictionary of customers
oldCustomers = {}
newCustomers = {}

for line in a: 
	lastName, firstName, email, customerID, phoneNumber = line.split("\t" )
	customerID = customerID.replace('"','')
	oldCustomers[int(customerID)] = {'lastName':lastName, 'firstName':firstName,'email':email,'customer id':customerID, 'phoneNumber':phoneNumber}

for line in b:
	lastName, firstName, email, customerID, phoneNumber = line.split("\t" )
	customerID = customerID.replace('"','')
	newCustomers[int(customerID)] = {'lastName':lastName, 'firstName':firstName,'email':email,'customer id':customerID, 'phoneNumber':phoneNumber}

group_a = {}
group_b = {}
group_c = {}

for customerID in oldCustomers.keys() + newCustomers.keys():
     if customerID in oldCustomers and customerID in newCustomers:
	 customer = newCustomers[customerID]
         group_c[customerID] = customer
     elif customerID in newCustomers and customerID not in oldCustomers:
	customer = newCustomers[customerID]
	group_b[customerID] = customer
     elif customerID in oldCustomers and customerID not in newCustomers:
	customer = oldCustomers[customerID]
	group_a[customerID] = customer

print "GroupA", group_a
print "GropuB", group_b
print "GropuC", group_c



outputA = open('oldCustomers.txt','w')
outputB = open('newCustomers.txt','w')
outputC = open('currentCustomers.txt','w')


#writing output to file outputA, outputB and outputC using pickle 
pickle.dump(group_a, outputA)
pickle.dump(group_b, outputB)
pickle.dump(group_c, outputC)


#closing all the files opened to read and write
a.close()
b.close()
outputA.close()
outputB.close()
outputC.close()



