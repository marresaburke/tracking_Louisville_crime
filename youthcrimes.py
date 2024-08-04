import pandas as pd
import numpy as np
from datetime import datetime

#Loading in Data 
teen_data = pd.read_csv("/Volumes/MyPassportforMac/Code-Louisville/tracking_Louisville_crime/LMPD_JuvenilesWithGunsClean_Jan23-Dec23.csv")
teen_data.set_index('Date')

guns_demographics = pd.read_csv('LMPD_JuvenilesWithGunsClean_Jan23-Dec23.csv')
guns_demographics.set_index('Date')
guns_demographics = guns_demographics.drop(columns=['Agency Name']) #Remove LMPD from data 

#Cleaning data by dates 

teen_date_values = pd.DatetimeIndex(teen_data["Date"]) #convert Date column

teen_data['Year'] = teen_date_values.year #seperate the year
teen_data['Month'] = teen_date_values.month #seperate the month 


handgun = ['POSS HANDGUN BY MINOR 1ST OFFENSE 527.100 52206 520','RECEIVING STOLEN PROPERTY (FIREARM) 514.110 28020 280', 'CARRYING A CONCEALED DEADLY WEAPON 527.020 01501 520','POSS HANDGUN BY MINOR 2ND OR > 527.100 52205 520', 'TBUT OR DISP FIREARM 514.030 23100 23H', 'POSSESSION OF HANDGUN BY CONVICTED FELON 527.040 52197 520','UNLAWFUL POSSESSION OF WEAPON ON SCHOOL PROPERTY 527.070 52204 520', 'UNLAWFULLY PROV/PERMIT MINOR TO POSSESS HANDGUN 527.110 52203 520','USING RESTRICTED AMMO DURING A FELONY (NO SHOTS) 527.080(2)(A) 02549 520', 'POSSESSION OF DEFACED FIREARM 527.050 01504 520','POSSESSION OF FIREARM BY CONVICTED FELON 527.040 52196 520']
gun_filter =teen_data[teen_data['Charges'].isin(handgun)]


##Building final dataframe 

#age is rows 
#months is columns 
#data is date and total number of charges vs. gun charges 
 
