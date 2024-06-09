# # Basic python practice

# # 1. Create a string: organism = “Homo sapiens”. Write code that will store the genus and
# # species name as separate variables. Also accomplish this in one line.

# >>> organism = "Homo sapiens"
# >>> organism.split(" ")
# ['Homo', 'sapiens']
# >>> genus,species = organism.split(" ")
# >>> genus
# 'Homo'
# >>> species
# 'sapiens'


# # 2. The user of your script specifies a number of files that they would like to process, which
# # is stored as an integer object called file_num. Create a string that indicates how many
# # files the user would like to process like: “You would like to process 8 files”


# >>> user_files = "You would like to process " +  str(file_num)+ " files"



# # 3. Store your first name as a variable and your second name as a variable. Create a new
# # variable from these called full_name that contains your first and last name separated by
# # a space. Do this in two ways:
# # a. Using the string + operator

# >>> fname = 'Sarth'
# >>> lname = 'Diskalkar'
# >>> full_name = fname + " " + lname
# >>> full_name
# 'Sarth Diskalkar'

# # b. Using the join method of the list class

# >>> fnamelnamelist = ['Sarth', 'Diskalkar'] 
# >>> full_name = " ".join(fnamelnamelist)
# >>> full_name
# 'Sarth Diskalkar'

# 4. Create a variable:
# DNA = “ACgttGTcgtTTgaCCGacACCGGTTAACCGGTACGGTAACAAGGTTTAGGTA”
# Create a list that contains the number of each nucleotide stored as an element.
# a. Do this however you can manage it using multiple lines if necessary

DNA = DNA.upper()
counts = ["A: " + str(DNA.count('A')), "C: " + str(DNA.count("C")), "G: " + str(DNA.count("G")), "T: " + str(DNA.count("T"))]
>>> counts = ["A: " + str(DNA.count('A')), "C: " + str(DNA.count("C")), "G: " + str(DNA.count("G")), "T: " + str(DNA.count("T"))]
>>> counts
['A: 13', 'C: 11', 'G: 15', 'T: 14']
>>> len(counts)
4
>>> len(DNA)
53
>>> 24 + 29
53

# b. Do this in a single line using a list comprehension

>>> DNA
'ACgttGTcgtTTgaCCGacACCGGTTAACCGGTACGGTAACAAGGTTTAGGTA'
>>> [DNA.upper().count(x) for x in ['A','C','G','T']]
[13, 11, 15, 14]




# 5. Create a variable called phrase = 'If you want to read "Watership Down", I would
# recommend it.'. Create a list that contains each word of the phrase as an element,
# removing all punctuation.

>>> phrase
'If you want to read "Watership Down", I would recommend it.'
>>> phrase = phrase.replace(",","")
>>> phrase
'If you want to read "Watership Down" I would recommend it.'
>>> phrase = phrase.replace("\"","")
>>> phrase
'If you want to read Watership Down I would recommend it.'
>>> phrase
'If you want to read Watership Down I would recommend it.'
>>> x= phrase.split()
>>> x
['If', 'you', 'want', 'to', 'read', 'Watership', 'Down', 'I', 'would', 'recommend', 'it.']


# 6. Create a string called second_phrase = “Its about rabbits.”. Add each word from this
# string to the previous list. Do it using:
>>> second_phrase = "Its about rabbits."
# a. The + operator of list
>>> x = x + second_phrase.split()
>>> x
['If', 'you', 'want', 'to', 'read', 'Watership', 'Down', 'I', 'would', 'recommend', 'it.', 'Its', 'about', 'rabbits.']

# b. The append method of list (append() takes in one element)
Had to change my list here :
>>> x
['I', 'Love', 'Anushka']
var = second_phrase.split()
>>> x.append(var[0])
>>> x.append(var[1])
>>> x.append(var[2])
>>> x
['I', 'Love', 'Anushka', 'Its', 'about', 'rabbits.']

# c. The extend method of list (extend() takes in an iterable or list and adds it to the end of list)
>>> y = ['Beanu','Baby', 2]
>>> y.extend(second_phrase.split())
>>> y
['Beanu', 'Baby', 2, 'Its', 'about', 'rabbits.']

# 7. How many elements does this list contain? Using both a built in function and a magic
# method of list to answer this.

>>> count = len(y)
>>> count
6
>>> y.__len__()
6


# 8. Using this list, print the phrase “Watership Down” by using the slicing operator to access
# the elements you need.
>>> x = phrase.split()
>>> x
['If', 'you', 'want', 'to', 'read', 'Watership', 'Down', 'I', 'would', 'recommend', 'it.']
>>> y.extend(x[5:7])
>>> y
['Beanu', 'Baby', 2, 'Its', 'about', 'rabbits.', 'Watership', 'Down']


# 9. You are asked to write a script that converts a csv file into an excel file. You are given
# the name of the file which is stored as a string called filename (e.g. filename =
# “MyFile.csv”.
# a. Determine if the file ends with the appropriate filetype (i.e. .csv)
>>> filename = 'MyFile.csv'
>>> filename
'MyFile.csv'
>>> filename.endswith("csv")
True
# b. Create a new name where the .csv is replaced with .xls
>>> filename.replace('.csv','.xls')
'MyFile.xls'		
# 10. Count the number of stop codons that are in a DNA sequence stored as a variable called
# DNA. Do this:
# a. However you want
>>> DNA = 'GCCATTTATCGGAGCGCCTCCGTACACGGTATGATCGGACGCCTCGTGAG'
>>> stop_codons = ['TAA', 'TGA', 'TAG']
>>> total = 0
>>> total += DNA.count(stop_codons[1])
>>> total += DNA.count(stop_codons[0])
>>> total += DNA.count(stop_codons[2])
>>> total
2

# b. Using a list comprehension and the sum built in method
>>> DNA
'GCCATTTATCGGAGCGCCTCCGTACACGGTATGATCGGACGCCTCGTGAG'
>>> [DNA.count(i) for i in stop_codons]
[0, 2, 0]
>>> sum([DNA.count(i) for i in stop_codons])
2

# 11. What is the difference between __add__ and __iadd__ of the list class?
1)'+=' calls in-place add i.e iadd method. This method takes two parameters, but makes the change in-place, modifying the contents of the first parameter (i.e x is modified). Since both x and y point to same Pyobject they both are same.

2)Whereas x = x + [4] calls the add mehtod(x.add([4])) and instead of changing or adding values in-place it creates a new list to which a points to now and y still pointing to the old_list.