# Loading Packages
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from fredapi import Fred

# Using FRED API Key
fred_key = 'e97ead98bf794c0a4316ef8c10370f31'

# CREATING FRED OBJECT
fred = Fred(api_key=fred_key)

# setting plot styles
plt.style.use('fivethirtyeight')
pd.options.display.max_columns = 500
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]

# STREAMLIT STUFF

header = st.container()
dataset = st.container()
modelTraining = st.container()
climate_plots = st.container()

with header:
    st.title("welcome to project")
    st.text("project descr")

    # all_results = []

    # for key_state, value in state_mapping.items():
    #     results = fred.get_series(state_mapping[key_state])
    #     results = results.to_frame(name = key_state)
    #     all_results.append(results)

    # gdp_result = pd.concat(all_results, axis=1)

    # # --------------- subplots ------------------------

    # fig, axs = plt.subplots(10, 5, figsize = (30,30), sharex=True)
    # axs = axs.flatten()

    # i = 0
    # for key_state, value in state_mapping.items():
    #     if i == 50:
    #         continue
    #     ax2 = axs[i].twinx()
    #     chart_selected_df = fred.get_series(state_mapping[key_state])
    #     axs[i].set_title(key_state, fontsize = 10)
    #     chart_selected_df.plot(ax=ax2)
    #     ax2.grid(False)
    #     i += 1

    # plt.tight_layout()
    # plt.show()

    # # st.write(plt.show())
    # st.pyplot(fig)

with dataset:
    # PULLING RAW DATA - SERIES
    il_gdp = fred.get_series('NGMP16980')

    # key - state name; value - id to get GDP data from FRED for particular state
    state_mapping = {'California': ['CARGSP', 4], 'Florida': ['FLRGSP', 8], 'Minnesota': ['MNRGSP', 21],
                     'Texas': ['TXRGSP', 41],
                     'New York': ['NYRGSP', 30], 'Pennsylvania': ['PARGSP', 36], 'Alaska': ['AKRGSP', 50],
                     'Illinois': ['ILRGSP', 11],
                     'Utah': ['UTRGSP', 42], 'Louisiana': ['LARGSP', 16], 'Hawaii': ['HIRGSP'],
                     'Virginia': ['VARGSP', 44],
                     'South Carolina': ['SCRGSP', 38], 'Alabama': ['ALRGSP', 1], 'Ohio': ['OHRGSP', 33],
                     'Mississippi': ['MSRGSP', 22],
                     'Wyoming': ['WYRGSP', 48], 'Michigan': ['MIRGSP', 20], 'North Dakota': ['NDRGSP', 32],
                     'Massachusetts': ['MARGSP', 19],
                     'Wisconsin': ['WIRGSP', 47], 'Georgia': ['GARGSP', 9], 'North Carolina': ['NCRGSP', 31],
                     'Arizona': ['AZRGSP', 2],
                     'Kansas': ['KSRGSP', 14], 'Colorado': ['CORGSP', 5], 'Montana': ['MTRGSP', 24],
                     'New Mexico': ['NMRGSP', 29],
                     'Iowa': ['IARGSP', 13], 'Idaho': ['IDRGSP', 10], 'Delaware': ['DERGSP', 7],
                     'Maryland': ['MDRGSP', 18],
                     'New Jersey': ['NJRGSP', 28], 'Tennessee': ['TNRGSP', 40], 'Vermont': ['VTRGSP', 43],
                     'Oklahoma': ['OKRGSP', 34],
                     'Nebraska': ['NERGSP', 25], 'Kentucky': ['KYRGSP', 15], 'Oregon': ['ORRGSP', 35],
                     'Missouri': ['MORGSP', 23],
                     'Connecticut': ['CTRGSP', 6], 'Washington': ['WARGSP', 45], 'West Virginia': ['WVRGSP', 46],
                     'Arkansas': ['ARRGSP', 3], 'Nevada': ['NVRGSP', 26], 'Maine': ['MERGSP', 17],
                     'South Dakota': ['SDRGSP', 39],
                     'the District of Columbia': ['DCRGSP'], 'Rhode Island': ['RIRGSP', 37], 'Indiana': ['INRGSP', 12],
                     'New Hampshire': ['NHRGSP', 27]}

    parameter = {"Average Temperature": 'tavg', "Maximum Temperature": "tmax", "Minimum Temperature": "tmin",
                 "Precipitation": "pcp", \
                 "Cooling Degree Days": "hdd", "Heating Degree Days": "cdd",
                 "Palmer Drought Severity Index (PDSI)": "pdsi", \
                 "Palmer Hydrological Drought Index (PHDI)": "phdi", "Palmer Modified Drought Index (PMDI)": "pmdi",
                 "Palmer Z-Index": "zndx"}

    # get list of all states in usa
    states = list(state_mapping.keys())

    # sample graph for 1 state - Illinois
    st.header("Agriculture GDP Comparison")
    # st.text("Hello ji")

    fig = px.line(il_gdp, title='illinois gdp')
    fig.update_layout(
        title="illinois gdp",
        xaxis_title="Year",
        yaxis_title="GDP",
        legend_title="GDP in millions",
        font=dict(
            family="Courier New, monospace",
            size=18
        ))

    st.write(fig)

with modelTraining:
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
    st.header("2nd plot")
    st.text("creating experimental plot")

    sel_col, disp_col = st.columns(2)

    state_selection = sel_col.selectbox('Select the state to see its GDP', options=states, index=1)

    chart_selection = sel_col.selectbox('Real GDP vs Nominal GDP', options=['Real', 'Nominal'], index=0)

    chart_selected_df = fred.get_series(state_mapping[state_selection][0])

    fig = px.line(chart_selected_df)

    st.write(fig)

with climate_plots:
    st.header(f'Climate of States')
    st.text("Plotting climate data")

    new_sel_plot, new_disp_plot = st.columns(2)
    print(type(new_sel_plot))


    # getting climate series data from the link
    # parameter_selection = disp_col.selectbox('Select the parameter', options=parameter.keys(), index=0)
    state_selection = disp_col.selectbox('Select the state to see its temp', options=states, index=0)

    https: // www.ncei.noaa.gov / access / monitoring / climate - at - a - glance / statewide / time - series / 4 / tmax / all / 12 / 1970 - 2022.
    csv
    # from_year = disp_col.text_input('Start Year, from 1970')
    # to_year = disp_col.text_input('End Year, till date')
    url = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/' + \
          str(state_mapping[state_selection][1]) + '/tavg/12/12/1998-2022.csv?base_prd=true&begbaseyear=1970&endbaseyear=2022'
    climate_data = pd.read_csv(url, index_col='Date', skiprows=4, usecols=['Value', 'Date'])

    fig_climate = px.line(climate_data, title=f'Climate of {state_selection} ')

    fig_climate.update_layout(
        title=f'{parameter_selection} of {state_selection}',
        xaxis_title= parameter_selection,
        yaxis_title="year",
        # legend_title="GDP in millions",
        font=dict(
            family="Courier New, monospace",
            size=18
        ))

    st.write(fig_climate)
