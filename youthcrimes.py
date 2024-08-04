import pandas as pd
import numpy as np

#Loading in Data 
teen_data = pd.read_csv("/Volumes/MyPassportforMac/Code-Louisville/tracking_Louisville_crime/LMPD_JuvenilesWithGunsClean_Jan23-Dec23.csv")

guns_demographics = pd.read_csv('LMPD_JuvenilesWithGunsClean_Jan23-Dec23.csv', index_col=0)

#Drop redundant or unneed information 
guns_demographics.drop(columns=['Agency Name'])

teen_data.drop(columns=['Charges Sequence #'])




