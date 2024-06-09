"""
Assignment 5: Automatic Primer Identification

In this assignment, you will practice using python's subprocess library, the pyfasta library, and the primer3
command-line-interface to automatically identify primers. This template provides a potential route to a completed
script, but the implementation details are entirely up to you. The checker script, as you will see, does little more
than confirm that your script prints the correct primers to the console for a handful of argument combinations.
Author: Tucker J Lancaster
"""
### Sarth Diskalkar ###

import argparse, pdb
import subprocess
from pyfasta import Fasta

"""
If you have not already, install pyfasta and primer3 into the current environment using the following commands:
conda install -c bioconda primer3
conda install -c bioconda pyfasta
"""

"""
Create your parser and arguments. Your script should expect three positional arguments: First, the name of a
fasta file, second, the chromosome you want to amplify, and third, the position you want amplified. Enforce that
the first two arguments are of type str, and the third is of type int.
"""

# your code here
parser = argparse.ArgumentParser()
parser.add_argument('fasta_file', type=str, help='Enter a genome file containing DNA sequence')
parser.add_argument('chromosome', type=str, help='Enter the chromosome you want amplified')
parser.add_argument('position', type=int, help='Enter the position you want amplified')
args = parser.parse_args() 

"""
Open the fasta file and read in the entirety of the sequence. You can use whatever data structure you prefer.
"""

# your code here
f = Fasta(args.fasta_file)
f = str(f[args.chromosome][:])

"""
Identify the sequence 500 bp upstream and downstream of the requested position and store it as a string.
"""

# your code here
sequence = f[args.position - 500 : args.position + 500]
pdb.set_trace()

"""
Add braces to the DNA sequence 100 bp upstream and downstream of the requested position. Alternatively, you can use 
an argument in the input file to specify this
"""

# your code here
sequence = sequence[:400] + '{' + sequence[400:600] + '}' + sequence[600:]

"""
Create an input file containing the DNA sequence and specify a product length of 600 - 800 base pairs
"""

# your code here
with open('input_file.txt', 'w') as file:
    file.write(f"SEQUENCE_ID=example\n")
    file.write(f"SEQUENCE_TEMPLATE={sequence}\n")
    file.write(f"SEQUENCE_TARGET=400,200\n")
    file.write(f"PRIMER_PRODUCT_SIZE_RANGE=600-800\n")
    file.write(f"SEQUENCE_INTERNAL_EXCLUDED_REGION=400,200\n=")

    # file.write(f"PRIMER_PICK_LEFT_PRIMER=1\n")
    # file.write(f"PRIMER_PICK_RIGHT_PRIMER=1\n")
    # file.write(f"SEQUENCE_INTERNAL_EXCLUDED_REGION=400,200\n=")
    # file.write('=')

    
"""   
Execute the primer3_core command on the input file you created.
"""

# your code here
# subprocess.run(["primer3_core", "input_file.txt"], check=True)

input_file = 'input_file.txt'
output_file = 'output_file.txt'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    subprocess.run(['primer3_core'], stdin=infile, stdout=outfile, check=True)

""" 
Read in and parse the output to identify the sequence of best two primers. Print these out to the user
"""

# your code here
with open('output_file.txt', 'r') as file:
    output_data = file.read()
lines = output_data.split('\n')
for line in lines:
    if line.startswith("PRIMER_LEFT_0_SEQUENCE"):
        left_primer = line.split('=')[1]
    elif line.startswith("PRIMER_RIGHT_0_SEQUENCE"):
        right_primer = line.split('=')[1]

print(left_primer)
print(right_primer)
