"""
Exercise 13: Numpy

In this exercise you will practice creating, manipulating, indexing and slicing
"""

import numpy as np

"""
1. Manual array creation
Convert the following lists to numpy arrays. Store the array from 1a as a, the array from 1b as b, etc.
    a. [7, 7, 6]
    b. [[3, 4, 5], [0, 2, 7], [1, 9, 6]]
    c. [[[3, 1, 8], [3, 8, 3], [5, 5, 6]], [[0, 1, 6], [9, 4, 9], [6, 7, 4]], [[8, 7, 7], [2, 6, 0], [0, 9, 6]]]
"""

# your code here

"""
2. Array creation functions 
Create each of the following arrays using numpy array creation functions without resorting to manual construction.
Store the array from 2d as d, the array from 2e as e, etc. You may find this page from the numpy docs useful:
https://numpy.org/doc/stable/user/basics.creation.html

    d. [1 2 3]

    e. [1 3 5]

    f. [5.1 5.3 5.5]

    g. [[1. 0. 0.]
        [0. 1. 0.]
        [0. 0. 1.]]

    h. [[0. 0. 0.]
        [0. 0. 0.]
        [0. 0. 0.]]

    i. [[1. 1. 1.]
        [1. 1. 1.]
        [1. 1. 1.]]
"""

# your code here

"""
3. Element-wise array arithmetic 
Using element-wise array arithmetic (+, -, *, /, of two arrays) and scalar arithmetic (+, -, *, / of an array and a 
scalar) to generate the following arrays from the arrays you made in part 2. Continue to store your resulting arrays
as the indicated letter. 

    j. [[0. 1. 1.]
        [1. 0. 1.]
        [1. 1. 0.]]

    k. [5.1  10.6  16.5]

    l. [[5. 5. 5.]
        [5. 5. 5.]
        [5. 5. 5.]]

    m. [[-3. -4. -4.]
        [-4. -3. -4.]
        [-4. -4. -3.]]

    n. [0.5  1.5  2.5]


"""

# your code here

"""
4. Array Properties 
Arrays have a variety of properties that provide useful information. You can use the following line of code to list
these properties:

[prop for prop in dir(g) if not callable(getattr(g, prop))]

Determine which array property will give you each of the following pieces of information. You do not need to store the
output, just print it.:
    - the data type of the values stored in array g. Should return float64'
    - the number of dimensions of array g. Should return 2
    - the total number of elements in array g. Should return 9
    - the number of rows and columns in array g. Should return (3, 3)
"""

# your code here

"""
5. Array indexing
Use indexing to do the following (don't forget that numpy indexes start at 0!):
    - print the element in the second row, first column of array b. Should return 0
    - using negative indexing, print the element in the last row, last column of array b. Should return 6
    - change the element in the second row, second column of array b from 2 to 10. Print array b and confirm that the
      value actually changed.
"""

# your code here

"""
6. Array slicing
Use slicing to accomplish the following:
    - print the second row of array b. Should return [0  10  7]
    - print the second column of array b. Should return [ 4  10  9]
    - create a new array containing only the first and second rows of array b. Store this array as o
    - create a new array containing only the first and second columns of array b. Store this array as p
    - set both of the elements in the first row of p to 20. Print p to confirm this worked. Now print array b. Did 
      modifying p also modify b? Why or why not?
"""

# your code here

"""
7. Array Filtering
Using conditional operations (>, <, >=, <=, ==, !=), achieve the following:
    - print all elements in array b that are greater than 5. Should return [20  20  10  7  9  6]
    - print all elements in array c that are greater than 6 but not equal to 8. Should return [9 9 7 7 7 9]
      Hint: you can slice an array on multiple conditionals by enclosing each condition in parentheses and using bitwise
      conditional operators (& for "and", | for "or", ^ for "xor", ~& for "nand", ~| for "nor", and ~^ for "xnor"). 
      For example, c[(c<2) | (c>5)] would return all values in c that are less than 2 or greater than 5.
    - print all elements in array c that are even. Should return [8 8 6 0 6 4 6 4 8 2 6 0 0 6]. The modulo operator may
      be useful here.
    - set all of the even elements in array c to 0. print array c to confirm your changes stuck
    - increase all of the odd elements in array c by 1. The compound assignment operator += may be useful.
    - Set the elements along the diagonal of array b to 0. Hint: use array g to construct your conditional


"""

# your code here

"""
8. Summary Functions and useful methods
Find the numpy function or array method that finds/achieves each of the following. Apply the function/method to 
test_array (defined for you) and confirm that you get the correct output. You can use this line of code to print all
of the available array methods: 

[prop for prop in dir(g) if callable(getattr(g, prop))]

    - the average of all elements in test array (should be 49.5)
    - the average of each row of test array (should be [4.5  14.5  24.5  34.5  44.5  54.5  64.5  74.5  84.5  94.5]
    - The cumulative sum of test array (should return an array of 100 numbers, starting with 0 and ending with 4950)
    - the max value within each row (should be [9  19  29  39  49  59  69  79  89  99]
    - the flat index of the largest value in test_array (should be 99)
    - the standard deviation of all elements in test_array
    - an array method that returns a copy of the array but with a different datatype. Use this method to create a copy
      of test_array (call it test_array_2) with the dtype set to 'int8' instead of 'int32'. Use the nbytes array 
      property to compare the memory usage of test_array and test_array_2
    - the peak-to-peak value along axis 1 (should be [9 9 9 9 9 9 9 9 9 9])

"""

test_array = np.arange(100).reshape((10, 10))




