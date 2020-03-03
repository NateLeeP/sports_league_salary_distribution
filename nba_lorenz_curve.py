# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 05:47:29 2019

@author: Nate P
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

salary_df = pd.read_csv('salary_data.csv')

nba_salary = salary_df[salary_df['League'] == 'NBA'].sort_values(by = 'Salary', ascending = True) ### Looking at only NBA players
n_players = len(nba_salary) ### Number of NBA players
p_income = np.linspace(0,1,101) ### income percentages, 0% to 100%
nba_total_salary = nba_salary['Salary'].sum()
nba_cum_sum = np.cumsum(nba_salary['Salary']).reset_index().drop(columns = 'index') ### Vector of the Cum Sum

nba_cum_sum[(nba_cum_sum['Salary'] < (.5 * nba_total_salary))] ### Boolean that returns all cum_sum values less than 50% of income. How many players are below this value?

p_players = [len(nba_cum_sum[(nba_cum_sum['Salary'] < (p * nba_total_salary))]) / n_players for p in p_income]

plt.plot(p_players, p_income)


def plot_lorenz_curve(league_salaries, league):
    n_players = len(league_salaries) ### Number of players in selected league
    p_income = np.linspace(0,1,101) ### Income percentages, 0% to 100%
    sorted_salary = league_salaries.sort_values(by = 'Salary', ascending = True)
    total_salary = league_salaries['Salary'].sum()
    cum_sum = np.cumsum(league_salaries['Salary']).reset_index().drop(columns = 'index') ##cumulative sum of salaries
    p_players = [len(league_salaries[(league_salaries['Salary'] < (p * total_salary))]) / n_players for p in p_income]
    
    plt.plot(p_players, p_income)