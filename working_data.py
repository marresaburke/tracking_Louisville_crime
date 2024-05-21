import pandas as pd

teen_data = pd.read_csv('teen_crimes_edit.csv')
teen_data

teen_data.columns

date = teen_data['Date']
date.describe()
date.value_counts()