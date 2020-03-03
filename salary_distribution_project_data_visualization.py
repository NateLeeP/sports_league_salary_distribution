# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 06:09:00 2019

@author: Nate P
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats
pd.options.display.float_format = '{:.2f}'.format
pd.set_option('display.max_columns', 10)
salary_df = pd.read_csv('salary_data.csv')

""" Boxplot 

fig, ax = plt.subplots()

ax.boxplot([salary_df[salary_df.League == 'MLB'].Salary.dropna(),
            salary_df[salary_df.League == 'NFL'].Salary,
            salary_df[salary_df.League == 'NBA'].Salary, 
            salary_df[salary_df.League == 'NHL'].Salary], 
            labels = ['MLB','NFL','NBA','NHL'])
ax.set_ylabel('Salary')
ax.set_title('Salary Distributions across major four sports leagues')
ax.set_yticks([10000000,20000000,30000000])
ax.set_yticklabels(['$10,000,000','$20,000,000','$30,000,000'])
ax.set_xlabel('Sports League')
"""
#$ax.ticklabel_format(axis = 'y',style = 'plain') Format to be numeric if do not want scientific. Instance method ax.set_yticklabels is better

""" Is it possible to convert int to dollars on boxplot? """

""" Can you format an entire series? Probably with apply """
#print(salary_df.groupby('League').get_group('MLB').describe().apply(lambda x: ('${:,.2f}').format(x)), axis = 0)

""" How do I return the max and include player name? Aggregating max returns the max of that object """


def gini(array):
    """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq: http://www.statsdirect.com/help/content/image/stat0206_wmf.gif
    # from: http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    array = array.flatten() #all values are treated equally, arrays must be 1d
    if np.amin(array) < 0:
        array -= np.amin(array) #values cannot be negative
    array += 0.0000001 #values cannot be 0
    array = np.sort(array) #values must be sorted
    index = np.arange(1,array.shape[0]+1) #index per array element
    n = array.shape[0]#number of array elements
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array))) #Gini coefficient


""" Plotting a Lorenz Curve. NFL """

'''
def lorenz_curve(salary_df, league):
    salary_array = np.array(salary_df[salary_df['League'] == league].Salary.dropna())
    x_values = np.linspace(0,1,21)
    y_values = []
    for salary in np.quantile(salary_array, x_values):
        income_percent = (salary_array[salary_array <= salary].sum()) / (salary_array.sum())
        y_values.append(income_percent)
    plt.plot(x_values, np.array(y_values), label = league)
    return y_values


for league in salary_df['League'].unique():
    lorenz_curve(salary_df, league)
    
    
    
    
plt.plot(np.linspace(0,1,21),np.linspace(0,1,21), label = 'Equality')
plt.legend()
plt.xlim(0,1)
plt.ylim(0,1)
'''

nhl_income_percent = []
nhl_salary_array = salary_df[salary_df['League'] == 'NHL'].Salary.dropna()
for salary in np.unique(np.quantile(nhl_salary_array, np.linspace(0,1,11))):
    income_percent = (nhl_salary_array[nhl_salary_array <= salary].sum()) / (nhl_salary_array.sum())
    nhl_income_percent.append(income_percent)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    