# Script written by Tucker J Lancaster 
import importlib
from contextlib import contextmanager
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

"""
Instructions: Place this script in the same directory as your assignment 4 solutions. If you have renamed you solution
script from "Assignment4_Template", change the definition of "script_name" below accordingly. Now run this script
from the terminal using "python3 Assignment4_Checker.py" or "python Assignment4_Checker.py", depending on how your
system is configured. I recommend you try running this script with the un-modified template script first to confirm that 
it is working. 

If this script runs successfully, you should see print-out start to appear in the terminal as this script checks the 
three functions (seed_grid, update_grid, and update_plot) that you wrote. seed_grid and update_grid are each tested ten 
times each, to allow for partial credit if your solution only works sometimes. If you are failing a particular check, 
and are not sure why, look at the contents of the associated testing function below. These functions are split into 
multiple subtests, each contained within a "with ignore_all(verbose):" block. Above each block is an explanation of 
what the test is trying to check. 

The three functions are tested independently, such that you could get all of the points for update_plot, for example, 
even if you haven't implemented the other two functions. I will use a very similar script to grade your submissions, 
so please use this tool to your advantage. To receive credit for a portion of your submission that does not pass this


As much as possible, I have written this script to minimize the chances
of the randomness implicit to this assignment affecting the score, but it remains possible. For a correctly implemented
solution, however, this should be exceedingly rare.
"""

# name of your solution script. Do not include the .py extension
script_name = 'Assignment4_Template'

@contextmanager
def ignore_all(verbose=False):
    try:
        yield
    except Exception:
        if verbose:
            print(Exception)
        else:
            pass


def test_seed_grid(module, verbose=False):
    # 10 points possible
    points = []
    # check grid seeds with correct shape (1pt)
    with ignore_all(verbose):
        points.append(0)
        test_grid = module.seed_grid(10)
        points[-1] += (int(test_grid.shape == (10, 10)))
    # check grid is of type np.ndarray (1pt)
    with ignore_all(verbose):
        points.append(0)
        points[-1] += (int(type(test_grid) == np.ndarray))
    # check dtype is np.int8 (1pt)
    with ignore_all(verbose):
        points.append(0)
        points[-1] += (int(type(test_grid[0, 0]) == np.int8))
    # check seed grid fully populates, with no 0's (1pt)
    with ignore_all(verbose):
        points.append(0)
        test_grid_large = module.seed_grid(10000)
        points[-1] += (int(0 not in test_grid_large))
    # check that max value in seed grid is 1 (1pt)
    with ignore_all(verbose):
        points.append(0)
        points[-1] += (int(test_grid_large.max() == 1))
    # check that min value in seed grid is -1 (1pt)
    with ignore_all(verbose):
        points.append(0)
        points[-1] += (int(test_grid_large.min() == -1))
    # check that the split the grid seeds approximately as many 1's as it does -1's (4 pts)
    with ignore_all(verbose):
        points.append(0)
        points[-1] += (4 * np.isclose(test_grid_large.mean(), 0, rtol=0, atol=0.1))
    return points


def test_update_grid(module, verbose=False):
    # 80 points possible
    points = []
    # test that the function can handle corners and edges without crashing, and that it at least tried to modify the
    # grid (5 points). Further confirm and that a bacterium kills all adjacent bacteria of the opposite species
    # (5 points)
    with ignore_all(verbose):
        points.append(0)
        test_grid = np.ones((2, 2))
        test_grid[0, :] = -1
        test_grid_og = test_grid.copy()
        test_grid = module.update_grid(test_grid, 0.25, 0)
        points[-1] += (5 * (test_grid != test_grid_og).any())
        points[-1] += (5 * (np.abs(test_grid.sum()) == 2))
    # test that like does not kill like (15 points)
    with ignore_all(verbose):
        points.append(0)
        test_grid = np.zeros((9, 9))
        test_grid[4, 4] = 1
        for _ in range(3):
            test_grid = module.update_grid(test_grid, 1.0, 1.0)
        points[-1] += (15 * (test_grid.sum() == 8))
    # test that unlike kills unlike (15 points)
    with ignore_all(verbose):
        points.append(0)
        test_grid = np.zeros((10, 10))
        test_grid[3, 3] = 1
        test_grid[4, 4] = -1
        test_grid = module.update_grid(test_grid, 0.5, 0)
        points[-1] += (15 * (np.sum(test_grid != 0) == 1))
    # test reproduction (10 points)
    with ignore_all(verbose):
        points.append(0)
        test_grid = np.zeros((10, 10))
        test_grid[3, 3] = 1
        test_grid = module.update_grid(test_grid, 0, 1.0)
        points[-1] += (10 * (np.sum(test_grid) == 2))
    # test that reproduction will only occur into empty positions (10 points)
    with ignore_all(verbose):
        points.append(0)
        test_grid = np.tile([-1, 0, 1], (3, 1)).T
        for _ in range(10):
            test_grid = module.update_grid(test_grid, 0, 1.0)
        points[-1] += 10 * (((test_grid[0] == -1).all()) & ((test_grid[1] != 0).all()) & ((test_grid[2] == 1).all()))

    # test that reproduction occurs in a randomly chosen direction (10 points)
    with ignore_all(verbose):
        points.append(0)
        poses = []
        for iter in range(100):
            test_grid = np.zeros((10, 10))
            test_grid[3, 3] = 1
            test_grid = module.update_grid(test_grid, 0, 1.0)
            pos = list(test_grid[2:5, 2:5].flatten())
            pos.pop(4)
            poses.append(pos.index(1))
        points[-1] += (5 * (len(set(poses)) >= 6)) + (5 * (len(set(poses)) >= 4))
    # test that the correct number of bacteria reproduce (10 points)
    with ignore_all(verbose):
        points.append(0)
        test_grid = np.zeros((10, 10))
        test_grid[[0, 0, -1, -1], [0, -1, 0, -1]] = 1
        test_grid = module.update_grid(test_grid, 0, 1.0)
        points[-1] += (10*(test_grid.sum() == 8))
    return points


def test_update_plot(module, verbose=False):
    # 10 points possible
    points = []
    test_grid_1 = np.ones((20, 20))
    test_grid_2 = np.zeros((20, 20))
    # Check that the grid updates (4 pts)
    with ignore_all(verbose):
        points.append(0)
        img_obj = plt.matshow(test_grid_1)
        module.update_plot(img_obj, test_grid_2, 1)
        points[-1] += (4 * (img_obj.properties()['array'].data == test_grid_2).all())
        plt.close('all')
    # Check that the title updates (1 pt)
    with ignore_all(verbose):
        points.append(0)
        points[-1] += (img_obj.axes.get_title().strip()[-1] == '1')
    # Update again, and check that the grid updates (4 pts)
    with ignore_all(verbose):
        points.append(0)
        img_obj = plt.matshow(test_grid_2)
        module.update_plot(img_obj, test_grid_1, 2)
        points[-1] += (4 * (img_obj.properties()['array'].data == test_grid_1).all())
        plt.close('all')
    # check that the title updated a second time (1 pt)
    with ignore_all(verbose):
        points.append(0)
        points[-1] += (img_obj.axes.get_title().strip()[-1] == '2')
    plt.close('all')
    return points


if __name__ == '__main__':
    mod = importlib.import_module(script_name)

    sgs = []
    print('testing seed_grid for 10 repetitions:')
    for iter in range(10):
        sg = test_seed_grid(mod)
        print(f'test rep {iter}/9: {sg}')
        sgs.append(sg)
    sgs = list(np.array(sgs).mean(axis=0))
    print(f'\nmean scores: {sgs}')
    print(f'total: {sum(sgs)}/10\n\n')

    ugs = []
    print('testing update_grid for 10 repetitions:')
    for iter in range(10):
        ug = test_update_grid(mod)
        print(f'test rep {iter}/9: {ug}')
        ugs.append(ug)
    ugs = list(np.array(ugs).mean(axis=0))
    print(f'\nmean scores: {ugs}')
    print(f'total: {sum(ugs)}/80\n\n')


    print('testing update_plot (no repetition):')
    up = test_update_plot(mod)
    print(f'test rep 0/0: {up}')
    print(f'total: {sum(up)}/10\n\n')

    print(f'total score on this assignment: {sum(sgs + ugs + up)}/100')






