import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    filepath = os.path.join(base_path, '..', 'data', 'processed', 'pm25_cleaned.csv')
    df = pd.read_csv(filepath)

    df['Year'] = pd.to_datetime(df['Period'], format='%Y').dt.year
    return df
