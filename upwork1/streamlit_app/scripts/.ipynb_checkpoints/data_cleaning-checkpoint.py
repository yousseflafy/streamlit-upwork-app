# scripts/data_loader.py
import pandas as pd
import streamlit as st

@st.cache_data
def load_data(filepath="../data/processed/pm25_cleaned.csv"):
    return pd.read_csv(filepath)