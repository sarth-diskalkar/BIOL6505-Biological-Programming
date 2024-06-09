f = open("/Users/sarthdiskalkar/Desktop/Fall2023Bioinformatics/BIOL 6505/Lectures:Exercises/Lecture9-ReadingWritingData-2/penguins.csv", "r")
print(type(f))
print(dir(f))
for line in f:
	print(line) # \n at the end of each line
	print(line.rstrip()) # \n taken off
	print(line.rstrip().split(",")) # \n taken off and each element of csv split at the comma and each element put into a list
	# a \n is seen at the end of each line
	print(type(line))
	#csv file is printed out as a str
import pysam



