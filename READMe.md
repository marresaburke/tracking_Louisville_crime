# Dataset Title: Tracking Louisville Crime

Data Journalist: Marresa Burke (502)379-9365, marresa.burke@wave3.com

## Overview: 
This project analyzes the Louisville Metro Police Department's records for kids aged 13 to 17 who have been arrested for serious crimes such as murder, rape, burgulary, possession of a gun, etc. The findings from this analysis can used as a tool for non-profits and group violence intervention programs target their efforts to specifc age groups, identify trends, and find additional preventative measures. 

File Naming Convention: `Agency_SummarizationOfDataSet_YearRange.csv` This name system where the data came from, general information  the set contains and the time period. 

Some information in the data is privileged/or connected to the department's internal filing system. This project merges two data sets that contain different details about the teens arrests. The cleaning process included searching for blanks, filtering by date, removing unwanted columns, finding totals by month and sorting.  

## Visualization

The data sets show the trends and relationship between gun arrest vs. total of serious crimes like murder, possession of a gun, assault, rape, bugulary, etc. 
https://public.tableau.com/views/TrackingTeenCrimeData/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Instructions: 
1. Make a folder on your computer to store this repo. 
2. Create a virtual environment and install the packages in the `requirements.txt`(instructions below).
3. Clone the repo to your machine in the folder you created in (1).
4. Run the python file. `python3 youthcrimes.py`

## Virtual Environment:
1.  After you've cloned the repository to your computer, navigate to your folder in your Terminal. 
2.  Create a virtual environment in the project folder. `python3 -m venv venv` or `python -m venv venv`
3.  Activate the virtual environment. `source venv/bin/activate` or `source venv/Scripts/activate`
4.  Install the required packages. `pip install -r requirements.txt`
5.  When you are done, deactivate the virtual environment. 




