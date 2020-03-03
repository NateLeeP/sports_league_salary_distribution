# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 06:08:33 2019

@author: Nate P
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

salary_df = pd.read_csv('salary_data.csv')

""" How many players from each league? """


""" Gini Coeffecient. Taken from github.com/oliviaguest/gini """

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

nfl_salary_array = np.array(salary_df[salary_df['League'] == 'NFL'].Salary.dropna())
nfl_salary_array[:5]