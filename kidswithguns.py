import pandas as pd

teens_w_guns = pd.read_csv("/Volumes/MyPassportforMac/Code-Louisville/tracking_Louisville_crime/LMPD_JuvenilesWithGunsClean_Jan23-Dec23.csv")
print(teens_w_guns)


teens_w_guns.columns

#How many girls were caught with guns? 
Gender_counts = teens_w_guns.Gender.value_counts()
Gender_counts

#How many of each age group? 
age_groups = teens_w_guns.Age.value_counts()
age_groups

#Race breakdown , data that's not there. 
teens_w_guns.Race.value_counts()



teens_w_guns.count()



Ethnicity = teens_w_guns.Ethnicity.value_counts()
Ethnicity

#missing data - replace with missing info 

teens_w_guns[teens_w_guns.Ethnicity.isnull()]

teens_w_guns.Age.describe()

