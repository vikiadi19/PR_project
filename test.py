state_mapping = {'California': ['CARGSP', 4], 'Florida': ['FLRGSP', 8], 'Minnesota': ['MNRGSP', 21], 'Texas': ['TXRGSP', 41],
 'New York': ['NYRGSP', 30], 'Pennsylvania': ['PARGSP', 36], 'Alaska': ['AKRGSP', 50], 'Illinois': ['ILRGSP', 11],
 'Utah': ['UTRGSP', 42], 'Louisiana': ['LARGSP', 16], 'Hawaii': ['HIRGSP'], 'Virginia': ['VARGSP', 44],
 'South Carolina': ['SCRGSP', 38], 'Alabama': ['ALRGSP', 1], 'Ohio': ['OHRGSP', 33], 'Mississippi': ['MSRGSP', 22],
 'Wyoming': ['WYRGSP', 48], 'Michigan': ['MIRGSP', 20], 'North Dakota': ['NDRGSP', 32], 'Massachusetts': ['MARGSP', 19],
 'Wisconsin': ['WIRGSP', 47], 'Georgia': ['GARGSP', 9], 'North Carolina': ['NCRGSP', 31], 'Arizona': ['AZRGSP', 2],
 'Kansas': ['KSRGSP', 14], 'Colorado': ['CORGSP', 5], 'Montana': ['MTRGSP', 24], 'New Mexico': ['NMRGSP', 29],
 'Iowa': ['IARGSP', 13], 'Idaho': ['IDRGSP', 10], 'Delaware': ['DERGSP', 7], 'Maryland': ['MDRGSP', 18],
 'New Jersey': ['NJRGSP', 28], 'Tennessee': ['TNRGSP', 40], 'Vermont': ['VTRGSP', 43], 'Oklahoma': ['OKRGSP', 34],
 'Nebraska': ['NERGSP', 25], 'Kentucky': ['KYRGSP', 15], 'Oregon': ['ORRGSP', 35], 'Missouri': ['MORGSP', 23],
 'Connecticut': ['CTRGSP', 6], 'Washington': ['WARGSP', 45], 'West Virginia': ['WVRGSP', 46],
 'Arkansas': ['ARRGSP', 3], 'Nevada': ['NVRGSP', 26], 'Maine': ['MERGSP', 17], 'South Dakota': ['SDRGSP', 39],
 'the District of Columbia': ['DCRGSP'], 'Rhode Island': ['RIRGSP', 37], 'Indiana': ['INRGSP', 12],
 'New Hampshire': ['NHRGSP', 27]}

# "
# <option value="1">Alabama</option>
# <option value="50">Alaska</option>
# <option value="2">Arizona</option>
# <option value="3">Arkansas</option>
# <option value="4">California</option>
# <option value="5">Colorado</option>
# <option value="6">Connecticut</option>
# <option value="7">Delaware</option>
# <option value="8">Florida</option>
# <option value="9">Georgia</option>
# <option value="10">Idaho</option>
# <option value="11">Illinois</option>
# <option value="12">Indiana</option>
# <option value="13">Iowa</option>
# <option value="14">Kansas</option>
# <option value="15">Kentucky</option>
# <option value="16">Louisiana</option>
# <option value="17">Maine</option>
# <option value="18">Maryland</option>
# <option value="19">Massachusetts</option>
# <option value="20">Michigan</option>
# <option value="21">Minnesota</option>
# <option value="22">Mississippi</option>
# <option value="23">Missouri</option>
# <option value="24">Montana</option>
# <option value="25">Nebraska</option>
# <option value="26">Nevada</option>
# <option value="27">New Hampshire</option>
# <option value="28">New Jersey</option>
# <option value="29">New Mexico</option>
# <option value="30">New York</option>
# <option value="31">North Carolina</option>
# <option value="32">North Dakota</option>
# <option value="33">Ohio</option>
# <option value="34">Oklahoma</option>
# <option value="35">Oregon</option>
# <option value="36">Pennsylvania</option>
# <option value="37">Rhode Island</option>
# <option value="38">South Carolina</option>
# <option value="39">South Dakota</option>
# <option value="40">Tennessee</option>
# <option value="41">Texas</option>
# <option value="42">Utah</option>
# <option value="43">Vermont</option>
# <option value="44">Virginia</option>
# <option value="45">Washington</option>
# <option value="46">West Virginia</option>
# <option value="47">Wisconsin</option>
# <option value="48">Wyoming</option>
# "

lis = []

# for k, l in state_mapping.items():
#     if len(l) > 1:
#         lis.append(l[1])
#
# lis.sort()
# print(lis)
#
#
# states = state_mapping.keys()
# states = list(states)
# states.sort()
# map = {}
#
# count = 0
# for state in states:
#     if state != 'Alaska' or state != 'Hawaii':
#         map[state] = (count+1)
#         count += 1
#
# # map['Alaska'] = [50]
# del map['the District of Columbia']
# print(map)

import pandas as pd

state_selection = 'California'
url = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/'+\
          str(state_mapping[state_selection][1]) + 'pcp/12/12/1998-2022.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'
climate_data = pd.read_csv(url, index_col='Date', skiprows=4, usecols=['Value', 'Date'])

print(climate_data)


