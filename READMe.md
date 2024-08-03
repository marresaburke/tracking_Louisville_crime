# Dataset Title: Tracking Louisville Crime

Data Journalist: Marresa Burke (502)379-9365, marresa.burke@wave3.com

## Overview: 
This project analyzes the Louisville Metro Police Department's records for kids aged 13 to 17 who have been arrested for serious crimes such as possession of a gun. The findings from thsi analysis can used as a tool for non-profits and group violence intervention programs to better target their efforts to specifc age groups, identify trends, and find additional preventative measures. 

File Naming Convention: `Agency_SummarizationOfDataSet_YearRange.csv` This name system where the data came from, general information  the set contains and the time period. 

Some information in the date is privileged/or connected to the department's internal filing system. Before I can use my data, I had to define each column, figure out it's relevance for this project and if it's redundant. 

### Dictionary of terms:
- `Date`: Arrest date 
- `Charge`: Crime listed on arrest report 
- `Charge Sequence Number`:  A number that will be either the case number associated with that person's charges, or a unique serial number assigned by the agency. If the agency uses a case number, then the number will change for each new case. If it's a serial/identifying number, it will remain the same.
- `Arrest #`: a way for authorities to track an arrested person
- 

## Instructions: 
1. Make a folder on your computer to store this repo. 
2. Create a virtual environment and install the packages in the `requirements.txt`(instructions below).
3. Clone the repo to your machine in the folder you created in (1).
4. Run the python file. `python3 youthcrimes.py`

## Virtual Environment:
1.  After you've cloned the repository to your computer, navigate to your folder in your Terminal. 
2.  Create a virtual environment in the project folder. `python3 -m venv venv`
3.  Activate the virtual environment. `source venv/bin/activate`
4.  Install the required packages. `pip install -r requirements.txt`
5.  When you are done, deactivate the virtual environment. 




