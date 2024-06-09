# Script modified by Tucker J Lancaster
### Sarth Diskalkar ###
import argparse, random
import numpy as np
import matplotlib.pyplot as plt

"""
Assignment 4: Bacterial Warfare 

General instructions: Please use this code skeleton for your implementation, making no changes to the function names,
function parameter names, or function return-value names. We recommend that you complete this assignment in the
following order:
	1. implement the argument parser, as described in the "if __name__ == '__main__'" block at the bottom of this script
	2. implement seed_grid
	3. implement update_grid
	4. implement update_plot
	5. run your code and confirm that the plots you see resemble those from the paper
"""

def seed_grid(n):
	"""
	This function is used to create the initial "playing field", an n x n array randomly populated with 1's (for the
	red species) and -1's (for the blue species). Initially, populate every position in the grid (i.e., fill every
	position with either a 1 or a -1).

	:param n: grid dimension. returned grid will be nxn
	:type n: int
	:return grid: n x n grid, randomly populated with 1's and -1's
	:rtype grid: numpy.ndarray
	"""
	grid = np.random.choice([-1, 1], size=(n, n)).astype(np.int8)	# properly define this variable
	return grid

def update_grid(grid, killing_rate, reproducing_rate):
	"""
	This function is used to simulate a single step of the bacterial warfare simulation. It takes in the current
	playing field (grid), updates it (through killing and reproduction), and returns the updated playing field (grid).

	:param grid: initial grid
	:type grid: numpy.ndarray
	:param killing_rate: proportion of cells that activate their TS66 system each step
	:type killing_rate: float
	:param reproducing_rate: proportion of cells that attempt to reproduce each step
	:type reproducing_rate: float
	:return grid: updated grid
	:rtype grid: numpy.ndarray
	"""

	# Determine how many bacteria are activated for T6SS (killing_rate * number of cells alive)
	num_activated = int(killing_rate * len(np.where(grid != 0)[0])) # Properly define this variable

	# use a for loop to activate the specified number of bacteria.
	for i in range(num_activated):
		# Randomly choose a grid position
		x = np.random.randint(low=0, high=len(grid)) # define x appropriately
		y = np.random.randint(low=0, high=len(grid))  # define y appropriately
		# using a while loop, choose new random grid positions until you encounter an occupied position (if the position
		# you chose initially was unoccupied)
		while grid[x, y] == 0:
			x = np.random.randint(low=0, high=len(grid))  # define x appropriately
			y = np.random.randint(low=0, high=len(grid))  # define y appropriately

		# kill all bacteria of the opposite species occupying positions adjacent to the bacterium in the chosen position
		for j in range(-1,2):
			for k in range(-1,2):
				neighbor_x, neighbor_y = x + j, y + k
				if not (0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid)):
					continue
				if grid[neighbor_x, neighbor_y] == 0:
					continue
				if not grid[neighbor_x, neighbor_y] == grid[x, y]:
					grid[neighbor_x, neighbor_y] = 0


	# Determine the number of bacteria that will reproduce (number of bacteria alive * reproduction rate)
	num_reproducing = int(reproducing_rate * len(np.where(grid != 0)[0])) # Properly define this variable

	# Loop through number of bacteria that are reproducing
	for i in range(num_reproducing):
		# Randomly choose a grid position
		x = np.random.randint(low=0, high=len(grid)) # define x appropriately
		y = np.random.randint(low=0, high=len(grid))  # define y appropriately
		# using a while loop, choose new random grid positions until you encounter an occupied position (if the position
		# you chose initially was unoccupied)
		while grid[x, y] == 0:
			x = np.random.randint(low=0, high=len(grid)) # define x appropriately
			y = np.random.randint(low=0, high=len(grid))  # define y appropriately

		# if there is not an empty position adjacent to the cell, continue without modifying the grid
		species = None
		if grid[x, y] == 1:
			species = 1
		elif grid[x, y] == -1:
			species = -1
		else:
			continue

		offsets = [-1, 0, 1]
		neighbor_x, neighbor_y = np.meshgrid(x + np.array(offsets), y + np.array(offsets))
		neighbor_x = neighbor_x.flatten()
		neighbor_y = neighbor_y.flatten()
		valid_coords = (0 <= neighbor_x) & (neighbor_x < grid.shape[0]) & (0 <= neighbor_y) & (neighbor_y < grid.shape[1])
		
		neighbor_x = neighbor_x[valid_coords]
		neighbor_y = neighbor_y[valid_coords]
		neighbor_values = grid[neighbor_x, neighbor_y]
		empty_neighbors = neighbor_values == 0
		if not np.any(empty_neighbors[:] == True):
			continue
		# if there is at least one empty position adjacent to the cell, set one of the empty positions to the species
		# of the reproducing cell. The filled position should be chosen randomly from all available positions adjacent
		# to the focal bacterium.
		neighbor_x = neighbor_x[empty_neighbors]
		neighbor_y = neighbor_y[empty_neighbors]
		rand = np.random.choice(len(neighbor_x))
		grid[neighbor_x[rand], neighbor_y[rand]] = species
	
	return grid

def update_plot(img_obj, grid, i):
	"""
	This function is used to update the plot of the current bacterial distribution across the playing field. The
	parameter img_obj should be a matplotlib.image.AxesImage object, which is the type of object returned by
	matplotlib.pyplot.matshow().

	:param img_obj: plotting object to be updated
	:type img_obj: matplotlib.image.AxesImage
	:param grid: array containing the current playing field
	:type grid: numpy.ndarray
	:param i: current simulation step
	:type i: int
	"""

	# use the matplotlib.image.AxesImage.set_data() method to update array associated with img_obj
	img_obj.set_data(grid)
	# update the title to be "Step i", where i is the current step
	img_obj.axes.set_title(f"Step {i}")
	# use the matplotlib.pyplot.draw() command to redraw the figure
	plt.draw()
	# use the matplotlib.pyplot.pause() command to delay the drawing of the next frame by 0.1 seconds
	plt.pause(0.1)
  	# remove this pass statement when your function is implemented

	# this return statement is not necessary, but is included to help with grading
	return img_obj


if __name__ == '__main__':
	# Use argparse to take in the grid size, the number steps you want to simulate, the killing_rate, and the
	# reproduction_rate. Set the default values of these arguments to what was used in the paper. Use flagged arguments
	# for all four arguments. Use the flag names "--gridsize", "--n_steps", "--killing_rate", and "--reproduction_rate".
	# include a descriptive help string for each, and specify the expected type. Please place all of your argument
	# parsing code here, within the __name__ == '__main__' block.

	# add your argument parsing code here
	args = None  # properly define this variable

	# the code below is complete, but you should read it to better understand how the functions you write above should
	# operate
	grid = seed_grid(args.gridsize)
	img_obj = plt.matshow(grid, cmap='seismic')
	for i in range(args.n_steps):
		print('Loop: ' + str(i))
		update_grid(grid, args.killing_rate, args.reproduction_rate)
		update_plot(img_obj, grid, i)



