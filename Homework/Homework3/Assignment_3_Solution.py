"""
Assignment 3: Pandas Practice
Sarth Diskalkar

This assignment was created by Tucker J Lancaster

About this template: For this assignment, we have broken your overall goal into a series of smaller functions that,
when completed, can be used in sequence to get the desired output. Before you start writing code, look towards the
bottom of this template at the section starting with "if __name__ == 'main':". In python, code within this kind of
special if statement will only run when the script is executed from the command line (and not, for example, if you
import a function from this script into another script). This time, we have filled in this section for you, and you
can use it to help understand how the functions you write will come together to form a completed pipeline. In many
of the functions, you will see variables set to the string "replace this string with code". This is just to make
sure the script will run even if you have only implemented some of the functions. As the string suggests, you should
replace it with code. Feel free also to add additional lines of code above or below this placeholder.
"""

import argparse
import pandas

"""
Part I: Write a function that uses argparse to define the two positional arguments (InputFile and OutputFile) expected 
by this script. The code you put in this function will look exactly like the argparse code you've written outside of 
functions, the only difference being that you will return the args variable (containing the parsed arguments) from this
function. Note that this function is intentionally constructed without input arguments, hence the empty parentheses when
we first define it
"""


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('InputFile', type=str, help='Input file')
    parser.add_argument('OutputFile', type=str, help='Output file')
    args = parser.parse_args()
    return args


"""
Part II: Write a function that reads in the data from input file (SampleData.xlsx, in this case) and returns two 
Dataframes: one called dt_well, containing the contents of the "WellData" sheet, and one called dt_dictionary,
containing the contents of the "Dictionary" sheet. Note that the use of the word dictionary here has nothing to do
with the object of the same name in python -- i.e., dt_dictionary should be a DataFrame read directly from the excel
file, not a dictionary.
"""


def read_data(input_file):
    dt_well = pandas.read_excel(input_file, sheet_name='WellData')
    dt_dictionary = pandas.read_excel(input_file, sheet_name='Dictionary')
    return dt_well, dt_dictionary


"""
Part III: Write a function that takes in dt_well (the first output from read_data), and returns a new DataFrame with 
same information rearranged, as well as a new column called "Ratio" containing the relative abundance of Ch2Unknown.
The first few rows of your output should match the DataFrame fragment shown below. With careful use of pandas methods, 
this function can be correctly implemented in two lines of code.

 Well TargetType_x  Concentration_x TargetType_y  Concentration_y     Ratio
0   A01   Ch1Unknown            941.0   Ch2Unknown           207.00  0.180314
1   A02   Ch1Unknown           1709.0   Ch2Unknown            43.10  0.024599
2   A03   Ch1Unknown           1468.0   Ch2Unknown           117.00  0.073817
3   A04   Ch1Unknown           1242.0   Ch2Unknown           229.00  0.155676
4   A05   Ch1Unknown            951.0   Ch2Unknown           193.00  0.168706
"""


def calculate_ratio(dt_well):
    dt_well_ch1 = dt_well.loc[dt_well['TargetType']=='Ch1Unknown'] 
    dt_well_ch2 = dt_well.loc[dt_well['TargetType']=='Ch2Unknown']  
    dt_well_sl = pandas.merge(dt_well_ch1, dt_well_ch2, on='Well')
    dt_well_sl['Ratio'] = dt_well_sl['Concentration_y'] / (dt_well_sl['Concentration_x'] + dt_well_sl['Concentration_y'])

    return dt_well_sl


"""
Part IV: Write a function called master_merge that takes in dt_dictionary and dt_well_sl, and merges them into a single
master table called dt_master. Compare the first few lines of your output with the DataFrame fragment below. With 
careful use of pandas, this function can be completed by adding a single line of code.

Well Strain1 Strain2  Replicate  Time Point TargetType_x  Concentration_x TargetType_y  Concentration_y     Ratio
0  A01      N2   nurf1          1           2   Ch1Unknown            941.0   Ch2Unknown            207.0  0.180314
1  A05      N2   nurf1          2           2   Ch1Unknown            951.0   Ch2Unknown            193.0  0.168706
2  B01      N2   nurf1          1           4   Ch1Unknown           1944.0   Ch2Unknown             96.0  0.047059
3  B05      N2   nurf1          2           4   Ch1Unknown           2074.0   Ch2Unknown             93.0  0.042916
"""


def master_merge(dt_dictionary, dt_well_sl):
    dt_master = dt_dictionary.merge(dt_well_sl, on='Well')
    return dt_master


"""
Part V: Write a function that takes in dt_master, and returns a DataFrame pivoted on the Time Point column. Check your
output against the "All_Data" page of the provided "OutputData.xlsx" file. This function can be implemented in a single 
line.
"""


def pivot(dt_master):
    dt_output1 = pandas.pivot(dt_master, index=['Strain1','Strain2','Replicate'], columns='Time Point', values='Ratio')
    return dt_output1


"""
Part VI: Write a function that takes in dt_output1, and returns a DataFrame matching the Average_data page of the 
provided OutputData.xlsx file. The numerical values in this DataFrame represent the averaged ratios, across all 18
replicates, at each of the three time points. 
"""


def strain_avg(dt_output1):
    dt_output2 = dt_output1.groupby(['Strain1','Strain2'])[[2,4,6]].mean()
    return dt_output2


"""
Part VII: write a function that takes in an output file name, dt_output1, and dt_output2, and writes the two DataFrames
to the provided output file, with dt_outpu1 on a page named 'All_data', and dt_output2 on a page called 'Average_data',
just like in the provided OutputData.xlsx file. When you are ready to write this function, replace the "pass" statement
with your own code.
"""


def write_data(output_file, dt_output1, dt_output2):
    dt_output1.to_excel(output_file, sheet_name='All_data')
    dt_output2.to_excel(output_file, sheet_name='Average_data')


"""
Execution code. Refrain from adding any code here, but feel free to comment out portions while developing your code
"""
if __name__ == '__main__':
    args = parse_args()
    dt_well, dt_dictionary = read_data(args.InputFile)
    dt_well_sl = calculate_ratio(dt_well)
    dt_master = master_merge(dt_dictionary, dt_well_sl)
    dt_output1 = pivot(dt_master)
    dt_output2 = strain_avg(dt_output1)
    write_data(args.OutputFile, dt_output1, dt_output2)
