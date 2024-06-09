"""One of the most important uses of functions is to simplify our code by collecting frequently-repeated tasks into
simple functions. Any time you find yourself copying and pasting large sections of similar code throughout a script,
you could likely simplify the task using a function. Take a look at the following block of code:"""

# home_dir = '~/User/'
# data_dir = 'data1/'
# file = 'file1.txt'
# path = home_dir + data_dir + file
# print(path)

# home_dir = '~/User/'
# data_dir = 'data1/'
# file = 'file2.txt'
# path = home_dir + data_dir + file
# print(path)

# home_dir = '~/User/'
# data_dir = 'data1/'
# file = 'file3.txt'
# path = home_dir + data_dir + file
# print(path)

# home_dir = '~/User/'
# data_dir = 'data2/'
# file = 'file1.txt'
# path = home_dir + data_dir + file
# print(path)

# home_dir = '~/User/'
# data_dir = 'data2/'
# file = 'file2.txt'
# path = home_dir + data_dir + file
# print(path)

# home_dir = '~/User/'
# data_dir = 'data2/'
# file = 'file3.txt'
# path = home_dir + data_dir + file
# print(path)

"""now try to simplify this code block using one or more functions to achieve the same results in as few lines as 
you can"""
def CombinePath(home_dir, data_dir, file):
	path = home_dir + data_dir + file
	print(path)
CombinePath(home_dir = '~/User/',data_dir = 'data1/',file = 'file1.txt')
CombinePath(home_dir = '~/User/',data_dir = 'data2/',file = 'file3.txt')
