"""
Exercise 5: Loops and Conditionals

How to use this file: in the command-line, navigate to the directory that contains this script using the "cd" command.
Then issue the command "python3 -i Exerises_5.py" to run this script in interactive mode. This will cause all of the
functions definitions created below to load. You can then call your custom functions just like you would a built-in
python function.

"""


def python_chatter():
    """Take in input from a user. If the string contains the word “Python” print out “Are you learning Python?”.
    If the string contains “Java”, print out “Are you sure you want to learn Java? Python is better.” Otherwise, print
    out “Not listening. I only want to talk about Python."

    Hint: you want to choose between three options based on some condition. This calls for an "if, elif, else"
    construction
    """
    string = input("Talk about coding with me: ")
    if "Python" in string:
        print("Are you learning Python?")
    elif "Java" in string:
        print("Are you sure you want to learn Java? Python is better.")
    else:
        print("Not listening. I only want to talk about Python")

    # ^ starting a comment with "TODO: " is a common way keeping track of tasks you still need to work on. In this case,
    # it indicates that you need to finish this function

    # a pass statement is included at the end of the function so that you can run this script without errors even if
    # some of the below functions are still incomplete


def is_palindrome(word):
    """
    Create a function is_palindrome that recognizes palindromes (i.e. words that look the same written backwards).
    For example, is_palindrome("radar") should return True.

    Side note: Docstrings
    Also note how this block of text is enclosed in triple quotes and placed directly underneath the function name.
    This is what's called a docstring, and it's where you should document how to use your function (though it's being
    used here to provide instructions instead). When you use the "help()" function, python is actually printing out the
    docstring for the object you enclose in parentheses. Try running this script in interactive mode (see instructions
    at the top of this file), then type "help(is_palindrome)", and this docstring should print to the console. Don't
    forget that, after using the help function to read the docstring, you can close it and return to the python prompt
    by pressing "q".

    The docstring is also used to provide descriptions of the input (called paramaters or arguments) and outputs
    (called return values) of the function. There are a few different ways to do this, one of which is shown below.
    Note how, after both the parameter description and the return value description, there is a line where we indicate
    their respective types. This helps you remember (and communicate) what kinds of objects your function can take in,
    and which types it returns. In the context of these exercises, the 'param' and 'return' descriptions are also a good
    place to start understanding how the function is meant to work.

    :param word: word to check
    :type word: str
    :return is_pal: True if word is a palindrome, false if it is not
    :type is_pal: bool
    """
    word = word.lower()
    if word == word[::-1]: #if word is the same as the reverse word
        return True
    else:
        return False


def check_fname():
    """
    Take in input from a user. Determine if it ends with “.doc”. If it does, print out “You gave me a Microsoft Word
    file. If you want a text file it should be called: “. Then print out the file name with the “.doc” replaced by
    a “.txt”

    (Since this function has no parameters, and no return values, there's nothing else we need to include in this
    docstring)
    """

    user_input = input("Enter file name and include extension: ")
    if user_input.endswith(".doc"):
        newUserInput = user_input.replace(".doc",".txt")
        print("You gave me a Microsoft Word file. If you want a text file it should be called: " + newUserInput)

    
import string

def is_palindrome_2(phrase):
    """
    Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a
    lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the
    exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.

    :param string: word to check
    :type string: str
    :return is_pal: True if word is a palindrome, false if it is not
    :type is_pal: bool
    """

    #accounting for punctuation,spacing, and punctuation below first

    new_string = ""
    for char in phrase:
        if char not in string.punctuation:
            new_string += char
    new_string = new_string.lower()
    new_string = new_string.replace(" ","")
    if new_string == new_string[::-1]:
        return True
    else:
        return False


def validate_seq():
    """
    Create a function that takes in a DNA sequence from a user. Determine if the sequence is valid using a
    combination of a loop and an if statement using the in statement. Continue to prompt the user for DNA sequence
    until a valid sequence is entered. Accomplish this using a combination of a while loop and a break statement.
    """

    seq = input("Enter a DNA sequence: ").upper()
    valid_bases = ['A','C','G','T']
    total = 0
    while True:
        for base in seq:
            if base in valid_bases:
                total += 1
                if total == len(seq):
                    break
            else:
                total = 0
                seq = input("The DNA sequence entered was invalid. Please enter a valid DNA sequence: ").upper()
                break
        if total == len(seq) and len(seq) != 0:
            print("The sequence is valid.")
            break


                


    

