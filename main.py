import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px



masterdf = pd.read_csv("MasterDataset.csv")



def FindCities(price_intervals):
    ans = []
    for index, row in masterdf.iterrows():
        temp = []
        if(row['PriceMean'] >= price_intervals[0] and row['PriceMean'] <= price_intervals[1]):
            temp.append(row['city'])
            temp.append(row['state_name'])
            temp.append(row['PriceMean'])
            if(row['_merge'] == 'both'):
                ethnicity = row.iloc[18:25]
                temp.append(ethnicity)
            ans.append(temp)
    return ans



st.title('DreamCityFinder')
# sidebar:
add_slider = st.sidebar.slider(
    'Select Rent range',
    0, 4000, (900, 1000)
)
temp_slider = st.sidebar.slider(
    'Select Temp range',
    0.0, 100.0, (25.0, 75.0)
)
age_slider = st.sidebar.slider(
    'Select Age range',
    0.0, 100.0, (25.0, 75.0)
)


add_selectbox = st.sidebar.selectbox(
    'How dense do you want the city to be',
    ('Rural', 'Urban')
)



names = FindCities(add_slider)


expanders = []
limit = 0
for name in names:
    if(limit == 20):
        break
    expander = st.beta_expander(f"{name[0]},{name[1]}")
    if len(name) == 4 :
        with expander:
            f'Average Rent Price Range: {add_slider[0]} to {add_slider[1]}' 
            
            f'Average Rent: {name[2]}'
            
            'STATS'
            fig = px.bar(name[3], x=name[3].index, y=name[3].values, color=name[3].index, labels={'y':'Percent of population 2013'})
            fig.update_layout(xaxis={'visible': True, 'showticklabels': False})
            st.plotly_chart(fig,use_container_width=False, sharing="streamlit")
    else:
        with expander:
            'No diveristy stats available'
    limit += 1

    


