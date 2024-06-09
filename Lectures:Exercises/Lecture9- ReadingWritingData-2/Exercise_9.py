"""
Exercise 9: Reading and Writing Data part 2

This exercise will focus on reading and writing data to and from .txt and .csv files using both python builtins
(like open() and print()) and the pandas library. You will also continue to practice skills from previous lessons,
including string formatting, loops, and list comprehensions.
"""

import pandas as pd

"""
1. download the penguins.csv dataset from canvas. using the pandas read_csv method, read the csv into a 
DataFrame called df. Do not manually set the index_col (as we did in some of the lecture examples). The index
should default to a RangeIndex, where the index of each row is just its row number. Use "df.head()" to print the
first few rows of the dataframe and confirm that it parsed correctly. This dataset is taken from
https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv
"""

df = pd.read_csv("/Users/sarthdiskalkar/Desktop/Fall2023Bioinformatics/BIOL 6505/Lectures:Exercises/Lecture9-ReadingWritingData-2/penguins.csv")
print(df)
print(df.head())
print(len(df))

"""
2. Use the DataFrame method to_csv() to write the DataFrame from part 1 to a file called penguins_copy.csv. Use the 
keyword argument "index" to prevent the index from writing to the file. If you do this correctly, penguins_copy.csv
and penguins.csv should be identical.
"""

df.to_csv("/Users/sarthdiskalkar/Desktop/Fall2023Bioinformatics/BIOL 6505/Lectures:Exercises/Lecture9-ReadingWritingData-2/penguins_copy.csv", sep=",", index=False)

"""
3. Use the python builtin "open" to open penguins_copy.csv as f. Then, using a for loop, print each line of 
penguins_copy.csv. Finally, call "f.close()" to close the file object. 
"""

f = open('/Users/sarthdiskalkar/Desktop/Fall2023Bioinformatics/BIOL 6505/Lectures:Exercises/Lecture9-ReadingWritingData-2/penguins_copy.csv', 'r')
for line in f:
  print(line)
f.close()


"""
4. Now expand your code from part 3 to improve the formatting of each line before it is printed. Do the following:
    - Do not print the first line, which contains the column headings. Instead, split this string on the commas and 
      store it as a list called "col_names". You may find the enumerate() function useful for keeping track of how many 
      iterations of the loop you have completed.
    - For the remaining lines, strip the newline characters so that the lines do not get separated by a blank line
    - check that the line contains exactly 7, non-empty, comma-separated entries. Lines with less than 7 such entries 
      are incomplete observations. Do not print these lines.
    - make sure to call f.close() at the end and outside of your loop to release the file object
"""

f = open('/Users/sarthdiskalkar/Desktop/Fall2023Bioinformatics/BIOL 6505/Lectures:Exercises/Lecture9-ReadingWritingData-2/penguins_copy.csv', 'r')

# col_names = f.readline().rstrip().split(",")
for index,value in enumerate(f):
  if index == 0:
    col_names = value.rstrip().split(",")
  elif "" not in value.rstrip().split(",") and len(value.rstrip().split(',')) == 7:
    print(value.rstrip())
  else:
    continue

f.close()


"""
5. Now further expand your code from part 4 to make your printout a little prettier. Your goal is to have each line
print out in the following format: 

"species: Adelie, island: Torgersen, bill_length_mm: 39.1, bill_depth_mm: 18.7, flipper_length_mm: 181.0, body_mass_g: 3750.0, sex: MALE"

You should be able to accomplish this using list comprehension for each line. Recall that you already have the column
names stored as list called col_names. you may find the zip function helpful for iterating over two lists simultaneously 
as explained here:
https://www.kite.com/python/answers/how-to-iterate-over-two-lists-at-the-same-time-in-python
"""

f = open('/Users/sarthdiskalkar/Desktop/Fall2023Bioinformatics/BIOL 6505/Lectures:Exercises/Lecture9-ReadingWritingData-2/penguins_copy.csv', 'r')

for index,value in enumerate(f):
  if index > 0 and "" not in value.rstrip().split(",") and len(value.rstrip().split(',')) == 7:
    zipped_object = zip(col_names,value.rstrip().split(','))
    x = ["{}: {}".format(a,b) for a,b in zipped_object]
    string = ""
    for element in x:
      string += element + ", "
    print(string.rstrip(", "))
print('All done!')
f.close()

"""
6. Modify your code from part 5 such that, instead of printing each formatted line to the console, it writes
the formatted line to a file called pretty_penguins.txt.
"""

f = open('/Users/sarthdiskalkar/Desktop/Fall2023Bioinformatics/BIOL 6505/Lectures:Exercises/Lecture9-ReadingWritingData-2/penguins_copy.csv', 'r')

output_file = open('/Users/sarthdiskalkar/Desktop/Fall2023Bioinformatics/BIOL 6505/Lectures:Exercises/Lecture9-ReadingWritingData-2/pretty_penguins.txt', 'w') # writing to pretty_penguins.txt using object output_file

for index,value in enumerate(f):
  if index > 0 and "" not in value.rstrip().split(",") and len(value.rstrip().split(',')) == 7:
    zipped_object = zip(col_names,value.rstrip().split(','))
    x = ["{}: {}".format(a,b) for a,b in zipped_object]
    string = ""
    for element in x:
      string += element + ", "
    print(string.rstrip(", "), file=output_file)
print("All done!", file=output_file)

f.close()
output_file.close()

