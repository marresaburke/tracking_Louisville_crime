import pandas as pd

teens_w_guns = pd.read_csv("/Volumes/MyPassportforMac/Code-Louisville/tracking_Louisville_crime/LMPD_JuvenilesWithGunsClean_Jan23-Dec23.csv", index_col = 0)
print(teens_w_guns)


teens_w_guns.columns 

teens_w_guns.Gender.value_counts()


teens_w_guns.Age.value_counts()

teens_w_guns.Gender.value_counts()

teens_w_guns.Race.value_counts()

teens_w_guns.sum

388 + 98 + 2 


teens_w_guns.Ethnicity.value_counts()

461 + 14 + 14

teens_w_guns[teens_w_guns.Ethnicity.isnull()]


teens_w_guns.Age.pop

teens_w_guns.Age.value_counts()

teens_w_guns.Ethnicity.value_counts()

teens_w_guns.shape

teens_w_guns.Charges Names.value_counts