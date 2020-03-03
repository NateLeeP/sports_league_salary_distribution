# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:27:55 2019

@author: Nate P
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

salary_df = pd.read_csv('salary_data.csv')

""" Create Salary Arrays """
# Not sure how do create variable names with for loop. 

nfl_salary_array = np.array(salary_df[salary_df['League'] == 'NFL'].Salary)
mlb_salary_array = np.array(salary_df[salary_df['League'] == 'MLB'].Salary.dropna())
nba_salary_array = np.array(salary_df[salary_df['League'] == 'NBA'].Salary)
nhl_salary_array = np.array(salary_df[salary_df['League'] == 'NHL'].Salary)

salary_arrays = [nfl_salary_array,mlb_salary_array,nba_salary_array,nhl_salary_array]
fig, ax = plt.subplots()
def plot_lorenz_curve(array):
    p_income = np.linspace(0,1,101) ## Income %, 0 to 100
    sorted_array = array.sort()
    n_players = len(array) ### Number of players
    total_salary = array.sum() ## Total salary in the array
    cum_sum = np.cumsum(array) ###cum sum of array 
    p_players = [len(cum_sum[(cum_sum['Salary'] < (p * total_salary))]) / n_players for p in p_income]
    ax.plot(p_players, p_income)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    plt.show()
""" Having trouble with inplace method, can't seem to loop and add on     
salary_arrays_zero_added = []
for array in salary_arrays:
    array = np.append(array, 0)
    salary_arrays_zero_added.append(array)
    
"""

nfl_salary_array_zero = np.append(nfl_salary_array, 0)
mlb_salary_array_zero = np.append(mlb_salary_array, 0)
nba_salary_array_zero = np.append(nba_salary_array, 0)
nhl_salary_array_zero = np.append(nhl_salary_array, 0)

salary_array_zero = [nfl_salary_array_zero, mlb_salary_array_zero, nba_salary_array_zero,nhl_salary_array_zero]

