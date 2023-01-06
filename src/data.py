import pandas as pd
import streamlit as st


@st.cache(allow_output_mutation=True)
def get_data() -> pd.DataFrame:
    """Return hotel reservation CSV data as pandas DataFrame."""
    _df = pd.read_csv("data/Hotel_Reservations.csv")
    return _df


df = get_data()
