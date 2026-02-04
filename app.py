import pandas as pd
import streamlit as st
import plotly.express as px

DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

st.title("COVID-19 Data Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

countries = sorted(df['location'].dropna().unique())
country = st.selectbox("Select Country", countries)

filtered_df = df[df['location'] == country]

fig = px.line(
    filtered_df,
    x="date",
    y="total_cases",
    title=f"Total COVID-19 Cases in {country}"
)

st.plotly_chart(fig, width="stretch")