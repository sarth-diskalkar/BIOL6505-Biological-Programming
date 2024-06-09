import random
import matplotlib.pyplot as plt # We have not covered this module yet but we use this for plotting

def seedGrid(n):
    # This function should create a grid of n x n squares 
    # Each square should contain the value -1 (for the red species), 1 (for the blue species), or 0 (if it is empty)
    # Implement this as a list of lists: [[],[],[]]
    # Use two for loops to loop through each dimension of the grid
    # Use the random module to generate an integer of -1 or 1 to randomly seed the grid with one or the other species

    grid = []

    # Make each element of grid into a list that is n elements long, initially set to the value of zero. range() is a useful built in function for looping through a set number 
    # Loop through each element of each list and set the value to 1 or -1, using a method of the random module to do this in a random way
    for i in range(n):
        row = [random.choice([-1, 1]) for _ in range(n)]
        grid.append(row)
    return grid

def updateGrid(grid, killing_rate = 0.05, reproducing_rate = 0.05):
    # This function takes in a grid and updates it by killing and reproducing a subset of grids
    n = len(grid)
    # Determine how many cells are activated for T6SS (killing_rate * number of grids)
    num_activated = int(killing_rate * n * n)
    num_killed = 0 # Keep track of how many bacteria are killed each round

    # Loop through number of cells that are activated
    for i in range(num_activated):
        # Randomly select an x and y position, representing a cell that is activated.
        x, y = random.randint(0, n-1), random.randint(0, n-1)
        activated_cell = grid[x][y]

        # Determine if the cell contains a bacteria, if not continue!
        if activated_cell == 0:
            continue
    
        # Loop through each of the nearby neighbors of this activated cell
        for j in range(-1,2):
            for k in range(-1,2):
                # Determine if the neighbor is still within the grid. If it's not, continue to the next neighbor
                nx, ny = x + j, y + k
                if 0 <= nx < n and 0 <= ny < n:

                # Determine if the neighbor contains a bacteria, if not continue!
                    neighbor = grid[nx][ny]
                    if neighbor == 0:
                        continue

                # If the neighbor is a different species, than kill it!
                    if neighbor == -activated_cell:
                        grid[nx][ny] = 0
                        num_killed += 1

    # Determine how many cells are reproducing
    num_reproducing = int(reproducing_rate * n * n)
    num_new = 0 # Keep track of how many bacteria are produced each round
    
    # Loop through number of cells that are reproducing
    for i in range(num_reproducing):

        # Randomly select an x and y position, representing a cell that is reproducing.
        x, y = random.randint(0, n-1), random.randint(0, n-1)
        reproducing_cell = grid[x][y]

        # Determine if the cell contains a bacteria, if not continue!
        if reproducing_cell == 0:
            continue

        for j in range(-1,2):
            for k in range(-1,2):
                # Determine if the neighbor is still within the grid. If it's not, continue to the next neighbor
                nx, ny = x + j, y + k
                if 0 <= nx < n and 0 <= ny < n:

                #If the neighbor is empty, than reproduce!
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = reproducing_cell
                        num_new += 1
                        break

    print(str(num_killed) + ' bacteria were killed')
    print(str(num_new) + ' new cells were produced')

    return grid


gridsize = 300
n_steps = 100


grid = seedGrid(gridsize)

# Do not modify this code below
for i in range(n_steps):

    plt.matshow(grid, cmap='coolwarm')
    plt.title('Step ' + str(i))
    plt.show(block=False)
    plt.pause(.1)
    plt.close()

    print('Loop: ' + str(i))
    updateGrid(grid, 0.05, 0.05)

counter = {0:0, 1:0, -1:0}
for i in range(gridsize):
    for j in range(gridsize):
        counter[grid[i][j]] += 1
print(counter)


