# Basic python practice
# 1. If this is your first time encountering dictionaries, running the following lines of code (one at a time) and trying to understand 
# the results may help you get your footing before moving onto the remaining exercises. 
# If you are confident using dictionaries, you can skip to exercise 2. (If you are getting an ‘invalid character’ error after 
# copying and pasting, try typing the code into the console manually)
# a. my_dict = {‘common name’: ‘barn owl’, ‘genus’: ‘Tyto’, ‘species’: ‘alba’}
# b. my_dict
# c. dir(my_dict)
# d. my_dict.keys()
# e. my_dict.values()
# f. my_dict.items()
# g. my_dict[‘common name’]
# h. my_dict.update({‘max speed (km/h)’: 32})
# i. my_dict[‘max speed (km/h)’]
# j. my_dict[‘weight (kg)’] = 0.6
# k. my_dict[‘weight (kg)’]
# l. my_dict[‘weight (kg)’] += 0.01
# m. my_dict[‘weight (kg)’]
# n. for key, val in my_dict.items():
# 		print(‘{}: {}’.format(key, val))
# DONE


# 2. Create a function that calculates the number of A’s, C’s, G’s, and T’s in a DNA sequence.
# a. Do this by looping through the string while keeping track of the number of nucleotides using a dictionary, using each nucleotide as a key, 
# and the number of nucleotides as a value. Print out the number of each nucleotide in a pretty way. Identify the most common and least common nucleotide.

def dna_counter(seq: str) -> None:
	""" Args: 
		seq(string): a DNA sequence 

		Return: 
		(None): prints a string of the count of each nucleotide as well as the most common and least common nucleotide
	"""

	counter = {"A": 0, "G": 0, "C": 0, "T": 0}
	for base in seq.upper():
			counter[base] += 1
	print("Count of bases in the DNA sequence")
	for key,val in counter.items():
		print(f"Count of {key}: {val}") #f-string 
	minimum = [k for k,v in counter.items() if v == min(counter.values())][0]
	maximum = [k for k,v in counter.items() if v == max(counter.values())][0]
	print("The most common nucleotide is {1} and the least common nucelotide is {0}".format(minimum,maximum)) #.format()


# For the next two problems you might find this page useful:
# https://docs.python.org/3/library/collections.html

# b. For situations like this, a default dictionary is often more useful
# than normal dictionary. One of the issues with part a is that you have to initialize the value as 0. A default dictionary can automatically do that for you. 
# The defaultdict is a subclass of dictionary that is found in the collections module. Implement your code using the defaultdict.

from collections import defaultdict
def dna_counter_defaultdict(seq: str) -> None:
	counter = defaultdict(int)
	for base in seq.upper():
			counter[base] += 1
	print("Count of bases in the DNA sequence")
	for key,val in counter.items():
		print(f"Count of {key}: {val}") #f-string 
	minimum = [k for k,v in counter.items() if v == min(counter.values())][0]
	maximum = [k for k,v in counter.items() if v == max(counter.values())][0]
	print("The most common nucleotide is {1} and the least common nucelotide is {0}".format(minimum,maximum)) #.format()


# c. Finally use a Counter object from the collections module. Again print out the number of each nucleotide 
# in a pretty way and print out the most common and least common nucleotide.

from collections import Counter
def dna_counter_counter(seq: str) -> None:
	c = Counter(seq)
	print(c)
	print("The count for all the bases in the DNA sequence: ")
	for key,val in c.items():
		print("{}:{}".format(key,val))
	most_common_base,most_common_val = c.most_common(1)[0]
	least_common_base,least_common_val = c.most_common()[-1]
	print(f"The most common nucleotide is {most_common_base} and the least common nucelotide is {least_common_base}.")



# 3. Create a dictionary:
# student = {"firstname": "Tyler", "lastname": "Smith", "homework": [82.0, 0.0, 87.0, 75.0, 22.0], "quizzes": [93.0, 0.0, 75.0, 78.0], "tests": [100.0, 100.0]}
# Create a function that prints out the name of the student followed by the overall grade in the class. To calculate the overall grade, first throw out the 
# lowest quiz grade and the lowest homework grade. Then use the following weights to calculate an overall grade: 25% from homework, 25% from quizzes, and 50% from tests.

def get_grade(info: dict) -> None:
	""" Args:
		info(dict): a dictionary of the students first name, last name, homework grades, quiz grades, and test grades

		Return:
		None: Prints a string containing the students name and overall grade depending on throwing out the 
		lowest quiz grade and the lowest homework grade. To calculate the overall grade, consider the following: 
		25% from homework, 25% from quizzes, and 50% from tests
	"""

	# gather first and last name of student
	fname = info["firstname"]
	lname = info["lastname"]

	# drop lowest quiz grade
	quiz_grades = info["quizzes"]
	dropped_quiz_grade = min(quiz_grades)
	quiz_grades.remove(dropped_quiz_grade)
	#print(quiz_grades)

	# drop lowest homework grade
	homework_grades = info["homework"]
	dropped_homework_grade = min(homework_grades)
	homework_grades.remove(dropped_homework_grade)
	#print(homework_grades)

	# calculate overall grade (factor in weights)
	test_grades = info["tests"]
	overall_grade = (0.25 * (sum(homework_grades)/len(homework_grades))) + (0.25 * (sum(quiz_grades)/len(quiz_grades))) + (0.50 * (sum(test_grades)/len(test_grades)))
	print(f"Student Name: {fname} {lname}\nOverall Grade: {overall_grade}")


# 4. The os module is useful for file directory type operations. But as with anything involving file manipulation, be careful! You don’t want to accidentally delete something important. Reference the os module documentation if you get stuck (https://docs.python.org/3/library/os.html). Figure out how to use os to:

# a. Print the current directory you are in

import os
print(os.getcwd())

# b. Create a directory called TempDir

os.mkdir('TempDir')

# c. Delete a directory called TempDir

os.rmdir('TempDir')

# d. Print all of the files in your home directory

home_directory = os.path.expanduser("~")  
files_in_home_directory = os.listdir(home_directory)
for item in files_in_home_directory:
    item_path = os.path.join(home_directory, item)
    if os.path.isfile(item_path):  
        print(item)

# e. Print all of the directories in your home directory
print("\n\nspacer\n\n")

home_directory = os.path.expanduser("~")
with os.scandir(home_directory) as entries:
    for entry in entries:
        if entry.is_dir():  
            print(entry.name)


# f. Use an os function combined with a list comprehension to print
# out all of the files in your home directory that start with a ‘.’

home_directory = os.path.expanduser("~")
with os.scandir(home_directory) as entries:
    for entry in entries:
        if entry.is_dir():  
            print(entry.name)

# 5. You have a list of names of patients that are participating in a trial on whether ivermectin is effective at curing covid-19. You need to randomly 
# assign them to one of two groups, the treatment group (that gets ivermectin) and the control group (that gets a placebo). Reference the python documentation for the 
# random module (https://docs.python.org/3/library/random.html) if you get stuck. Do this in two ways:

# a. Use a method of the random module to randomize the order of the list and assign the first half to one group and the second half to another group

import random

def split_group(group: list) -> None:
	split_index = len(group)//2
	random.shuffle(group)
	treatment = group[0:split_index]
	control = group[split_index:]
	print(treatment)
	print(control)

# b. Use a method of the random module to return a 0 or 1 and use that for each person to assign them to one of two groups

def binary_split_group(group: list) -> None:
	# 0 is control, 1 is treatmeant
	treatment = []
	control = []
	new_list = []

	for i in range(0,len(group)):
		new_list.append(random.randint(0,1))

	# create control and treatment groups based on 0 or 1
	i = 0
	for num in new_list:
		if num == 0:
			control.append(group[i])
		if num == 1:
			treatment.append(group[i])
		i += 1

	print(f"Control Group: {control}")
	print(f"Treatment Group: {treatment}")






		



