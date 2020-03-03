# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:28:27 2019

@author: Nate P
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
### Clean NFL data

nfl_data = pd.read_csv('nfl_salary_data_unclean.csv')

""" From NFL data we need Player and Avg./Year columns. Need to add 'Sport' column to identify the sport. Remove Pos, Team, and Total Value
    1. Remove Pos, Team, and Total Value
    2. Change name 'Avg./Year' to 'Salary'
    3. Change 'Salary' column to integer
    4. Add 'League' column """
    
""" Remove Post, Team, and Total Value """
nfl_data.drop(['Pos.','Team','Total Value'], axis = 1, inplace = True)

""" Chance name 'Avg./Year' to 'Salary' """
nfl_data.rename(columns = {'Avg./Year':'Salary'}, inplace = True)

""" Change 'Salary' column values to integers """ 
nfl_data['Salary'] = nfl_data['Salary'].apply(lambda x: int(x.replace(',','').strip('$')))

#Should I drop Salary values that are zero?

""" Add 'League' column """
nfl_league = []
for x in range(len(nfl_data)):
    nfl_league.append('NFL')
nfl_data['League'] = nfl_league ## League NFL is a list the length of the dataframe with the string 'NFL' at each index



### Clean MLB data

mlb_data = pd.read_csv('mlb_salary_data_unclean.csv')

""" From MLB data we need Name, Avg Annual column. Need to add 'League' column to identify the League. Remove rank, Team, POS, Salary, Years, Total Value 
    1. Remove rank, Team, POS, Salary, Years, Total Value columns
    2. Change 'Avg Annual' to 'Salary'. Change 'Name' to 'Player'
    3. Change 'Salary' column to integer
    4. Add 'League' column """
    
""" Remove rank, Team, POS, Salary, Years, Total Value columns """
mlb_data.drop(columns = ['rank','Team','POS','Salary','Years','Total Value'], inplace = True)

""" Change name 'Avg Annual' to 'Salary' """
mlb_data.rename(columns = {'Avg Annual':'Salary', 'Name':'Player'}, inplace = True)

""" Change 'Salary' column values to integers """

""" Salary has '$NaN' strings! What to do? Method of converting missing value you know into NaN """
def clean_mlb_salary(salary):
#Function is passed to df.apply. Function cleans salary, but returns a NaN if salary is missing
    if salary == '$NaN':
        return np.nan
    else:
        return int(salary.replace(',','').strip('$'))
mlb_data['Salary'] = mlb_data['Salary'].apply(clean_mlb_salary)

""" Add 'League' Column """
mlb_league = []
for x in range(len(mlb_data)):
    mlb_league.append('MLB')
mlb_data['League'] = mlb_league


### Clean NHL data
nhl_data = pd.read_csv('nhl_salary_data_unclean.csv')

""" From NHL data we need Player, Salary. Need to add 'League' column to identify the League. Remove Cap Hit, Tm. Move 'Player' to front. Change salary to int.
    1. Remove Cap Hit, Tm
    2. Change 'Salary' column to integer
    3. Move 'Player' column to the front
    4. Add 'League' column """

""" Remove Cap Hit, Tm """
nhl_data.drop(columns = ['Cap Hit','Tm'],inplace = True)

""" Change 'Salary' column to integer """
nhl_data['Salary'] = nhl_data['Salary'].apply(lambda x: int(x.replace(',','')))

""" Move 'Player' column to the front """
nhl_data = nhl_data[['Player','Salary']]

""" Add 'League' column """
nhl_league = []
for x in range(len(nhl_data)):
    nhl_league.append('NHL')
nhl_data['League'] = nhl_league


### Clean NBA Data
nba_data = pd.read_csv('nba_salary_data_unclean.csv')

""" From NBA data we need Player, Avg. Salary. Remove Pos, Team, Age, Yrs, Dollars, Guaranteed, % GTD, Free Agent. Fix Player column. Change Salary to int. Add League column
    1. Remove Pos, Team, Age, Yrs, Dollars, Guaranteed, % GTD, Free Agent
    2. Change Avg. Salary column name to Salary
    3. Change Salary to integer
    4. Fix Player column
    5. Add League column """

""" Remove Pos, Team, Age, Yrs, Dollars, Guaranteed, % GTD, Free Agent """
nba_data.drop(columns = ['Pos','Team','Age','Yrs','Dollars','Guaranteed','% GTD','Free Agent'], inplace = True)

""" Change Avg. Salary to Salary """
nba_data.rename(columns = {'Avg. Salary':'Salary'}, inplace = True)

""" Change Salary to integer """
nba_data['Salary'] = nba_data['Salary'].apply(lambda x: int(x.replace(',','').strip('$')))

""" Fix Player Column """
player_pattern = re.compile('[A-Z][a-z]+') ### Matches first and last names

nba_data['Player'] = nba_data['Player'].apply(lambda x: player_pattern.findall(x)[1] + ' ' + player_pattern.findall(x)[0]) ### Find all returns a list of string matches. Indexing list, as in the value at index 1 is the first name, index 0 is last name

""" Add League columm """
nba_league = []
for x in range(len(nba_data)):
    nba_league.append('NBA')
nba_data['League'] = nba_league


""" Concat DataFrames, then save as one csv """

salary_df = pd.concat([nba_data,nfl_data,mlb_data,nhl_data])

salary_df.to_csv('salary_data.csv',index = False)








