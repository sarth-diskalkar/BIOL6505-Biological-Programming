import sys
print(sys.argv)

import argparse

parser = argparse.ArgumentParser(description='This is a sample program')
print(parser)
#print(dir(parser))

parser.add_argument("loops", type=int, help="Enter the number of times you want the loop to run.")
parser.add_argument('-f','--flags',help='This is a required input file', required=True, type=str)
parser.add_argument('-n','--number', help='This is an optional number to store', type=int)

args = parser.parse_args()


