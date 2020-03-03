# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:47:45 2019

@author: Nate P
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.options.display.max_columns = 10

""" Cleaning US Income Inequality Spreadsheet """
us_income_inequality = pd.read_excel('US Income Inequality.xls',skiprows = 6)

array = [['Share of Aggregate' for x in range(7)], 
          ['Lowest Quintile','Second Quintile','Third Quintile', 'Fourth Quintile','Fifth Quintile','Highest','Top 5']]
tuples = list(zip(*array))

index = pd.MultiIndex.from_tuples(tuples, names = ['Money Income', 'Quantile'])

us_income_data = pd.read_excel('US Income Inequality.xls', skiprows = 7, usecols = [1,2,3,4,5,6], nrows = 6)

us_income_data.columns = ['2017_Estimate','2017_Margin_of_Error',
                                          '2018_Estimate','2018_Margin_of_Error',
                                          'Percent_Change_Estimate','Percent_Change_Margin_of_Error']
income_2018 = us_income_data['2018_Estimate']

income_2018_cumsum = income_2018.cumsum()

income_2018_data = pd.DataFrame({'2018_Estimate':income_2018, '2018_Estimate_CumSum':income_2018_cumsum})
income_2018_data.index = ['Lowest Quintile','Second Quintile','Third Quintile', 'Fourth Quintile','Highest','Top 5']

income_2018_data['Quantile'] = [.2,.4,.6,.8,1,(.95)]

income_2018_data.to_csv('us_income_inequality_2018_data.csv')