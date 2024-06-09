"""
Exercise 8: Argparse and Command Line Redirection

IMPORTANT: It is recommend that you complete the below tasks in this order: 1, 5, 2, 3, 4, 6, 7.

This script will help you practice passing input to scripts from the command line, and redirecting command line output
using the > and >> operators.
"""

import argparse

"""
1. Create and ArgumentParser object and store it as parser (i.e., replace "None" in the line below with your code)
"""

parser = argparse.ArgumentParser(description='This is a script for Exercise_8.py')

"""
2. Use the add_argument method to add a positional argument to the parser. Call this argument "fname". Enforce that 
the argument is type str. Set the help string to the following: "name of output file. File extension will be appended 
automatically". 
"""

parser.add_argument('fname', type=str, help='name of output file. File extension will be appended automatically')

"""
3. Use the add_argument method to add two flagged arguments to the parser. 

For the first argument, set the abbreviated flag to "-L", the full flag to "--linear_dimension", and the help string to
"side-length of the square domain". Enforce that this argument is of type int, and set its default value to 30.

For the second argument, set the abbreviated flag to "-N", the full flag to "--number_of_birds", and the help string to
"number of birds to simulate". Enforce that this argument is of type int, and set its default value to 1000.
"""

parser.add_argument('-L', '--linear_dimension', help='side-length of the square domain', type=int, default=30)
parser.add_argument('-N', '--number_of_birds', help='number of birds to simulate', type=int, default=1000)

"""
4. Use the add_argument method to add two flagged arguments to the parser.

For the first, don't use an abbreviated flag. Use the full flag '--eta'. Set the help string to "strength of noise". 
Enforce that the input is of type float. Set the default value to 0.25. 

For the second, use the abbreviated flag "-R" and the full flag "--radius". Set the help string to "radius of 
interaction". Enforce that the input is type float. Set the default value to 0.5.
"""

parser.add_argument('--eta', help='strength of noise', type=float, default=0.25)
parser.add_argument('-R', '--radius', help="radius of interaction", type=float, default=0.5)

"""
5. Use the parse_args method to parse your arguments and store them as args. In the line below, replace "None" with your
code.
"""

args = parser.parse_args()

"""
6. The loop below is what causes the args you've added to print to the console each time you run this script. Use the 
> operator to instead direct this output to a file called output.txt. You do not need to add any python code to this 
section; instead, complete this task on the command line. If you do this part correctly, output.txt should look
something like this:

fname: your_fname, <class 'str'>
linear_dimension: 30, <class 'int'>
number_of_birds: 1000, <class 'int'>
eta: 0.25, <class 'float'>
radius: 0.5, <class 'float'>
"""

if args is not None:
    for key, val in args.__dict__.items():
        print('{}: {}, {}'.format(key, val, type(val)))

"""
7. When you are confident that you have compeleted parts 1-7 above, uncomment the following lines of code and run your
script again. If you see an error indicating "ffmpeg is unavailable" or "unknown file extension: .mp4", or similar,
try installing ffmpeg using either pip or conda. The animation takes time to generate, but if your computer is
really struggling, try decreasing both the linear dimension and the number of birds. 
"""

from Exercise_8_utils import run_sim
run_sim(args.linear_dimension, args.number_of_birds, args.eta, args.radius, args.fname)

"""
8. Once you get the animation to work, try adjusting the command-line parameters you pass to your script. What happens
when we increase and decrease the strength of noise or the radius of detection? What happens when the number of birds is
very small, or the linear dimension very large? 

If you make it through all of the above and still have time, skim through the underlying code in Exercise_8_utils.py, 
and see if you can make any sense of it.
"""