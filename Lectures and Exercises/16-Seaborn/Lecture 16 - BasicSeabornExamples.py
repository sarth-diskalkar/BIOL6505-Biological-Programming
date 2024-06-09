import seaborn as sns
import matplotlib.pyplot as plt


# Seaborn: a visualization library that works with pandas
# Built on matplotlib
# Designed to read in data from pandas
# Visually appealing palletes 
# Many types of plots: https://seaborn.pydata.org/examples/index.html

# Load dataset that comes with seaborn
df = sns.load_dataset('anscombe')
# Part 1: Basic plotting
# Example 1: basic scatter plot of data
out_fig = sns.scatterplot(data = df, x = 'x', y = 'y')
plt.show()

# Example 2: basic line plot of data with error bars
out_fig = sns.lineplot(data = df, x = 'x', y = 'y')
plt.show()

# Example 3: regression plot of data
out_fig = sns.lmplot(data = df, x = 'x', y = 'y')
plt.show()

# Example 4: 2D histogram
out_fig = sns.jointplot(data = df, x = 'x', y = 'y', kind='hex')
plt.show()

# Part 2: Using hue to separate data into different classes
# Example 1: basic scatter plot of data
out_fig = sns.scatterplot(data = df, x = 'x', y = 'y', hue = 'dataset')
plt.show()

# Example 2: basic line plot of data with error bars
out_fig = sns.lineplot(data = df, x = 'x', y = 'y', hue = 'dataset')
plt.show()

# Example 3: regression plot of data
out_fig = sns.lmplot(data = df, x = 'x', y = 'y', hue = 'dataset')
plt.show()

# Part 3: Separating hues into different graphs

# Example 1: regression plot of data
out_fig = sns.lmplot(data = df, x = 'x', y = 'y', hue = 'dataset', col='dataset')
plt.show()

# Example 2: controlling plot location
out_fig = sns.lmplot(data = df, x = 'x', y = 'y', hue = 'dataset', col='dataset', col_wrap = 2)
plt.show()

# Part 4: Plotting multiple columns against each other
iris = sns.load_dataset("iris")
sns.pairplot(iris)

