# Loading Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
from fredapi import Fred

# Using FRED API Key
fred_key = 'e97ead98bf794c0a4316ef8c10370f31'

# CREATING FRED OBJECT
fred = Fred(api_key=fred_key)

# # PULLING RAW DATA - SERIES
# il_gdp = fred.get_series('NGMP16980')

plt.style.use('fivethirtyeight')
pd.options.display.max_columns = 500
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]

state_mapping_GDP = {
    'California': 'CARGSP',
    'Florida': 'FLRGSP',
    'Minnesota': 'MNRGSP',
    'Texas': 'TXRGSP',
    'New York': 'NYRGSP',
    'Pennsylvania': 'PARGSP',
    'Alaska': 'AKRGSP',
    'Illinois': 'ILRGSP',
    'Utah': 'UTRGSP',
    'Louisiana': 'LARGSP',
    'Hawaii': 'HIRGSP',
    'Virginia': 'VARGSP',
    'South Carolina': 'SCRGSP',
    'Alabama': 'ALRGSP',
    'Ohio': 'OHRGSP',
    'Mississippi': 'MSRGSP',
    'Wyoming': 'WYRGSP',
    'Michigan': 'MIRGSP',
    'North Dakota': 'NDRGSP',
    'Massachusetts': 'MARGSP',
    'Wisconsin': 'WIRGSP',
    'Georgia': 'GARGSP',
    'North Carolina': 'NCRGSP',
    'Arizona': 'AZRGSP',
    'Kansas': 'KSRGSP',
    'Colorado': 'CORGSP',
    'Montana': 'MTRGSP',
    'New Mexico': 'NMRGSP',
    'Iowa': 'IARGSP',
    'Idaho': 'IDRGSP',
    'Delaware': 'DERGSP',
    'Maryland': 'MDRGSP',
    'New Jersey': 'NJRGSP',
    'Tennessee': 'TNRGSP',
    'Vermont': 'VTRGSP',
    'Oklahoma': 'OKRGSP',
    'Nebraska': 'NERGSP',
    'Kentucky': 'KYRGSP',
    'Oregon': 'ORRGSP',
    'Missouri': 'MORGSP',
    'Connecticut': 'CTRGSP',
    'Washington': 'WARGSP',
    'West Virginia': 'WVRGSP',
    'Arkansas': 'ARRGSP',
    'Nevada': 'NVRGSP',
    'Maine': 'MERGSP',
    'South Dakota': 'SDRGSP',
    'the District of Columbia': 'DCRGSP',
    'Rhode Island': 'RIRGSP',
    'Indiana': 'INRGSP',
    #  'the United States' : 'USRGSP',
    'New Hampshire': 'NHRGSP'
}

# Dict --> State: [GDP code,
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

parameter_dict = {'Average Temperature': 'tavg', 'Maximum Temperature': 'tmax', 'Minimum Temperature': 'tmin', \
                  'Precipitation': 'pcp', 'Heating Degree Days': 'hdd'}

# get list of all states in usa
states = list(state_mapping.keys())

# STREAMLIT STUFF

header = st.container()
dataset = st.container()
GDP_plot = st.container()
climate_plots_A = st.container()
climate_plots_B = st.container()


def get_climate_data(start_year, end_year, parameter, state_num):
    """
    :param start_year: start year for the duration of dataset
    :param end_year: end year for the duration of dataset
    :param parameter: climatic parameter, in parameter_dict
    :param state_num: state number from the state_mapping dictionary
    :return: returns a dataframe with from start to end year for specific parameter and specific state
    """

    climate_series_url = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/' \
                         f'{state_num}/{parameter}/ann/12/{start_year}-{end_year}.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'
    print(f'climate url : {climate_series_url}')
    climate_df = pd.read_csv(climate_series_url, index_col='Date', skiprows=4, usecols=['Value', 'Date'],
                             on_bad_lines='skip')
    year = climate_df.index
    year = year.astype(str).str[:4]

    # resetting index with just year
    climate_df.set_index(year, inplace=True, drop=True)

    return climate_df


def calc_corr(df, climate_df):
    """
    :param df: GDP dataframe for specific state
    :param climate_df: climate data for the same state
    :return: magnitude of correlation between the GDP values and climate values
    """
    correlation = df['GDP_value'].corr(climate_df['Value'])
    correlation = round(correlation, 2)

    return correlation


def create_plot(parameter, y_axis_title, df):
    """
    :param parameter: parameter based on which graph is plotted v/s year
    :param y_axis_title: title of y-axis
    :param df: data used to plot data
    :return: plot with formatting
    """
    figure = px.line(df, title=f'{parameter} of {states_selection}')

    # updating title, and layout of plot
    figure.update_layout(
        title=f'{parameter} of {states_selection}',
        xaxis_title="year",
        yaxis_title=f'{y_axis_title}',
        font=dict(
            family="Courier New, monospace",
            size=18
        ))

    return figure


with GDP_plot:
    st.header("Agriculture GDP statewise")
    st.text("Real Gross Domestic Product: Farms ")

    sel_col, disp_col = st.columns(2)

    states_selection = sel_col.selectbox('Select the state to see its GDP', options=states, index=12)

    # chart_selection = sel_col.selectbox('Real GDP vs Nominal GDP', options = ['Real', 'Nominal'], index=0)

    chart_selected_df = fred.get_series(state_mapping[states_selection][0])

    # Plotting data v/s year
    fig = create_plot('GDP(Farms)', 'Millions of Dollars', chart_selected_df)

    # Converting series into dataframe
    chart_selected_df = pd.DataFrame(chart_selected_df, columns=['GDP_value'])
    # extracting only year from date column
    year_df = chart_selected_df.index
    year_df = year_df.astype(str).str[:4]

    # resetting index with just year
    chart_selected_df.set_index(year_df, inplace=True, drop=True)
    # Dropping first column (to get years from 1998 instead of 1997)
    chart_selected_df = chart_selected_df.iloc[1:, :]

    st.write(fig)


with climate_plots_A:
    st.header(f'Climate of {states_selection}')
    st.text("Plotting climate data")

    left_col, right_col = st.columns([3, 3])

    # getting climate precipitation series data from the link
    climate_series_1 = get_climate_data('1998', '2022', 'pcp', state_mapping[states_selection][1])

    print(f'Climate series head : {climate_series_1.head()}')

    # Creating plot
    fig_1 = create_plot('Precipitation', 'precipitation in mm', climate_series_1)

    # Correlation metric for precipitation
    corr = calc_corr(chart_selected_df, climate_series_1)

    left_col.metric(label="Correlation", value=corr)
    left_col.write(fig_1)

    ################################################################################################

    # getting climate Heating Degree Days series data from the link
    climate_series_2 = get_climate_data('1998', '2022', 'hdd', state_mapping[states_selection][1])

    # climate_series = pd.read_csv(climate_series_url, index_col='Date' , skiprows=4, usecols=['Value', 'Date'])
    print(f'Climate series No 2 head : {climate_series_2.head()}')

    # Creating plot 2
    fig_2 = create_plot('Heating Degree days', 'Fahrenheit Degree-Days', climate_series_2)

    # Correlation metric for heating days
    corr_2 = calc_corr(chart_selected_df, climate_series_2)

    right_col.metric(label="Correlation", value=corr_2)
    right_col.write(fig_2)

with climate_plots_B:
    left_col, right_col = st.columns([3, 3])

    # getting Max temp of state
    climate_series_3 = get_climate_data('1998', '2022', 'tmax', state_mapping[states_selection][1])
    # climate_series = pd.read_csv(climate_series_url, index_col='Date' , skiprows=4, usecols=['Value', 'Date'])
    print(f'Climate series head : {climate_series_3.head()}')

    # Creating plot
    fig_3 = create_plot('Max temp', '°F', climate_series_3)
    # Correlation metric for precipitation
    corr_3 = calc_corr(chart_selected_df, climate_series_3)

    left_col.metric(label="Correlation", value=corr_3)
    left_col.write(fig_3)

    ################################################################################################

    # getting Min temp data of state
    climate_series_4 = get_climate_data('1998', '2022', 'tmin', state_mapping[states_selection][1])

    # climate_series = pd.read_csv(climate_series_url, index_col='Date' , skiprows=4, usecols=['Value', 'Date'])
    print(f'Climate series No 2 head : {climate_series_4.head()}')

    # Creating plot 2
    fig_4 = create_plot('Mim temp', '°F', climate_series_4)


    # Correlation metric for heating days
    corr_4 = calc_corr(chart_selected_df, climate_series_4)

    right_col.metric(label="Correlation", value=corr_4)
    right_col.write(fig_4)
