import pdb

def pointless_function(x):
	y = 5*x
	z = y**x
	print(z)

	pdb.set_trace()


for i in range(5):

	pointless_function(i)
	pointless_function(i*3)
