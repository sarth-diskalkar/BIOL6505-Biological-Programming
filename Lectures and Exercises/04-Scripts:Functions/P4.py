"""sometimes, you want to write a function that is able to handle a variable number of arguments. This can be
accomplished using the unpacking operator, indicated by an asterix (*). By convention, we call the argument being
unpacked *args, but can use a more descriptive name if we want. Below is an example of a function that can take a
variable number of integers and return their sum"""


def my_sum(*args):
    # print out the arguments stored as args
    print(args)
    # print out the type of args
    print(type(args))
    # set the variable "total" to 0, then iterate through args adding each entry to "total" until you have the
    # sum of all elements
    total = 0
    for arg in args:
        total += arg # total += arg is shorthand for total = total + arg.
    # print and return the total
    print('total = {}'.format(total))
    return total

print(my_sum(1,2,3,4,5))

"""You can mix and match regular function arguments and arguments meant for unpacking, as shown in the code skeleton
below. This function takes in a genus name, and a variable number of species names, then prints each species name with
the genus tacked onto the front -- i.e., calling: 

print_genus_species_pairs('Homo', 'sapiens', 'neanderthalensis', 'habilis')

should result in the following printout:

'Homo sapiens'
'Homo neanderthalensis'
'Homo habilis'

Note that we are calling the unpacked argument *species here, instead of using the
generic *args. Try filling out the missing portions of this function"""

def print_genus_species_pairs(genus, *species):
    for s in species:
        full_name = genus + ' ' + s
        print(full_name)
print_genus_species_pairs('Homo', 'sapiens', 'neanderthalensis', 'habilis')
