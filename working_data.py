import pandas as pd

teen_data = pd.read_csv('teen_crimes_edit.csv')
teen_data

teen_data.columns

date = teen_data['Date']
date.describe()
date.value_counts().unique()

age = teen_data.Age
age.value_counts()

charges = teen_data.Charges
charges.value_counts()


Age_v_charges = teen_data.groupby('Age')
teen_data.columns


