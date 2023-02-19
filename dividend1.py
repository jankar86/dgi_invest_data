import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import fundamentalanalysis as fa
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# set title and layout
st.set_page_config(page_title="Dividend stock analysis", layout="wide")

# import api key for stock data
FA_API_KEY = os.getenv("FA_API_KEY")

TIME_DIFFS = {
    "1 week": pd.DateOffset(weeks=1),
    "1 month": pd.DateOffset(months=1),
    "3 months": pd.DateOffset(months=3),
    "1 year": pd.DateOffset(years=1),
    "3 years": pd.DateOffset(years=3),
    "5 years": pd.DateOffset(years=5)
}
