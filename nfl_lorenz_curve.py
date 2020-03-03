# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:10:57 2019

@author: Nate P
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

salary_df = pd.read_csv('salary_data.csv')
""" US Inequality Information
Cleaning data. Fixing cumulative sum value for Top 5. Converting 2018 Cum Sum from a percent to a decimal.

 """ 
us_inequality_df = pd.read_csv('us_income_inequality_2018_data.csv',index_col = 0)
us_inequality_df.loc['Top 5', '2018_Estimate_CumSum'] = 1 - .235
us_inequality_df['2018_Estimate_CumSum_Decimal'] = us_inequality_df['2018_Estimate_CumSum'] / 100

nfl_salary = np.array(salary_df[salary_df['League'] == 'NFL'].Salary)
mlb_salary = np.append(np.array(salary_df[salary_df['League'] == 'MLB'].Salary.dropna()), 0)
nba_salary = np.append(np.array(salary_df[salary_df['League'] == 'NBA'].Salary), 0)
nhl_salary = np.append(np.array(salary_df[salary_df['League'] == 'NHL'].Salary),0)



x_values = np.linspace(0,1,11)
y_values = [(nfl_salary[nfl_salary <= np.quantile(nfl_salary, x)].sum()) / (nfl_salary.sum()) for x in x_values]

''' Gini function courtesy  https://github.com/oliviaguest/gini '''
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


fig, ax = plt.subplots()

ax.plot(x_values, y_values, linestyle = '-.', color = 'b', label = 'NFL')
ax.plot(x_values,[(mlb_salary[mlb_salary <= np.quantile(mlb_salary, x)].sum()) / (mlb_salary.sum()) for x in x_values], linestyle = '-',
                  color = 'b', label = 'MLB')
ax.plot(x_values,[(nba_salary[nba_salary <= np.quantile(nba_salary, x)].sum()) / (nba_salary.sum()) for x in x_values], linestyle = '--',
                  color = 'b', label = 'NBA')
ax.plot(x_values,[(nhl_salary[nhl_salary <= np.quantile(nhl_salary, x)].sum()) / (nhl_salary.sum()) for x in x_values], linestyle = ':',
                  color = 'b', label = 'NHL')
ax.plot(np.linspace(0,1,11),np.linspace(0,1,11), color = 'black')

""" Plotting US income inequality """
ax.plot(np.sort(np.append(us_inequality_df['Quantile'],0)), np.sort(np.append(us_inequality_df['2018_Estimate_CumSum_Decimal'],0)), color = 'red', label = 'USA')

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_ylabel('% of Income')
ax.set_xlabel('% of Players')
ax.set_xticks([0,.2,.4,.6,.8,1])
ax.set_xticklabels(['0%','','','','','100%'])
ax.set_yticks([0,.2,.4,.6,.8,1])
ax.set_yticklabels(['0%','','','','','100%'])
ax.annotate('NFL Gini Coefficient: ' + str(np.round(gini(nfl_salary), 3)), xy = [.01,.6])
ax.annotate('MLB Gini Coefficient: ' + str(np.round(gini(mlb_salary),3)), xy = [.01,.55])
ax.annotate('NBA Gini Coefficient: ' + str(np.round(gini(nba_salary),3)), xy = [.01, .50])
ax.annotate('NHL Gini Coefficient: ' + str(np.round(gini(nhl_salary),3)), xy = [.01,.45])
#ax.annotate('Lorenz Curve is a visual depiction of inequality. The more bowed the curve, the greater the inequality. The straight line represents perfect equality',
#             xy = [50,15], xycoords = 'figure points', fontsize = 8)
ax.legend(loc = 'upper left')
ax.set_title('Share of Income vs Share of Players', fontsize= 10)
fig.suptitle('Lorenz Curve in United States Major Sports Leagues')
fig.savefig('Major Sports Leagues Lorenz Curve.png')





