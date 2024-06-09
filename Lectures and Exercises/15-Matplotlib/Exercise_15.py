"""
Exercise 15: Plotting Basics

Matplotlib is one of those libraries where there are about a dozen ways to access any given method/function/attribute.
In this exercise I will walk you through some of my preferred approaches, but these are by no means definitive nor
optimal for every situation.
"""

import matplotlib.pyplot as plt
import numpy as np

"""
1. Setting up a figure

I almost always start off with the plt.subplots() function (not the same as the plt.subplot() function). This is a 
convenience function that lets you create a figure with one or more associated subplots in a single call. plt.subplots() 
returns a tuple of two objects -- a Figure object, and an Axes object (or an array of Axes objects, when you have more 
than one subplot). The following syntax  is therefore useful for simultaneously storing the Figure as fig and the 
Axes/array of Axes as ax:

fig, ax = plt.subplots()

Start by using the plt.subplots() command to create a Figure with a single Axes. You can do this by calling 
plt.subplots() with the default parameters, i.e, exactly as it is written above. Under the hood, this is the same as
calling plt.subplots(nrows=1, ncols=1). store the returned Figure as fig, and the returned Axes as ax. 

For more information on using plt.subplots() to create figures with multiple subplots, see the documentation here:
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
"""

# your code here

"""
2. A Basic Plot

In the lecture, most of the plots were created with plt.* commands, such as plt.plot(), plt.bar(), plt.pie(), et cetera.
These are fine, but make it hard to control exactly where (i.e., on what Axes object) your plot appears. To accomplish
this, we can instead use the Axes object methods. These operate almost identically to their plt.* versions, but will
always plot to the targeted axis. Use the x and y data provided and the Axes.plot() command to create a lineplot 
on the ax object from problem 1. Then call plt.show() to see your figure
"""

# your code here

"""
3. Setting properties

In the lecture, we used functions like plt.title() and plt.xlabel() to add additional content to our plots. The 
equivalent Axes methods usually has "set_" prepended, such as Axes.set_title(), axes.set_xlabel(), et cetera. 
Alternatively, if we want to set a bunch of these properties at once, we can instead use the Axes.set() method. 
For example, ax.set(title='my_title', xlabel='my_xlabel', xlim=(0,10)) would set the title, xlabel, and xlim (x min and
x max) simultaneously. Using either Axes.set_* methods, or the Axes.set() method, and the ax object from the previous 
problem, set the following:

title = 'wiggly plot'
xlim = (0, 6)
ylim = (-3, 3)
xlabel = 'x'
ylabel = 'y' 

You may need to move your plt.show() command from the previous problem to the end of the code you write for this
problem. 
"""

# your code here

"""
4. Updating

Matplotlib ships with a full animation API in the matplotlib.annotation package. Unfortunately, this package can be
tricky to use for beginners. One way to "fake it til you make it" with animations is to just repeatedly generate a 
plot, wait briefly, and then generate an updated plot. One of the smoothest ways to do this is with the update_data()
method, which most of matplotlib's Artist type classes will have. For now, don't worry too much about what an Artist 
type class is, just know that its the kind of object returned by function like plt.plot() and plt.matshow(), and 
methods like Axes.plot() and Axes.matshow(). So in the following line of code:

art_obj = ax.plot(x, y)

art_obj would be an Artist-type object with a set_data() method. Because this is a new concept, the code below is 
implemented for you, but I still recommend you walk yourself through it line by line. Uncomment the below lines when
you are ready (highlighting the whole block of code and pressing "cmd + /" or "ctrl + /" will uncomment it in many
development environments)
"""

# # close out any existing plots
# plt.close('all')
#
# # create a new fig and ax
# fig, ax = plt.subplots()
#
# # generate some initial data, in this case a 20x20 array
# arr = np.arange(400).reshape(20, 20)
#
# # plot the initial data, and hold onto the returned Artist object
# art_obj = ax.matshow(arr)
#
# # use a for loop to step through the frames of the animation
# for i in range(400):
#     # wait for a fraction of a second. Larger values will result in a slower animation
#     plt.pause(0.05)
#     # update the array however you want. For this example, I rolled the array by 1.
#     arr = np.roll(arr, 1)
#     # update the Artist Object with the new data
#     art_obj.set_data(arr)
#     # force matplotlib to redraw the figure so it realizes the Artist object was modified
#     plt.draw()








