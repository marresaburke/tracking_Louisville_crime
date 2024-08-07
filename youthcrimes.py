import pandas as pd
import numpy as np
from datetime import datetime

#Loading in Data 
teen_data = pd.read_csv('LMPD_CleanedData_YouthCrimeFull_2023-2024.csv')
teen_data.set_index('Date')
teen_data = teen_data.drop(columns=['Charges Sequence #', 'Arrest #']) #Remove unwanted info

guns_demographics = pd.read_csv('LMPD_JuvenilesWithGunsClean_Jan23-Dec23.csv')
guns_demographics = guns_demographics.drop(columns=['Agency Name', 'Gender', 'Race', 'Ethnicity', 'Charges Classification','Arrest Type']) #Remove unwanted info
#Cleaning/Sorting data by dates 

month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',7:'July',8:'August',9:'September',  10:'October',11:'November',12:'December'}

teen_date_values = pd.DatetimeIndex(teen_data["Date"]) #convert Date column
teen_data['Year'] = teen_date_values.year #seperate the year
teen_data['Month'] = teen_date_values.month #seperate the month 
teen_data['Month'] = teen_data['Month'].map(month_dict) #applying month dictionary to column

gun_date_values = pd.DatetimeIndex(guns_demographics['Date']) #convert gun Date column

guns_demographics['Year'] = gun_date_values.year #separate the year 
guns_demographics['Month'] = gun_date_values.month #seperate the month 

guns_demographics['Month'] = guns_demographics['Month'].map(month_dict) #applying month dictionary to column


#sorted by date range
dates_teen_full_df = teen_data[(teen_data['Date'] > '2023-01-01') & (teen_data['Date'] < '2023-12-31')]
dates_gun_full_df = guns_demographics[(guns_demographics['Date'] > '2023-01-01') & (guns_demographics['Date'] < '2023-12-31')]

#Sort crimes by months to build dataframes to merge
list_of_months = ['January', 'February', 'March','April','May', 'June','July','August', 'September', 'October','November', 'December']

crimes_per_month = dates_teen_full_df.Month.value_counts() #how many teens arrested for serious crimes each month
crimes_per_month.index = pd.CategoricalIndex(crimes_per_month.index, categories=list_of_months, ordered=True)
crimes_per_month = crimes_per_month.sort_index()
total_crime_final = pd.DataFrame({'Total Teen Arrests': crimes_per_month})

guns_per_month = dates_gun_full_df.Month.value_counts() #how many teens arrested for gun possession charges
guns_per_month.index = pd.CategoricalIndex(guns_per_month.index, categories=list_of_months, ordered=True)
guns_per_month= guns_per_month.sort_index()
gun_final = pd.DataFrame({'Gun Possession Charges': guns_per_month})
final = pd.merge(total_crime_final, gun_final, on='Month')

final.to_csv('Teen_crimes_comparison.csv')


 
