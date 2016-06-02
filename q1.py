
#Dawa Lama
#109463980
#CSE 337
#Python 2.7
#Mac OSX
#Assignment 1



inputFile = raw_input("Enter the name of the input file: ")

o1 = inputFile.split('.')
o1 = o1[0]
outputFile = '%s_output.html' % o1[0] 

inFile = open(inputFile)
outFile = open(outputFile, 'w')


for line in inFile.readlines():
	cleaned_line = line.replace("<span><span>", "").replace("</span></span>", "")
	outFile.write(cleaned_line)
	print cleaned_line

inFile.close()
outFile.close()

	
