# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:52:59 2019

@author: Nate P
"""


import pandas as pd
from bs4 import BeautifulSoup
import requests
""" Collecting NFL data """
nfl_salary_url = 'https://overthecap.com/contracts/'
nfl_requests = requests.get(nfl_salary_url).text
nfl_soup = BeautifulSoup(nfl_requests, 'lxml')

### Retrieve the first four columns
nfl_data = [[td.text for td in tr.findAll('td')[0:5]] for tr in nfl_soup.findAll('tr')[1:len(nfl_soup.findAll('tr'))]]
### Retrieve Table Headers
nfl_data_headers = [th.text for th in nfl_soup.findAll('th')[0:5]]

nfl_data_df = pd.DataFrame(nfl_data, columns = nfl_data_headers)

nfl_data_df.to_csv('nfl_salary_data_unclean.csv',index = False)


""" Collecting the MLB data """
""" MLB Salary will also use Average Annual amount"""
mlb_salary_url = 'https://www.usatoday.com/sports/mlb/salaries/'
mlb_requests = requests.get(mlb_salary_url).text
mlb_soup = BeautifulSoup(mlb_requests, 'lxml')
### Retrieve all columns
mlb_data = [[td.text.strip() for td in tr.findAll('td')] for tr in mlb_soup.findAll('tr')[1:len(mlb_soup.findAll('tr'))]]
### Retrieve Table Headers
mlb_headers = [th.text.strip() for th in mlb_soup.findAll('th')]
### Create data frame
mlb_data_df = pd.DataFrame(mlb_data,columns = mlb_headers)
mlb_data_df.to_csv('mlb_salary_data_unclean.csv', index = False)


""" Collecting NHL Data """
nhl_salary_url = 'https://www.hockey-reference.com/friv/current_nhl_salaries.cgi'
nhl_requests = requests.get(nhl_salary_url).text
nhl_soup = BeautifulSoup(nhl_requests, 'lxml')

nhl_data = [[td.text for td in tr.findAll('td')] for tr in nhl_soup.findAll('tr')[1:len(nhl_soup.findAll('tr'))]]
nhl_data_headers = [th.text for th in nhl_soup.find('tr').findAll('th')]

### Scrape needs adjustment. Why? player names are classified as th. Will create dataframe out of scraped categories, add 'Player' column separately

nhl_data_df = pd.DataFrame(nhl_data, columns = nhl_data_headers[1:])

nhl_data_players = [[th.text for th in tr.findAll('th')] for tr in nhl_soup.findAll('tr')[1:len(nhl_soup.findAll('tr'))]]
### Extract first value from list. Player names were read in as list
nhl_players = pd.Series(nhl_data_players).apply(lambda x: x[0])

nhl_data_df['Player'] = nhl_players

nhl_data_df.to_csv('nhl_salary_data_unclean.csv',index = False)
""" Collecting NBA Data """
nba_salary_url = 'https://www.spotrac.com/nba/contracts/'
nba_requests = requests.get(nba_salary_url).text
nba_soup = BeautifulSoup(nba_requests, 'lxml')

nba_data = [[td.text for td in tr.findAll('td')] for tr in nba_soup.findAll('tr')[1:-2]]
nba_data_headers = [th.text for th in nba_soup.findAll('tr')[0].findAll('th')]

nba_data_df = pd.DataFrame(nba_data, columns = nba_data_headers)

nba_data_df.to_csv('nba_salary_data_unclean.csv', index = False)

