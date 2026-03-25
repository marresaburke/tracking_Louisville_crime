import pandas as pd 
from pypdf import PdfReader

five_yr_crime_data = PdfReader('TeenCrimes5yrs.pdf')
print(f"Total pages: {len(five_yr_crime_data)}")

print(five_yr_crime_data)


