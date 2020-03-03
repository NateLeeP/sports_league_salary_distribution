# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:25:49 2019

@author: Nate P
"""
""" This code generates the lorenz curve figure for the four major sports leagues. """


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from lorenz_curve_functions import lorenz_curve_values

salary_df = pd.read_csv('salary_data.csv')

fig, ax = plt.subplots()

### Extracting the values for plotting
nba_values = lorenz_curve_values(salary_df, 'NBA')
nfl_values = lorenz_curve_values(salary_df, 'NFL')
mlb_values = lorenz_curve_values(salary_df, 'MLB')
nhl_values = lorenz_curve_values(salary_df, 'NHL')

### Plotting each lorenz curve on the same plot
ax.plot(nba_values[0], nba_values[1], color = 'blue', linestyle = '--', label = 'NBA')
ax.plot(nfl_values[0], nfl_values[1], color = 'blue', linestyle = '-', label = 'NFL')
ax.plot(nhl_values[0], nhl_values[1], color = 'blue', linestyle = '-.', label = 'NHL')
ax.plot(mlb_values[0], mlb_values[1], color = 'blue', linestyle = ':', label = 'MLB')

### Line of perfect equality
ax.plot(np.linspace(0,1,101), np.linspace(0,1,101), color = 'black') 

### Chart characteristics
fig.suptitle('Lorenz Curves of the Four Major U.S. Sports Leagues')
fig.text(0.55, -.01, 
         'Lorenz curve visualizes income inequality. The more bowed away from the line of perfect equality, the more inequal the income distribution', 
         fontsize = 9,
         ha = 'center')
fig.set_size_inches(7,5)
ax.legend()
ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.set_xticklabels(['0%','20%','40%','60%','80%','100%']); ax.set_yticklabels(['0%','20%','40%','60%','80%','100%'])
ax.set_xlabel('% of Population'); ax.set_ylabel('% of Income Owned')
ax.set_title('Percent of Population vs Percent of Income')

fig.savefig('Lorenz Curve V2.0.png', bbox_inches = 'tight')