
# Loading Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide")
from fredapi import Fred

#Using FRED API Key
fred_key = 'e97ead98bf794c0a4316ef8c10370f31'


# CREATING FRED OBJECT
fred = Fred(api_key=fred_key)

# # PULLING RAW DATA - SERIES
# il_gdp = fred.get_series('NGMP16980')

plt.style.use('fivethirtyeight')
pd.options.display.max_columns = 500
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]


state_mapping_GDP = {
 'California' : 'CARGSP',
 'Florida' : 'FLRGSP',
 'Minnesota' : 'MNRGSP',
 'Texas' : 'TXRGSP',
 'New York' : 'NYRGSP',
 'Pennsylvania' : 'PARGSP',
 'Alaska' : 'AKRGSP',
 'Illinois' : 'ILRGSP',
 'Utah' : 'UTRGSP',
 'Louisiana' : 'LARGSP',
 'Hawaii' : 'HIRGSP',
 'Virginia' : 'VARGSP',
 'South Carolina' : 'SCRGSP',
 'Alabama' : 'ALRGSP',
 'Ohio' : 'OHRGSP',
 'Mississippi' : 'MSRGSP',
 'Wyoming' : 'WYRGSP',
 'Michigan' : 'MIRGSP',
 'North Dakota' : 'NDRGSP',
 'Massachusetts' : 'MARGSP',
 'Wisconsin' : 'WIRGSP',
 'Georgia' : 'GARGSP',
 'North Carolina' : 'NCRGSP',
 'Arizona' : 'AZRGSP',
 'Kansas' : 'KSRGSP',
 'Colorado' : 'CORGSP',
 'Montana' : 'MTRGSP',
 'New Mexico' : 'NMRGSP',
 'Iowa' : 'IARGSP',
 'Idaho' : 'IDRGSP',
 'Delaware' : 'DERGSP',
 'Maryland' : 'MDRGSP',
 'New Jersey' : 'NJRGSP',
 'Tennessee' : 'TNRGSP',
 'Vermont' : 'VTRGSP',
 'Oklahoma' : 'OKRGSP',
 'Nebraska' : 'NERGSP',
 'Kentucky' : 'KYRGSP',
 'Oregon' : 'ORRGSP',
 'Missouri' : 'MORGSP',
 'Connecticut' : 'CTRGSP',
 'Washington' : 'WARGSP',
 'West Virginia' : 'WVRGSP',
 'Arkansas' : 'ARRGSP',
 'Nevada' : 'NVRGSP',
 'Maine' : 'MERGSP',
 'South Dakota' : 'SDRGSP',
 'the District of Columbia' : 'DCRGSP',
 'Rhode Island' : 'RIRGSP',
 'Indiana' : 'INRGSP',
#  'the United States' : 'USRGSP',
 'New Hampshire' : 'NHRGSP'
}

state_mapping = {'California': ['CAFARMRGSP', 4],
                 'Florida': ['FLFARMRGSP', 8],
                 'Minnesota': ['MNFARMRGSP', 21],
                 'Texas': ['TXFARMRGSP', 41],
                 'New York': ['NYFARMRGSP', 30],
                 'Pennsylvania': ['PAFARMRGSP', 36],
                 'Alaska': ['AKFARMRGSP', 50],
                 'Illinois': ['ILFARMRGSP', 11],
                 'Utah': ['UTFARMRGSP', 42],
                 'Louisiana': ['LAFARMRGSP', 16], 
                 'Hawaii': ['HIFARMRGSP'],
                 'Virginia': ['VAFARMRGSP', 44],
                 'South Carolina': ['SCFARMRGSP', 38],
                 'Alabama': ['ALFARMRGSP', 1],
                 'Ohio': ['OHFARMRGSP', 33],
                 'Mississippi': ['MSFARMRGSP', 22],
                 'Wyoming': ['WYFARMRGSP', 48],
                 'Michigan': ['MIFARMRGSP', 20],
                 'North Dakota': ['NDFARMRGSP', 32],
                 'Massachusetts': ['MAFARMRGSP', 19],
                 'Wisconsin': ['WIFARMRGSP', 47],
                 'Georgia': ['GAFARMRGSP', 9],
                 'North Carolina': ['NCFARMRGSP', 31],
                 'Arizona': ['AZFARMRGSP', 2],
                 'Kansas': ['KSFARMRGSP', 14],
                 'Colorado': ['COFARMRGSP', 5],
                 'Montana': ['MTFARMRGSP', 24],
                 'New Mexico': ['NMFARMRGSP', 29],
                 'Iowa': ['IAFARMRGSP', 13],
                 'Idaho': ['IDFARMRGSP', 10], 
                 'Delaware': ['DEFARMRGSP', 7],
                 'Maryland': ['MDFARMRGSP', 18],
                 'New Jersey': ['NJFARMRGSP', 28], 
                 'Tennessee': ['TNFARMRGSP', 40], 
                 'Vermont': ['VTFARMRGSP', 43],
                 'Oklahoma': ['OKFARMRGSP', 34],
                 'Nebraska': ['NEFARMRGSP', 25],
                 'Kentucky': ['KYFARMRGSP', 15], 
                 'Oregon': ['ORFARMRGSP', 35],
                 'Missouri': ['MOFARMRGSP', 23],
                 'Connecticut': ['CTFARMRGSP', 6], 
                 'Washington': ['WAFARMRGSP', 45], 
                 'West Virginia': ['WVFARMRGSP', 46],
                 'Arkansas': ['ARFARMRGSP', 3], 
                 'Nevada': ['NVFARMRGSP', 26], 
                 'Maine': ['MEFARMRGSP', 17],
                 'South Dakota': ['SDFARMRGSP', 39],
                 'the District of Columbia': ['DCFARMRGSP'],
                 'Rhode Island': ['RIFARMRGSP', 37], 
                 'Indiana': ['INFARMRGSP', 12],
                 'New Hampshire': ['NHFARMRGSP', 27]}



# get list of all states in usa
states = list(state_mapping.keys())


# STREAMLIT STUFF

header = st.container()
dataset = st.container()
GDP_plot = st.container()
climate_plots = st.container()
climate_plots_2 = st.container()




# with header:
#     st.title("welcome to project")
#     st.text("project descr")

#     all_results = []

#     for key_state, value in state_mapping_GDP.items():
#         results = fred.get_series(state_mapping_GDP[key_state])
#         results = results.to_frame(name = key_state)
#         all_results.append(results)

#     gdp_result = pd.concat(all_results, axis=1)

#     # --------------- subplots ------------------------

        
#     fig, axs = plt.subplots(10, 5, figsize = (30,30), sharex=True)
#     axs = axs.flatten()

#     i = 0
#     for key_state, value in state_mapping_GDP.items():
#         if i == 50:
#             continue
#         ax2 = axs[i].twinx()
#         chart_selected_df = fred.get_series(state_mapping_GDP[key_state])
#         axs[i].set_title(key_state, fontsize = 10)
#         chart_selected_df.plot(ax=ax2)
#         ax2.grid(False)
#         i += 1

#     plt.tight_layout()

#     # st.write(plt.show())
#     st.pyplot(fig)

# with dataset:
#     st.header("Agriculture GDP Comparison")
#     st.text("dataset about taxi driver")

#     # PULLING RAW DATA - SERIES
#     il_gdp = fred.get_series('NGMP16980')


#     fig_farm = px.line(il_gdp, title='illinois gdp')
#     fig_farm.update_layout(
#     title="illinois gdP",
#     xaxis_title="Year",
#     yaxis_title="GDP",
#     legend_title="GDP in millions",
#     font=dict(
#         family="Courier New, monospace",
#         size=18
#     ))

#     st.write(fig_farm)


with GDP_plot:
    # df_st = fred.search('Real Gross Domestic Product: All Industry Total in*', order_by='popularity')
    # filt = (len(df_st['id']) <= 6)
    # mask = (df_st['id'].str.len() <= 6)
    # df_st = df_st.loc[mask]

    # df_st = df_st.loc[df_st['title'].str.contains('Real Gross Domestic Product: All Industry Total in*')]
    # result_title_list = df_st['title'].tolist()


    # # df_st is the dataframe which has the series name and the chart titles of all search results
    # df_st

    # # show the list
    # for each in result_title_list:
    #     print(each)


##-------------------------------------------------------------------------------------------------------
    st.header("Agriculture GDP statewise")
    st.text("Real Gross Domestic Product: Farms ")

    sel_col, disp_col = st.columns(2)

    states_selection = sel_col.selectbox('Select the state to see its GDP', options = states, index=12)

    # chart_selection = sel_col.selectbox('Real GDP vs Nominal GDP', options = ['Real', 'Nominal'], index=0)

    chart_selected_df = fred.get_series(state_mapping[states_selection][0])

    

    fig = px.line(chart_selected_df)

    # updating title, and layout of plot
    fig.update_layout(
    title=f'GDP (Farms) of {states_selection}',
    xaxis_title="year",
    yaxis_title="Millions of Dollars",
    font=dict(
        family="Courier New, monospace",
        size=18
    ))

    # Converting series into dataframe
    chart_selected_df = pd.DataFrame(chart_selected_df , columns=['GDP_value'])
    # extracting only year from date column
    year_df = chart_selected_df.index
    year_df = year_df.astype(str).str[:4]

    # resetting index with just year
    chart_selected_df.set_index(year_df, inplace=True, drop=True)
    # Dropping first column (to get years from 1998 instead of 1997)
    chart_selected_df = chart_selected_df.iloc[1: , :]


    st.write(fig)


with climate_plots:
    st.header(f'Climate of {states_selection}')
    st.text("Plotting climate data")

    left_col , right_col = st.columns([3,3])
    

    # getting climate precipiation series data from the link
    
    url_start_year = '1998'
    url_end_year   = '2022'
    url_parameter = 'pcp'
    # url_state_no = '8'
    url_state_no = state_mapping[states_selection][1]
    # url_state_no = str(state_mapping['Florida'][1])

    
    # climate_series_url = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{url_state_no}/{url_parameter}/ann/12/{url_start_year}-{url_end_year}?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    climate_series_url = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{url_state_no}/{url_parameter}/ann/12/{url_start_year}-{url_end_year}.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    print(f'climate url : {climate_series_url}')
    climate_series = pd.read_csv(climate_series_url, index_col='Date' , skiprows=4, usecols=['Value', 'Date'], on_bad_lines='skip')
    
    # extracting only year from date column
    year = climate_series.index
    year = year.astype(str).str[:4]

    # resetting index with just year
    climate_series.set_index(year, inplace=True, drop=True)



    # climate_series = pd.read_csv(climate_series_url, index_col='Date' , skiprows=4, usecols=['Value', 'Date'])
    print(f'Climate series head : {climate_series.head()}')

    # Creating plot
    fig_climate = px.line(climate_series, title=f'Precipitation of {states_selection} ')

    # updating title, and layout of plot
    fig_climate.update_layout(
    title=f'Precipitation of {states_selection}',
    xaxis_title="year",
    yaxis_title="precipitation in mm",
    # legend_title="GDP in millions",
    font=dict(
        family="Courier New, monospace",
        size=18
    ))


    # Correlation metric for precipitation
    corr = chart_selected_df['GDP_value'].corr(climate_series['Value'])
    corr = round(corr, 2)

    left_col.metric(label="Correlation", value= corr)

    left_col.write(fig_climate)



################################################################################################


    # getting climate Heating Degree Days series data from the link
    
    url_start_year_hdd = '1998'
    url_end_year_hdd   = '2022'
    url_parameter_hdd = 'hdd'
    # url_state_no = '8'
    url_state_no_hdd = state_mapping[states_selection][1]
    # url_state_no = str(state_mapping['Florida'][1])

    
    # climate_series_url = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{url_state_no}/{url_parameter}/ann/12/{url_start_year}-{url_end_year}?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    climate_series_url_2 = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{url_state_no_hdd}/{url_parameter_hdd}/ann/12/{url_start_year_hdd}-{url_end_year_hdd}.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    print(f'climate url : {climate_series_url_2}')
    climate_series_2 = pd.read_csv(climate_series_url_2, index_col='Date' , skiprows=4, usecols=['Value', 'Date'], on_bad_lines='skip')
    
    # extracting only year from date column
    year_hdd = climate_series_2.index
    year_hdd = year_hdd.astype(str).str[:4]

    # resetting index with just year
    climate_series_2.set_index(year, inplace=True, drop=True)



    # climate_series = pd.read_csv(climate_series_url, index_col='Date' , skiprows=4, usecols=['Value', 'Date'])
    print(f'Climate series No 2 head : {climate_series.head()}')

    # Creating plot 2
    fig_climate_2 = px.line(climate_series_2, title=f'Heating Degree Days of {states_selection} ')

    # Updating title and layout of plot
    fig_climate_2.update_layout(
    title=f'Heating Degree days of {states_selection}',
    xaxis_title="year",
    yaxis_title="Fahrenheit Degree-Days",
    # legend_title="GDP in millions",
    font=dict(
        family="Courier New, monospace",
        size=18
    ))

    # Correlation metric for heating days
    corr_2 = chart_selected_df['GDP_value'].corr(climate_series_2['Value'])
    corr_2 = round(corr_2, 2)

    right_col.metric(label="Correlation", value= corr_2)

    right_col.write(fig_climate_2)


with climate_plots_2:

    left_col , right_col = st.columns([3,3])
    

    # getting Max temp of state
    
    url_start_year = '1998'
    url_end_year   = '2022'
    url_parameter = 'tmax'
    # url_state_no = '8'
    url_state_no = state_mapping[states_selection][1]
    # url_state_no = str(state_mapping['Florida'][1])

    
    # climate_series_url = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{url_state_no}/{url_parameter}/ann/12/{url_start_year}-{url_end_year}?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    climate_series_url = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{url_state_no}/{url_parameter}/ann/12/{url_start_year}-{url_end_year}.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    print(f'climate url : {climate_series_url}')
    climate_series = pd.read_csv(climate_series_url, index_col='Date' , skiprows=4, usecols=['Value', 'Date'], on_bad_lines='skip')
    
    # extracting only year from date column
    year = climate_series.index
    year = year.astype(str).str[:4]

    # resetting index with just year
    climate_series.set_index(year, inplace=True, drop=True)



    # climate_series = pd.read_csv(climate_series_url, index_col='Date' , skiprows=4, usecols=['Value', 'Date'])
    print(f'Climate series head : {climate_series.head()}')

    # Creating plot
    fig_climate = px.line(climate_series, title=f'Maximum Temp of {states_selection} ')

    # updating title, and layout of plot
    fig_climate.update_layout(
    title=f'Max temp of {states_selection}',
    xaxis_title="year",
    yaxis_title="Degrees Fahrenheit",
    # legend_title="GDP in millions",
    font=dict(
        family="Courier New, monospace",
        size=18
    ))


    # Correlation metric for precipitation
    corr = chart_selected_df['GDP_value'].corr(climate_series['Value'])
    corr = round(corr, 2)

    left_col.metric(label="Correlation", value= corr)

    left_col.write(fig_climate)



################################################################################################


    # getting Min temp data of state
    
    url_start_year_hdd = '1998'
    url_end_year_hdd   = '2022'
    url_parameter_hdd = 'tmin'
    # url_state_no = '8'
    url_state_no_hdd = state_mapping[states_selection][1]
    # url_state_no = str(state_mapping['Florida'][1])

    
    # climate_series_url = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{url_state_no}/{url_parameter}/ann/12/{url_start_year}-{url_end_year}?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    climate_series_url_2 = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{url_state_no_hdd}/{url_parameter_hdd}/ann/12/{url_start_year_hdd}-{url_end_year_hdd}.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    print(f'climate url : {climate_series_url_2}')
    climate_series_2 = pd.read_csv(climate_series_url_2, index_col='Date' , skiprows=4, usecols=['Value', 'Date'], on_bad_lines='skip')
    
    # extracting only year from date column
    year_hdd = climate_series_2.index
    year_hdd = year_hdd.astype(str).str[:4]

    # resetting index with just year
    climate_series_2.set_index(year, inplace=True, drop=True)



    # climate_series = pd.read_csv(climate_series_url, index_col='Date' , skiprows=4, usecols=['Value', 'Date'])
    print(f'Climate series No 2 head : {climate_series.head()}')

    # Creating plot 2
    fig_climate_2 = px.line(climate_series_2, title=f'Min Temp of {states_selection} ')

    # Updating title and layout of plot
    fig_climate_2.update_layout(
    title=f'Min temp of {states_selection}',
    xaxis_title="year",
    yaxis_title="Degree Fahrenheit ",
    # legend_title="GDP in millions",
    font=dict(
        family="Courier New, monospace",
        size=18
    ))

    # Correlation metric for heating days
    corr_2 = chart_selected_df['GDP_value'].corr(climate_series_2['Value'])
    corr_2 = round(corr_2, 2)

    right_col.metric(label="Correlation", value= corr_2)

    right_col.write(fig_climate_2)

