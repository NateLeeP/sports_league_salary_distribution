# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 05:57:14 2019

@author: Nate P
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

""" This file returns the x and y values needed to plot the lorenz curve """
def lorenz_curve_values(salary_df, league):
    salary = salary_df[salary_df['League'] == league]['Salary'].sort_values(ascending = True).reset_index().drop(columns = 'index')['Salary'].dropna() #Dataframe only containing salary. 
    ## Inputs for calculating % of population
    salary = salary[salary > 0] ## Ensuring all salary values are above zero
    n_players = len(salary) # Number of players in the league
    cum_sum = np.cumsum(salary) ## Cum sum of league salary 
    total_salary = salary.sum() #### total salary of the league
    p_income = np.linspace(0,1,101) ### percents from 0 to 100
    p_players = [len(cum_sum[cum_sum <= (p * total_salary)]) / n_players for p in p_income]
    
    return p_players, p_income

