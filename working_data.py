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





age_char_nums = Age_v_charges.value_counts()

gun_count_data = teen_data.Charges.map(lambda Char: "GUN" in Char).sum()

#num_of_guns = pd.Series([gun_count_data],index = ["gun count"])



