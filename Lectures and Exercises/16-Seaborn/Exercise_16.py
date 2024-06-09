"""
Exercise 16: Basic Plotting with Seaborn

note that plt.show() commands are not included in this script by default. Depending on your coding environment,
you may need to add these after plotting commands that you want to visualize.
"""

import seaborn as sns
import matplotlib.pyplot as plt

"""
1. Import the penguins dataset included with seaborn as a pandas DataFrame. Use DataFrame functions and methods you 
already know (df.head(), df.describe(), df.info(), etc.) to get a feel for the data
"""

df = sns.load_dataset('penguins')

"""
2a. For this question, you will build up a progressively more complicated figure by adding additional keyword arguments
to the sns.replot command. First, use relplot to generate a scatterplot of 'bill_length_mm' vs. 'bill_depth_mm'.
"""



"""
2b. Rewrite your command from part a, but this time use the hue keyword to color the points by species
"""



"""
2c. Now rewrite your command from 2b, and use the "col" keyword to plot side-by-side scatterplots of the data 
separated by sex. Color your points by species, as in part b.
"""



"""
2d. Again, update your code from the previous portion. Use the row keyword to separate the the data into three rows 
of plots based on the island where the observation occurred
"""



"""
2e. Now use the size keyword to set the point size according to the body mass of each penguin. Your final figure should
have six subplots (arranged in three rows and two columns) with all data points colored by species and sized by body
mass
"""



"""
use the plt.savefig command to save your final figure as "penguin_scatters.pdf"
"""



"""
3a. As in question two, we again start with a simple seaborn plot and build it up into a more complicated figure.
Begin by generating a simple histogram showing the distribution of flipper lengths. Use the sns.displot command.
"""



"""
3b. Use the hue keyword to separate the histogram by species 

"""



"""
3c. Use the rug keyword to add a rugplot to the x axis
"""



"""
3d. Now use the "kind" keyword to change your histograms to kernel density estimate (kde) plots
"""



"""
3e. Using the "palette" keyword, change the colormap to 'rainbow'
"""



"""
3f. Use the row and col keywords to separate the the columns by sex and the rows by island, as in qeustion 2
"""



"""
3g. Finally, use the plt.savefig command to save your figure as "penguin_kdes.pdf"
"""



"""
4a: Use the sns.pairplot command to generate a pairplot for all variable in the penguins dataset
"""



"""
4b. Color your plot by species
"""



"""
4c. Convert the off-diagonal subplots from scatterplots to kde's
"""



"""
4d. Further customization can be achieved by manually constructing a PairGrid object (the object that underlies the 
pairplot function). This section is completed for you, and included to show you some of the more advanced customization
options you might find useful in creating your own figures. Uncomment to run.
"""
#
# # generate a pairgrid object, with the hue set to species and the data to df. Turn off shared y-axis limits on the
# # diagonal subplots. Set the palette to "colorblind", which is designed to maximize readability for colorblind users.
# # see this page for a visualization of how different palettes appear to people with different variants of colorblindness
# # https://gist.github.com/mwaskom/b35f6ebc2d4b340b4f64a4e28e778486
# g = sns.PairGrid(df, hue='species', diag_sharey=False, palette='colorblind')
# # plot kde's along the diagonal
# g.map_diag(sns.kdeplot)
# # plot scatterplots in the upper triangle. Reduce the point size, remove the outline on the points, and decrease the
# # opacity
# g.map_upper(sns.scatterplot, size=0.25, linewidth=0, alpha=0.5)
# # overlay kdes over the scatterplots in the upper triangle and reduce the opacity
# g.map_upper(sns.kdeplot, levels=4, alpha=0.75)
# # plot 2D histograms on the lower triangle of subplots. Increase the number of bins along each axis to 20, and decrease
# # the opacity
# g.map_lower(sns.histplot, bins=20, alpha=0.5)
# # snag the matplotlib figure object off the PairPlot object, and use it to set the figure title.
# #
# fig = g.fig
# fig.suptitle('Penguins')
# # Use the tight_layout command to fix any overlap between plots, title, etc.
# fig.tight_layout()