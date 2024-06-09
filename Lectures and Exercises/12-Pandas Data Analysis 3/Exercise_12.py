"""
Exercise 12: Pandas III

"""

import pandas as pd
from time import time

"""
Intro: 
Below is a function called simulation_step (already fully implemented) that can be used 
to simulate a simple Lotka-Voltera predator prey model. The function takes in a dictionary with the keys "pred_pop"
and "prey_pop", corresponding to the current predator and prey populations, and returns a similar dictionary, but with
the updated predator and prey populations after a single step of the simulation. For explanation of the "parameter"
variable, see the block comment within the simulation_step() function below. By repeatedly calling this function,
and passing its output back to the function as "state", you can build up the predator-prey population dynamics 
iteratively. Model loosely adapted from :
https://www.digitalbiologist.com/blog/2018/9/a-population-dynamics-model-in-five-lines-of-python,
"""

default_parameters = {'pred_birth_rate': 0.015, 'prey_birth_rate': 0.5, 'pred_death_rate': 0.5,
                      'prey_death_rate': 0.015, 'dt': 0.01, 'n_steps': 5000, 'pred_pop_init': 10,
                      'prey_pop_init': 100}


def simulation_step(state, parameters):
    """takes in a state dictionary with the keys "pred_pop" and "prey_pop" containing the current predator and prey
    populations, and returns a dictionary with the same keys, but the predator and prey populations after a single
    step of the simulation. Also expects a dictionary called parameters, with the the following structure:
    parameters = {'pred_birth_rate': float_value, 'prey_birth_rate': float_value, 'pred_death_rate': float_value,
                  'prey_death_rate': float_value, 'dt': float_value, 'n_steps': int_value, 'pred_pop_init': int_value,
                  'prey_pop_init': int_value}
    where dt is the time step, n_steps the number of iterations being run, and pred_pop_init and prey_pop_init the
    initial populations of predator and prey respectively.
    """
    p = parameters
    # update prey population
    delta_prey = p['dt'] * (p['prey_birth_rate'] * state['prey_pop'] - p['prey_death_rate'] * state['prey_pop'] * state['pred_pop'])
    new_prey_pop = state['prey_pop'] + delta_prey

    # update predator population
    delta_pred = p['dt'] * (p['pred_birth_rate'] * state['prey_pop'] * state['pred_pop'] - p['pred_death_rate'] * state['pred_pop'])
    new_pred_pop = state['pred_pop'] + delta_pred

    # return updated values
    return {'t': state['t'] + p['dt'], 'pred_pop': new_pred_pop, 'prey_pop': new_prey_pop}


"""
1. Sometimes, we want to use a dataframe to hold information we are generating at runtime, rather than data that we read 
in from a csv or other source. For this exercise, you will use the above function and a for-loop to iteratively
calculate the predator and prey populations over time. Ultimately, we want to end up with a dataframe containing three
columns: "t", corresponding to the time, "pred_pop", corresponding to the predator population at each time step, 
and "prey_pop", corresponding to they prey population at each time step. Complete the below function achieve this
using the pandas.DataFrame.append method. You will likely need to set the "ignore_index" keyword argument of append to 
True. Also note that append does not operate in-place by default. For explanation of the parameters dictionary, read
the comment in the simulation_step function. If you want to use the default parameters, simply pass the pre-defined
default_parameters dictionary to this function
append documentaiton: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.append.html
"""

def run_simulation_v1(parameters):
    curr_state = {'t': 0, 'pred_pop': parameters['pred_pop_init'], 'prey_pop': parameters['prey_pop_init']}
    df = pd.DataFrame([curr_state])

    # your code here

    return df

"""
2. While the append method is convenient, it gets pretty inefficient for large dataframes. This has to do with how 
pandas allocated memory. Appending to a list, however, is extremely efficient in python, and we can use this to
optimize our dataframe creation. Check out this article on using lists of dictionaries to generate a DataFrame, 
then modify your function from part 1 to use this approach instead of the append method.

https://www.geeksforgeeks.org/create-a-pandas-dataframe-from-list-of-dicts/
"""


def run_simulation_v2(parameters):
    states = [{'t': 0, 'pred_pop': parameters['pred_pop_init'], 'prey_pop': parameters['prey_pop_init']}]

    # your code here

    df = pd.DataFrame(states)
    return df

"""
3. Now uncomment the below lines of code to compare the efficiency of the two methods
"""
# n_steps = 1000
#
# start = time()
# df1 = run_simulation_v1(default_parameters)
# v1_runtime = time() - start
# print('unoptimized: {:.5f} seconds'.format(v1_runtime))
#
# start = time()
# df2 = run_simulation_v2(default_parameters)
# v2_runtime = time() - start
# print('optimized: {:.5f} seconds'.format(v2_runtime))
#
# print('optimized version is {:.2f}x faster'.format(v1_runtime/v2_runtime))
#
# print(f'dataframe contents are identical: {all(df2==df1)}')

"""
4. Using your run_simulation_v2 function, create two dataframes: the first, df_1, should use all default parameter
values. The second, df_2, should use default parameter values EXCEPT for dt, which you should set to 0.04, and n_steps,
which you should set to 1250. Be careful not to modify the original default parameter dictionary by mistake. The 
dict.copy() method may be useful to avoid this.
"""

# your code here

"""
5. merge df_1 and df_2 into a dataframe called df_3 that looks like this:

          t  pred_pop_x  prey_pop_x  pred_pop_y  prey_pop_y
0      0.00   10.000000  100.000000   10.000000  100.000000
1      0.01   10.100000  100.350000         NaN         NaN
2      0.02   10.201530  100.699720         NaN         NaN
3      0.03   10.304616  101.049125         NaN         NaN
4      0.04   10.409284  101.398179   10.400000  101.400000
     ...         ...         ...         ...         ...
4995  49.95  127.772850   50.026212         NaN         NaN
4996  49.96  128.092785   49.317544    6.223803  119.082105

due to accumulation of floating point errors, you will need to round the values in the 't' column of df_1 and df_2
before merging. To see why, compare list(df_1.t) and list(df_2.t). The easiest way to do this is to just replace df['t']
in each DataFrame with df['t'].round(x) before merging, where x is the number of decimals you want to round to. 
For this exercise, use x=2. 

round documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html
merge documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
"""

# your code here

"""
6. Add two new columns to df_3. Call the first 'pred_error', and populate it with the difference between pred_pop_y
and pred_pop_x for each row. Call the second new column 'prey_error', and populate it with the difference between 
prey_pop_y and prey_pop_x. This stack exchange post might give you a clue about how to do this without using any
fancy pandas methods:

https://stackoverflow.com/questions/36619631/how-to-divide-two-columns-element-wise-in-a-pandas-dataframe

Your finished dataframe should look like this:

          t  pred_pop_x  prey_pop_x  ...  prey_pop_y  pred_error  prey_error
0      0.00   10.000000  100.000000  ...  100.000000    0.000000    0.000000
1      0.01   10.100000  100.350000  ...         NaN         NaN         NaN
2      0.02   10.201530  100.699720  ...         NaN         NaN         NaN
3      0.03   10.304616  101.049125  ...         NaN         NaN         NaN
4      0.04   10.409284  101.398179  ...  101.400000   -0.009284    0.001821
     ...         ...         ...  ...         ...         ...         ...
"""

# your code here

"""
7. Now the DataFrame.abs() and DataFrame.mean() methods together to find the average absolute errors (i.e., the average
of the absolute value of the numbers in the pred_error and prey error, respectively.). Print these values and confirm
they match the ones below:

avg abs pred pop error: 10.438318836020711
avg abs prey pop error: 12.266723660151104
"""

# your code here

"""
8. You have finished the coding portion of this exercise, but if you want to visualize the data you've produced 
(and see another reason why pandas can be so useful) install the seaborn (using pip install seaborn or conda install 
seaborn), uncomment the code below, and rerun your script. matplotlib should install automatically with seaborn, but 
if it does not run "conda install matplotlib" or "pip install matplotlib". Can you see how cumulative errors affected 
your  simulation when you increased the timestep from 0.01 to 0.04? How do the results change if you use dt=0.01 for
both simulations, but adjust one of the other parameters?
"""

# import seaborn as sns
# import matplotlib.pyplot as plt
# from matplotlib import gridspec
#
# fig = plt.figure()
# spec = gridspec.GridSpec(ncols=1, nrows=2, height_ratios=[4, 1])
# ax0 = fig.add_subplot(spec[0])
# ax1 = fig.add_subplot(spec[1])
# df_tmp = df_3[['t', 'pred_pop_x', 'pred_pop_y', 'prey_pop_x', 'prey_pop_y']].melt(id_vars=['t']).dropna()
# err_vars = ['t', 'pred_error', 'prey_error']
# sns.lineplot(data=df_tmp, x='t', y='value', hue='variable', ax=ax0)
# df_tmp = df_3[['t', 'pred_error', 'prey_error']].melt(id_vars=['t']).dropna()
# sns.lineplot(data=df_tmp, x='t', y='value', hue='variable', ax=ax1)

