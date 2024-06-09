# Create a script that analyzes a DNA sequence.

# Write a function that Queries the user for a DNA sequence
def query_user():
    seq = input("Enter the DNA sequence: ").upper()
    return seq

# Use error checking to determine if the user only entered A,C,G,Ts (uppercase or lowercase). Return True if the
# sequence is valid, else return False
def check_sequence(seq):
    err = ['A','C','G','T']
    for base in seq.upper():
        if base in err:
            continue
        else:
            return False
    return True

# Create a function that prints out the GC content (i.e., the percentage of nucleotides that are G or C) in a given
# sequence
def print_GC_content(seq):
    gctotal = 0
    for base in seq:
        if base in ['G','C']:
            gctotal += 1
    gc_component = gctotal/len(seq)
    print('GC-content: {}'.format(gc_component))
    # note that .format is a string method you may not have seen before. It allows you to define a string containing
    # the special characters {} (indicating a replacement field), which is replaced by the argument passed to .format.
    # this is a very powerful string method that can replace many of the clunkier (albeit simpler) methods we have
    # seen so far.

# Create a function that prints out the reverse complement of the DNA sequence
def print_reverse_compliment(seq):
    reverse_compliment = seq[::-1]
    print('Reverse Complimennt: {}'.format(reverse_compliment))

# Create a function that prints out the first X nucleotides starting from the Y position (e.g. 5 nucletides
# starting from the 3rd nucleotide). X and Y are arguments of the function.  ACGTACGTACGT
def print_segment(X, Y):
    if Y != 0:
        segment = x[Y-1:(X+Y)-1]
    else:
        segment = x[Y:(X+Y)]
    print('{} nucleotides starting from nucleotide {}: {}'.format(X, Y, segment))
    # note here that we are using .format with multiple replacement fields and multiple arguments. The first argument
    # will fill the first field, the second argument the second field, and so on.

# Write a function that queries the user for a DNA sequence, checks it for errors, prints the GC compliment, and prints
# the reverse compliment. You should be able to accomplish this using the functions you have already written
def analyze_sequence():
    seq = query_user()
    error_checking = check_sequence(seq)
    if error_checking == False:
        print('Input another DNA sequence: ')
    else:
        print('DNA sequence is valid.')
    print_GC_content(seq)
    print_reverse_compliment(seq)
    return seq

# x = query_user()
# y = check_sequence(x)
# print(y)
# print_GC_content(x)
# print_reverse_compliment(x)
x = analyze_sequence()
print_segment(5,2)
