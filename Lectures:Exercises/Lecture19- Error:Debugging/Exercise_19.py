"""
Exercise 17: Exception-Handling and PDB
"""

"""
1. Errors and Exceptions

If we think of "errors" in python as all of the events that can cause our program to terminate prematurely, then 
"exceptions" are the subset of those errors that we can catch and handle at runtime to prevent termination. 

Some errors cannot be handled, and will (almost) always terminate your program. We'll call these irrecoverable errors.
One such error you've likely encountered is the SyntaxError. This occurs when a typo makes the code unreadable to the 
python interpreter. As you've likely noticed, this tends to cause the program to terminate and throw an error 
immediately, even if the syntax error is at the very end of your script. Other generally irrecoverable errors include 
the MemoryError (indicating the RAM is out of memory) and a RecursionError (triggered by infinite recursion). To python, 
there isn't much difference between these irrecoverable errors, and the less severe errors we are calling exceptions. 
But practically speaking, we should not try to catch these kinds of errors, and instead just let them terminate the 
program. Trying to keep a program limping along despite an irrecoverable error might cause your system to crash, rather 
than the program.

Most of the errors you encounter, however, are likely exceptions. By default, these will cause your program to exit just
like irrecoverable errors. But because the problems they indicate are comparatively minor, we often want to instead 
catch these errors at runtime and try to resolve them automatically. To a degree, you've been doing this already by
using if-else constructions to prevent exceptions from occurring in the first place. Often, however, it is more elegant
to handle exceptions with a try-except construction. The function provided below, while valid, will throw an error if
idx is greater than 3. To make it more robust, do the following:

1) Try passing in a value greater than 3, and take note of the kind of error that occurs
2) Modify the function using a try-except construciton such that, if this specific error occurs, the function instead 
prints "invalid input". Call your new function "less_error_prone_function"
3) again try passing in a value greater than 3, and confirm that the new function prints the warning message and does 
not throw an error
4) An IndexError is not the only type of error this function might encounter. What type of error occurs if we pass in 
a string or a float instead of an integer? Try for yourself and see
5) Modify your function again to separately handle the error that occur when idx is an integer greater than 3, and
the error that occurs when idx is not an integer at all. Call this function "even_less_error_prone_function". If idx
is an integer greater than 3, have the function print "idx out of bounds". If idx is not an integer, have the
function print "idx must be type int". Hint: you can have multiple "except" clauses associated with a single "try"
statement
6) Try passing an invalid type (such as float or string) to your new function, and confirm that it prints "idx must
be type int", instead of throwing an error

Despite our best attempts, there will often be exceptions we did not account for. In general, we do not want to 
silence these errors (i.e., prevent the program from terminating) as they could indicate a serious problem. There are
situations, however, when you might want to execute some code in the event of such an error before the program actually
terminates (For example, maybe you want to save some of your data as a csv before you exit). We can accomplish this with
a special except construction, like so:

    except Exception as e:
        # code inserted here will run before termination
        raise e

Here, "Exception" with a capital E is the base-class that underlies non-critical errors like IndexError and TypeError. 
This except statement will therefore catch any error built upon the Exception class. The addition of "as e" to the 
except statement causes the Exception to be stored as the variable "e" when the except clause triggers. Within the 
except clause, we include any code that we want to run before termination, and then end it with "raise e". This will
cause the Exception, which we suppressed temporarily, to terminate the program.

7) Write one final version of your function, and call it "robust_function". Make the following modifications:
    - replace the "except TypeError:" clause with an "except Exception as e:" clause, as described above. Have this 
      clause print "unknown error encountered" before exiting
    - replace the "except IndexError:" clause with an "except IndexError as e:" clause. Within the clause, instead of
      printing "idx out of bounds", print e.
"""


def error_prone_function(idx):
    short_list = ['a', 'b', 'c', 'd']
    return short_list[idx]


def less_error_prone_function(idx):
    # modify the code below as explained in the instructions
    short_list = ['a', 'b', 'c', 'd']
    return short_list[idx]


def even_less_error_prone_function(idx):
    # modify the code below as explained in the instructions
    short_list = ['a', 'b', 'c', 'd']
    return short_list[idx]


def robust_function(idx):
    # modify the code below as explained in the instructions
    short_list = ['a', 'b', 'c', 'd']
    return short_list[idx]


"""
2. PDB debugging

While try-except constructions can help us catch and handle errors at runtime, they require us to first understand why 
the error is occurring. For this, we an use PDB, the "Python DeBugger". For now, we'll focus on the pdb.set_trace()
function. Whenever this function is encountered during execution, python will pause and enter the interactive debugger.
Within the debugging console, you will have access to any of the variables that were defined at the moment the trace
was set. 

Below is a contrived example of a buggy function, showing where you might set the trace to figure out the 
problem. Uncomment the line below the function definition so that the function will execute, and run this script. Once
the debugging console opens, confirm that you can access the variables a, b, and c by calling print(a), print(b), and
print(c). Check their types using type(a), type(b), and type(c). Try calling print(d) -- you will get an error: why?
now type s and press enter to step your code forwards. Try calling print(d) again -- does it work this time? What 
happens when you type c and press enter, resuming the code execution? What happens if you move pdb.set_trace() below the
line where we defined e?
"""

import pdb

def buggy_function():
    a = 12
    b = 'hello'
    c = [1, 2, 3]
    pdb.set_trace()
    d = 'unused variable'
    e = a/b + c

# buggy_function()

"""
PDB debugging continued

pdb.set_trace() is such a commonly used function that, in versions of python starting with 3.7, a built-in function 
called "breakpoint()" was added that imports pdb and calls pdb.set_trace() in a single line. If you are using 
python>=3.7 (which all of you should be) you should use breakpoint() instead of pdb.set_trace(). The advantage of 
breakpoint() is that, when called, it consults a python environment variable called PYTHONBREAKPOINT. This variable
can be set at the environment-level to modify the behavior of breakpoint(). This functionality is a bit beyond the scope 
of this class, and depending on your OS, shell type, etc. might be tricky to actually utilize. But know that, when 
properly used, it allows you to "silence" all of your breakpoint() calls (without individually commenting them out or
removing them) and can even be used to execute a callable other than pdb.set_trace() at each breakpoint (such as a
function from a more advanced debugging library). 

For now, re-comment out the "buggy_function()" call above, and uncomment the "buggy_function_2()" call below. Run your
script again, and confirm that breakpoint() does indeed operate identically to pdb.set_trace()
"""

def buggy_function_2():
    a = 12
    b = 'hello'
    c = [1, 2, 3]
    breakpoint()
    d = 'unused variable'
    e = a/b + c

# buggy_function_2()
