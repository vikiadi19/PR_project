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

header = st.beta_container()
dataset = st.beta_container()
modelTraining = st.beta_container()
climate_plots = st.beta_container()

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
    state_mapping = {
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
        'New Hampshire': 'NHRGSP',
        #  'the United States' : 'USRGSP'
    }

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

    sel_col, disp_col = st.beta_columns(2)

    state_selection = sel_col.selectbox('Select the state to see its GDP', options=states, index=1)

    chart_selection = sel_col.selectbox('Real GDP vs Nominal GDP', options=['Real', 'Nominal'], index=0)

    chart_selected_df = fred.get_series(state_mapping[state_selection])

    fig = px.line(chart_selected_df)

    st.write(fig)

with climate_plots:
    st.header(f'Climate of {state_selection}')
    st.text("Plotting climate data")

    # getting climate series data from the link
    climate_series = pd.read_csv(
        'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/8/pcp/12/12/1998-2022.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000',
        index_col='Date', skiprows=4, usecols=['Value', 'Date'])

    fig_climate = px.line(climate_series, title=f'Climate of {state_selection} ')

    fig_climate.update_layout(
        title=f'Climate of {state_selection}',
        xaxis_title="climate",
        yaxis_title="year",
        # legend_title="GDP in millions",
        font=dict(
            family="Courier New, monospace",
            size=18
        ))

    st.write(fig_climate)

    ## New comment
