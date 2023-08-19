import streamlit as st
import pandas as pd
import plotly.express as px
import json

# constants
DATA = 'data/covid.csv'
DATE_COLUMN = 'date'


# functions
@st.cache_data
def load_data():
    return pd.read_csv(DATA, parse_dates=[DATE_COLUMN])


def draw_map_cases():
    fig = px.choropleth_mapbox(df,
                               geojson=json_locations,
                               locations='iso_code',
                               color='total_cases_per_million',
                               color_continuous_scale="Reds",
                               mapbox_style="carto-positron",
                               title="COVID 19 cases per million",
                               zoom=1,
                               opacity=0.5,
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


def draw_map_deaths():
    fig = px.choropleth_mapbox(df,
                               geojson=json_locations,
                               locations='iso_code',
                               color='total_deaths_per_million',
                               color_continuous_scale="Greys",
                               mapbox_style="carto-positron",
                               title="Deaths from COVID 19 per million",
                               zoom=1,
                               opacity=0.5,
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


def draw_map_vaccine():
    fig = px.choropleth_mapbox(df,
                               geojson=json_locations,
                               locations='iso_code',
                               color='people_vaccinated_per_hundred',
                               color_continuous_scale="BuGn",
                               mapbox_style="carto-positron",
                               title="Vaccinations from COVID 19 per hundred",
                               zoom=1,
                               opacity=0.5,
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


with open('data/countries.geo.json') as json_file:
    json_locations = json.load(json_file)

st.title("COVID 19 IN THE WORLD DASHBOARD")
st.write("""This dashboard will present the spread of COVID-19 in the world by visualizing the timeline of the total cases and deaths. As well as the total number of vaccinated people.""")

# Titles and Mode selections
st.sidebar.title("About")
st.sidebar.info(
    """
    COVID 19 IN THE WORLD DASHBOARD
    """
)

# Load data
df = load_data()

show_data = st.sidebar.checkbox('Show raw data')
if show_data == True:
    st.subheader('Raw data')
    st.markdown(
        "#### Data on COVID-19 (coronavirus) by Our World in Data could be found [here](https://github.com/owid/covid-19-data/tree/master/public/data).")
    st.write(df)



##### SIDEBAR
#slider to chose date
show_timerange = st.sidebar.checkbox("Show date range")
if show_timerange == True:
    # Calculate the timerange for the slider
    min_ts = min(df[DATE_COLUMN]).to_pydatetime()
    max_ts = max(df[DATE_COLUMN]).to_pydatetime()
    day_date = pd.to_datetime(st.sidebar.slider("Date to chose",
                                                min_value=min_ts,
                                                max_value=max_ts,
                                                value=max_ts
                                                )
                              )
    st.write(f"Data for {day_date.date()}")
    df = df[(df['date'] == day_date)]

# selectbox to chose between cases, deaths or total_vaccinations
select_event = st.sidebar.selectbox('Show map', ('cases per million', 'deaths per million', 'vaccinated per hundred'))
if select_event == 'cases per million':
    st.plotly_chart(draw_map_cases(),
                    use_container_width=True
                    )

if select_event == 'deaths per million':
    st.plotly_chart(draw_map_deaths(),
                    use_container_width=True
                    )

if select_event == 'vaccinated per hundred':
    st.plotly_chart(draw_map_vaccine(),
                    use_container_width=True
                    )


st.sidebar.info("How are you feeling?")
