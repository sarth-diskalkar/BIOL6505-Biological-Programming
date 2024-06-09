"""
Exercise 14:

In this exercise, you will be using numpy to analyze some real-world data from the Streelman and McGrath labs. As we
discussed last class, many Cichlid species from Lake Malawi exhibit an interesting mating behavior in which the males
build large sand structures called bowers. One way we study this process is by using a depth sensor to measure how the
sand surface changes over time. This data is stored as a 3D numpy array, where the first dimension corresponds to time,
and the second and third dimensions correspond to the 2D spatial position, and the value of each element of the array
contains the sand-height at a particular time and location in the frame. These 3D arrays can exceed 10 GB for a single
bower-construction sequence, so you will be working with a much smaller array containing one depth snapshot per day,
rather than one snapshot every five minutes.
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_depths(depth_array):
    # this function is written for you, and will be used later for visualizations.
    fig, ax = plt.subplots(3, depth_array.shape[0]//3, sharex='all', sharey='all')
    flax = ax.flatten()
    for d in range(depth_array.shape[0]):
        flax[d].imshow(depth_array[d], vmin=0, vmax=25)
        flax[d].set(title=f'day {d}')

"""
1. Setup:
Use numpy to load the file called "daily_depths.npy", and store the array it contains as "depth". Use the array.shape
method to find the shape of this array. Store the first value in this tuple as "n_days", the second value as "n_rows",
and the third value as "n_cols". 

"""

depth = 'replace with code'
# your code here

"""
2. Now, uncomment the line below to visualize the sand surface at each day.
"""

# plot_depths(depth)

"""
3. You probably noticed in the visualization that large portions of the depth data seems to be missing. Physically, 
these "blindspots" result from reflections and refractions that confuse the sensor. In the array, the missing
data is filled in with np.NaN values. How many np.NaN values are in the depth array? How does this compare to the 
total number of elements in the array? write a small function that takes in any numpy array, and prints out the 
fraction of all elements in that ray that are np.NaN.
"""


def nan_contents(arr):
    # remove the pass statement and fill in this function
    pass

nan_contents(depth)

"""
4. One way we might fill in some of this missing data is with interpolation. Today's lecture covered interpolation in
1D (i.e., interpolation in a 1xn vector). While 2D or 3D interpolation could be useful here, we'll stick with 1D for now
(but if you are interested in higher-dimensional interpolation, these can be accomplished with the scipy.interpolate
library, specifically using interp2d and interpn). Our goal is to interpolate along the 0 axis, treating each pixel
independently and interoplating based on depth values forwards and backwards in time.

Before we try to interpolate at every pixel, let's practice on a single pixel. Begin by isolating the pixel in the 
300th row and the 300th column. You should get a length 12 vector of values, 2 of which will be np.NaN values. Store 
this vector as "pixel". Now use the np.interp function to replace the two np.NaN values in pixel with interpolated
values. Confirm that the values seem reasonable, then move onto problem 5.

Hint: use "pixel = depth[:, 300, 300].copy()" to get your pixel. This will prevent you from unintentionally modifying
the original depth array. 
"""

# your code here

"""
5. Now, make a copy of the depth array and perform interpolation at every pixel. to fill in the np.NaN values.
When you perform the interpolation, be sure to use left=np.nan and right=np.nan to ensure you are not exterpolating
any values. When you are done, uncomment the call to plot_depths to visualize your output, and uncomment the call
to nan_contents to print out the new np.nan fraction.

HINT: if you see an error saying "array of sample points is empty", that likely means that the pixel you are working
on is np.nan for at every time point. Use an if statement to catch these empty pixels before attempting to interp,
and leave them as all np.nan

HINT2: similar to the last problem, use "depth_interp = depth.copy()" to create your copy. If you use 
"depth_interp = depth", any modifications you make to depth_interp will also modify depth
"""

# your code here

# plot_depths(depth_interp)
# nan_contents(depth_interp)

"""
6. Now that we have both the depth and the depth_interp arrays, maybe we want to visualize them side by side. We could
do that with some fancy tweaks to the plotting function, or we could just use the plotting function as-is and pass 
it stacked arrays. The goal here is to have the plotter show, for every day, the raw depth picture and the interpolated 
depth picture one on top of the other. Try to accomplish this using what you have learned about concatenation and 
stacking. If you're smart about it, this can be done in a single function call. Uncomment the plot_depths command to visualize
your results.

Hint: The array you pass in should be 12x766x466
"""

stacked_depths = 'your code here'
# plot_depths(stacked_depths)


