# 2022Fall_projects

# Project Title - Impact Of Climate Change Across States In USA​


It is known that Climate Change impacts the businesses. On macro level, collectively it impacts the financial performance of industries.​

However, the impact of climate change across states is not uniform.​For example, some states (such as Florida) gets impacted by climate change more than other states.​

We aim to measure the effect of climate changes on economy of states in USA. ​

Moreover, we believe that climate change is not industry agnostic and impacts some industries more than the others.​

Industries such as agriculture, fishing, forestry gets impacted more by climate change than the other industries like Insurance, real estate, retail trade etc. ​

We want to measure the impact of climate change on industries which suffers more impact on climate change. ​
## Steps to Run

Requirements :- API KEY FRED (Request here - https://fred.stlouisfed.org/docs/api/api_key.html)

1. Insert API KEY in variable *FRED_API_KEY* in file streamlit_final.py 
2. Run File streamlit_final.py
3. Run command **streamlit run [Path to file]/streamlit_final.py**
    The exact command will be printed as output in the console. Copy, paste and run that command in local terminal.
4. If a new browser window has not opened automatically then open local host in browser.
5. Explore the interactive visualization.

Note <br  /> - Sometimes an error might occur - 
    URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
This happens due to URL request being reject rejected or timeout. Re-running the code usually fixes this problem.


## DATA & DESIGN

For this analysis, we selected Industry specific GDP components:​

- Farm GDP for all states in US​

- Agriculture, Forestry, Fishing and Hunting GDP for all states in US​



Data Source for Economic data - Federal Reserve Economic Data (FRED).​


Further, we took climate data from - National centers for Environmental Information(NCEI, NOAA)​

To study the climate conditions, we analyzed states based on 4 factors:​

- Precipitation – Rain measured in Inches, for each month from 1998-2022​

- Heating Degree Days – demand for energy to heat a building if it reaches below 65°F​

- Maximum temperature – Maximum temperature in each month from 1998-2022​

- Minimum temperature – Minimum temperature in each month from 1998-2022​

We used correlation statistical method along with graph trends to observe a pattern​
## Hypothesis

#### Hypothesis 1

Climate change metrics (Precipitation , Heating Degree Days, Maximum temperature & Minimum temperature) has no correlation with GDP: Farm

#### Hypothesis 2

Climate change metrics (Precipitation , Heating Degree Days, Maximum temperature & Minimum temperature) has no Correlation with GDP​: Agriculture, Forestry, Fishing and Hunting


## ASSUMPTIONS

Measuring impact of any variable (like climate change) on economy of a state is a very complex process. ​

We do recognize that correlation does not mean causality.​

Correlation of these industry specific GDP with climate change metrics here means that there is a possibility that climate change impacted these industries.​

Limited climate change metrics available for our analysis. ​
