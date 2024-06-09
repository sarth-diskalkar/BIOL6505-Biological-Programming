### BIOL 6505 Programming in Biological and Health Sciences Fall 2023 ###
### Homework assignment 2 ###
### Sarth Diskalkar ###
### This assignment was created by Tucker J Lancaster ###

def valid_DNA_sequence(DNA):
    # This function takes in a string containing possible DNA sequence
    # it returns True if all nucleotides are valid (A,a,C,c,G,g,T,t) 
    # and False if any nucleotide is invalid
    valid_nucleotides = ["A","a","C","c","G","g","T","t"]
    return all([x in valid_nucleotides for x in DNA])
    # all() function returns True if all items in an iterable are true
    # otherwise it returns False
def print_DNA_sequence(DNA, mode):
    # This function takes in a string containing valid DNA sequence 
    # and a mode that specifies the output format
    # Prints info to a screen, maximum characters per line
    DNA = DNA.upper()
    for i in range(0,3):
        # This loop is used to create the three possible frames on the forward strand
        num_codons = (len(DNA) - i) // 3
        DNA_sequence = DNA[i:(i + num_codons * 3)]  
        # Create DNA sequence for current frame. Ensure it is divisible by 3
        translated_sequence = translate(DNA_sequence, mode)
        # Print out direction (5' to 3') and frame to screen
        framenum = str(i)
        print('5\' to 3\' Frame: ' + framenum)
        # Print out translated_sequence
        # If nucleotide sequence mode selected
        # print nucleotide sequence and amino acid sequence
        # 60 nucleotides per line until entire sequence is printed out
        if mode == 'DNA':
            for i in range(0, len(DNA_sequence), 60):
                print(DNA_sequence[i:(i + 60)])
                print(translated_sequence[i:(i + 60)])
        else:
            print(translated_sequence)
    rev_DNA_sequence = reverse_complement(DNA)
    for i in range(0,3):
        # This loop is used to create the three possible frames on the backward strand
        num_codons = (len(rev_DNA_sequence) - i) // 3
        DNA_sequence = rev_DNA_sequence[i:(i + num_codons * 3)]
        # Create DNA sequence for current frame. Ensure it is divisible by 3
        translated_sequence = translate(DNA_sequence, mode)
        # Print out direction (3' to 5') and frame to screen
        framenum = str(i)
        print('3\' to 5\' Frame: ' + framenum)
        # Print out translated_sequence. If nucleotide sequence mode selected
        # print nucleotide sequence and amino acid sequence, 60 nucleotides per line 
        # until entire sequence is printed out
        if mode == 'DNA':
            for i in range(0, len(DNA_sequence), 60):
                print(DNA_sequence[i:(i + 60)])
                print(translated_sequence[i:(i + 60)])
        else: 
            print(translated_sequence)
def translate(DNA_sequence, mode):
    # Create dictionaries that translate codons into amino acids of appropriate format
    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'-', 'TAG':'-',
    'TGC':'C', 'TGT':'C', 'TGA':'-', 'TGG':'W',
    }
    # If VERBOSE, modify the start and stop codons and modify all codons to add space after
    if mode.upper() == "VERBOSE":
      # indicate start codons as Met and stop codons written out
      codontable.update({'ATG':'Met','TGA':'Stop','TAA':'Stop','TAG':'Stop'})
      # modify all codons to add space after
      codontable = {key: value + ' ' for key, value in codontable.items()}
    # If DNA, modify all codons to add space before and after
    elif mode.upper() == "DNA":
      # modify all codons to add space before and after
      codontable = {key: ' ' + value + ' ' for key, value in codontable.items()}
    # if COMPACT, no modification to the given codon table
    else:
      pass
    # Loop through DNA sequence codons
    out_seq = ''
    for i in range(0, len(DNA_sequence), 3):
        out_seq += codontable[DNA_sequence[i:i + 3]] 
        # Determine new amino acid with appropriate format
    return out_seq
def reverse_complement(DNA_sequence):
    # Returns string containing reverse complement of DNA sequence
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    return ''.join(complement[i] for i in DNA_sequence)[::-1]
# Part I: Determine if the user has entered the appropriate number of argments when they called the script (one)
        # Determine if the user entered one of three valid options for the mode. 
        # If there is an error in either of these, print out informative error messages 
        # indicating which error was made, what the three valid options are, and then quit the program.
import sys
if len(sys.argv) != 2:
    print("Invalid number of options\nUsage: python3 BIOL6505_HW2_Final.py <mode>\nMode can be one of the following options:\n\tCOMPACT\n\tVERBOSE\n\tDNA")
    sys.exit()
mode = sys.argv[1]
if mode.upper() not in ["COMPACT", "VERBOSE", "DNA"]:
    print(mode.upper(), "not a valid option\nUsage: python3 BIOL6505_HW2_Final.py <mode>\nMode can be one of the following options:\n\tCOMPACT\n\tVERBOSE\n\tDNA")
    sys.exit()
mode = sys.argv[1]
if mode.upper() not in ["COMPACT", "VERBOSE", "DNA"]:
    print("Mode can be one of the following options:\n\tCOMPACT\n\tVERBOSE\n\tDNA")
    sys.exit()
# Part II: Create loop to query user for DNA sequence
while True:
    dna_input = input("Enter DNA sequence (or Exit to quit the program): ")
    # Part III: Determine if user wants to exit program
    if dna_input.upper() == 'EXIT':
        sys.exit()
    # Part IV: Determine if user input is valid DNA sequence
    # If DNA sequence is not valid, print error message and allow user to enter new DNA sequence.
    while not valid_DNA_sequence(dna_input):
        print('Invalid DNA sequence. Characters must be one of A, a, C, c, G, g, T, or t')
        dna_input = input("Enter DNA sequence (or Exit to quit the program): ")
        if dna_input.upper() == 'EXIT':
            sys.exit()
    # Part V: Print out 6 translated frames to the screen in appropriate format
    print_DNA_sequence(dna_input, mode)