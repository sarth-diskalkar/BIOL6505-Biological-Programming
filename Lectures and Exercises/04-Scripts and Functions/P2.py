""" Create a script that takes in an absolute path of a file from the user
(e.g -/Users/pmcgrath7/PythonClass/first_script.py). Create a function that prints out just the name of the file
(first_script.py) and the and the name of the directory it is found in (-/Users/pmcgrath7/PythonClass/ """

# write a function to query the user for a path, and return it as a string called "path"
def get_path():
    path = input("Enter absolute path: ")
    return path

# write a function to print out the filename of a given path
def print_filename(path):
    split_path = path.split("/") 
    filename = split_path[len(split_path)-1]
    print('filename: {}'.format(filename))

# write a function to print out the directory of a given path
def print_directory(path):
    split_path = path.split("/") 
    directory_pre = split_path[:len(split_path)-1]
    directory = "/".join(directory_pre) + '/'
    print('directory: {}'.format(directory))

# write a function combining the above three functions -- i.e., a function that queries the user for a path then
# prints out the filename and directory
def analyze_path():
    x = get_path()
    print_filename(x)
    print_directory(x)

# When we run a script from the command line (e.g., by calling "python P2.py") the entire script will execute in order.
# Any functions we wrote (as above) will be defined, but will not be executed unless we call the function outside of a
# function definition, as below. Once you have filled in the code above, try running this script from the command line.
analyze_path()